import os
import io
import wave
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pydub import AudioSegment
from pydub.effects import normalize

os.makedirs('output', exist_ok=True)
os.makedirs('public/media', exist_ok=True)

# 1. Load uploaded cloned voice
cloned_voice = AudioSegment.from_wav('audio/user_cloned_voice.wav')
voice_dur = len(cloned_voice) / 1000.0
print(f"Cloned Voice Duration: {voice_dur:.2f}s")

# 2. Add ambient music bed & SFX
sr = 44100
total_master_ms = len(cloned_voice) + 500
t_arr = np.linspace(0, total_master_ms / 1000.0, int(sr * total_master_ms / 1000.0), False)

c3, eb3, g3, bb3 = 130.81, 155.56, 196.00, 233.08
music_signal = (
    0.15 * np.sin(2 * np.pi * c3 * t_arr) +
    0.12 * np.sin(2 * np.pi * eb3 * t_arr) +
    0.10 * np.sin(2 * np.pi * g3 * t_arr) +
    0.08 * np.sin(2 * np.pi * bb3 * t_arr)
) * (0.85 + 0.15 * np.sin(2 * np.pi * (100/60) * t_arr))

music_pcm = (music_signal * 32767).astype(np.int16)
stereo_music = np.column_stack((music_pcm, music_pcm))

music_io = io.BytesIO()
with wave.open(music_io, 'wb') as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(sr)
    wf.writeframes(stereo_music.tobytes())
music_io.seek(0)
bg_music = AudioSegment.from_wav(music_io) - 22

