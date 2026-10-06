import os
import sys
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

os.makedirs('output', exist_ok=True)
os.makedirs('output/previews', exist_ok=True)
os.makedirs('public/media', exist_ok=True)

WIDTH = 1080
HEIGHT = 1920
FPS = 30

DUR1 = 16.0  # Scene 1: Form N4 Calendar Trap
DUR2 = 33.2  # Scene 2: RTA s. 59 & LTB Rule 3
DUR3 = 19.6  # Scene 3: Pre-Filing Checklist & CTA
TOTAL_DURATION = DUR1 + DUR2 + DUR3
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
    (0.0, 3.5, "ONE SINGLE CALENDAR MISTAKE...", "#ef4444", "TRIBUNALS ONTARIO FORM N4"),
    (3.5, 8.0, "CAN DISMISS YOUR L1 EVICTION CASE", "#f59e0b", "8+ MONTH DELAY"),
    (8.0, 12.0, "THOUSANDS OF APPLICATIONS THROWN OUT", "#ef4444", "LTB TECHNICAL DEFECT"),
    (12.0, 16.0, "BEFORE THE HEARING EVEN STARTS!", "#dc2626", "VOID UNDER RTA S. 59"),
    (16.0, 21.0, "RTA S. 59 REQUIRES 14 DAYS NOTICE", "#3b82f6", "ONTARIO e-LAWS STATUTE"),
    (21.0, 26.5, "TRAP #1: DAY 0 EXCLUSION RULE", "#f59e0b", "COUNT STARTS NEXT DAY"),
    (26.5, 32.0, "DAY 1 IS THE DAY AFTER SERVING", "#eab308", "CALCULATION ERROR"),
    (32.0, 39.0, "MAILED IT? ADD 5 DAYS (LTB RULE 3)", "#ef4444", "19 DAYS TOTAL MINIMUM"),
    (39.0, 44.5, "OFF BY 24 HOURS = INSTANT DISMISSAL", "#dc2626", "ZERO BOARD DISCRETION"),
    (44.5, 49.2, "FILING FEE LOST & 8 MONTHS RESET!", "#ef4444", "START OVER AT DAY 1"),
    (49.2, 54.0, "NEVER SERVE WITHOUT VERIFYING!", "#10b981", "PRE-FILING CHECKLIST"),
    (54.0, 59.0, "DM 'CHECKLIST' OR TAP BIO", "#10b981", "FREE AUDIT SHEET"),
    (59.0, 64.0, "JOIN OUR NIGHTLY STRATEGY CALL", "#3b82f6", "EVERY NIGHT AT 8 PM EST"),
    (64.0, 68.8, "DM 'CHECKLIST' TO PROTECT YOUR RENT", "#10b981", "ONTARIO LANDLORD DEFENSE")
]

def render_frame(frame_idx):
    t = frame_idx / FPS
    
    if t < DUR1:
        scene_img = img_s1
        local_t = t
        scene_dur = DUR1
        zoom = 1.0 + 0.08 * (local_t / scene_dur)
        pan_y = int(60 * (local_t / scene_dur))
    elif t < DUR1 + DUR2:
        scene_img = img_s2
        local_t = t - DUR1
        scene_dur = DUR2
        zoom = 1.0 + 0.05 * (local_t / scene_dur)
        pan_y = int(120 * (local_t / scene_dur))
    else:
        scene_img = img_s3
        local_t = t - (DUR1 + DUR2)
        scene_dur = DUR3
        zoom = 1.0 + 0.04 * np.sin(local_t * 1.5)
        pan_y = int(30 * (local_t / scene_dur))

    w_z = int(WIDTH / zoom)
    h_z = int(HEIGHT / zoom)
    x1 = (WIDTH - w_z) // 2
    y1 = min((HEIGHT - h_z) // 2 + pan_y, HEIGHT - h_z)
    cropped = scene_img.crop((x1, y1, x1 + w_z, y1 + h_z))
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

print(f"Starting video render: {TOTAL_FRAMES} frames ({TOTAL_DURATION:.2f}s) @ 1080x1920 30fps...")

audio_input = 'audio/master_preset_reel_audio.wav' if os.path.exists('audio/master_preset_reel_audio.wav') else 'audio/master_user_reel_audio.wav'

ffmpeg_cmd = [
    'ffmpeg',
    '-y',
    '-f', 'rawvideo',
    '-vcodec', 'rawvideo',
    '-s', f'{WIDTH}x{HEIGHT}',
    '-pix_fmt', 'rgb24',
    '-r', str(FPS),
    '-i', '-',
    '-i', audio_input,
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

print("Video render complete!")
subprocess.run(['cp', 'output/ontario_n4_calendar_trap_reel.mp4', 'public/media/ontario_n4_calendar_trap_reel.mp4'])
print("Copied final video to public/media/ontario_n4_calendar_trap_reel.mp4")