def generate_tone(freq, dur_ms, fade=True):
    t_a = np.linspace(0, dur_ms/1000.0, int(sr * dur_ms/1000.0), False)
    sig = np.sin(2 * np.pi * freq * t_a)
    if fade:
        sig = sig * np.linspace(1, 0, len(t_a))
    pcm = (sig * 0.4 * 32767).astype(np.int16)
    st = np.column_stack((pcm, pcm))
    b_io = io.BytesIO()
    with wave.open(b_io, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(st.tobytes())
    b_io.seek(0)
    return AudioSegment.from_wav(b_io)

sfx_whoosh = generate_tone(220, 400)
sfx_stamp = generate_tone(90, 600) + generate_tone(60, 600)

sfx_track = AudioSegment.silent(duration=total_master_ms)
sfx_track = sfx_track.overlay(sfx_whoosh, position=200)
if total_master_ms > 12000:
    sfx_track = sfx_track.overlay(sfx_stamp, position=int(voice_dur * 1000) - 1500)

master_audio = bg_music.overlay(sfx_track).overlay(cloned_voice)
master_audio = normalize(master_audio, headroom=0.5)
master_audio.export('audio/master_cloned_reel_audio.wav', format='wav')
master_audio.export('public/media/master_reel_audio.wav', format='wav')

# 3. Video Rendering
WIDTH = 1080
HEIGHT = 1920
FPS = 30
TOTAL_DURATION = len(master_audio) / 1000.0
TOTAL_FRAMES = int(TOTAL_DURATION * FPS)

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_regular = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def get_font(size, bold=True):
    p = font_path if bold else font_regular
    if os.path.exists(p):
        return ImageFont.truetype(p, size)
    return ImageFont.load_default()

font_caption = get_font(38, bold=True)
font_caption_lg = get_font(46, bold=True)
font_badge = get_font(26, bold=True)

img_s1 = Image.open('assets/borrowed_authority_scene1_n4.png').convert('RGB')
img_s2 = Image.open('assets/borrowed_authority_scene2_statute.png').convert('RGB')
img_s3 = Image.open('assets/borrowed_authority_scene3_checklist.png').convert('RGB')

captions = [
    (0.0, 4.0, "ONE SINGLE CALENDAR MISTAKE...", "#ef4444", "TRIBUNALS ONTARIO FORM N4"),
    (4.0, 9.0, "CAN DISMISS YOUR ENTIRE CASE", "#f59e0b", "8+ MONTH DELAY"),
    (9.0, 14.0, "THOUSANDS OF APPLICATIONS THROWN OUT", "#ef4444", "LTB TECHNICAL DEFECT"),
    (14.0, TOTAL_DURATION, "BEFORE THE HEARING EVEN STARTS!", "#dc2626", "VOID UNDER RTA S. 59"),
]

def render_frame(frame_idx):
    t = frame_idx / FPS
    local_t = t
    scene_dur = TOTAL_DURATION
    zoom = 1.0 + 0.08 * (local_t / scene_dur)
    pan_y = int(60 * (local_t / scene_dur))

    w_z = int(WIDTH / zoom)
    h_z = int(HEIGHT / zoom)
    x1 = (WIDTH - w_z) // 2
    y1 = min((HEIGHT - h_z) // 2 + pan_y, HEIGHT - h_z)
    cropped = img_s1.crop((x1, y1, x1 + w_z, y1 + h_z))
    frame = cropped.resize((WIDTH, HEIGHT), Image.Resampling.BILINEAR)
    
    draw = ImageDraw.Draw(frame)

    current_cap = None
    for (start, end, text, col, badge) in captions:
        if start <= t < end:
            current_cap = (text, col, badge, start, end)
            break
            
    if current_cap:
        text, col, badge, start, end = current_cap
        cap_prog = (t - start) / (end - start)
        
        card_w = 980
        card_h = 170
        card_x = (WIDTH - card_w) // 2
        card_y = 1680

        draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=24, fill=(10, 15, 29), outline=(51, 65, 85), width=3)
        
        badge_w = 400
        badge_h = 36
        draw.rounded_rectangle([card_x + 30, card_y + 16, card_x + 30 + badge_w, card_y + 16 + badge_h], radius=8, fill=col)
        draw.text((card_x + 30 + badge_w // 2, card_y + 16 + badge_h // 2), badge, fill=(0, 0, 0) if col != "#1e293b" else (255, 255, 255), font=font_badge, anchor="mm")

        draw.text((card_x + 30, card_y + 70), text, fill=(255, 255, 255), font=font_caption_lg)
        
        bar_w = int((card_w - 60) * cap_prog)
        draw.rectangle([card_x + 30, card_y + card_h - 18, card_x + 30 + bar_w, card_y + card_h - 12], fill=col)

    draw.rounded_rectangle([40, 30, 420, 80], radius=12, fill=(15, 23, 42), outline=(51, 65, 85), width=2)
    draw.text((230, 55), "⚖️ ONTARIO RTA ADVISORY", fill=(245, 158, 11), font=font_badge, anchor="mm")

    draw.rounded_rectangle([WIDTH - 240, 30, WIDTH - 40, 80], radius=12, fill=(15, 23, 42), outline=(51, 65, 85), width=2)
    mins = int(t // 60)
    secs = int(t % 60)
    tot_mins = int(TOTAL_DURATION // 60)
    tot_secs = int(TOTAL_DURATION % 60)
    draw.text((WIDTH - 140, 55), f"{mins}:{secs:02d} / {tot_mins}:{tot_secs:02d}", fill=(203, 213, 225), font=font_badge, anchor="mm")

    return frame.tobytes()

print(f"Starting video render with cloned voice: {TOTAL_FRAMES} frames ({TOTAL_DURATION:.2f}s) @ 1080x1920 30fps...")

ffmpeg_cmd = [
    'ffmpeg',
    '-y',
    '-f', 'rawvideo',
    '-vcodec', 'rawvideo',
    '-s', f'{WIDTH}x{HEIGHT}',
    '-pix_fmt', 'rgb24',
    '-r', str(FPS),
    '-i', '-',
    '-i', 'audio/master_cloned_reel_audio.wav',
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    '-preset', 'fast',
    '-crf', '19',
    '-c:a', 'aac',
    '-b:a', '192k',
    '-shortest',
    'output/ontario_n4_calendar_trap_reel.mp4'
]

pipe = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

for f in range(TOTAL_FRAMES):
    raw_frame = render_frame(f)
    pipe.stdin.write(raw_frame)
    if f % (FPS * 5) == 0:
        print(f"  Rendered {f}/{TOTAL_FRAMES} frames ({(f/TOTAL_FRAMES)*100:.1f}%)...")

pipe.stdin.close()
pipe.wait()

print("Cloned Video render complete!")
subprocess.run(['cp', 'output/ontario_n4_calendar_trap_reel.mp4', 'public/media/ontario_n4_calendar_trap_reel.mp4'])
print("Copied final video to public/media/ontario_n4_calendar_trap_reel.mp4")
