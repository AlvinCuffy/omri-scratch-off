import os
import io
import wave
import numpy as np
from pydub import AudioSegment
from pydub.effects import normalize

os.makedirs('audio', exist_ok=True)
os.makedirs('public/media', exist_ok=True)
os.makedirs('output', exist_ok=True)

# Convert mp3s to wav
for name in ['scene1', 'scene2', 'scene3']:
    s = AudioSegment.from_file(f'audio/ai_{name}.mp3')
    s = normalize(s, headroom=1.0)
    s.export(f'audio/ai_{name}.wav', format='wav')

s1 = AudioSegment.from_wav('audio/ai_scene1.wav')
s2 = AudioSegment.from_wav('audio/ai_scene2.wav')
s3 = AudioSegment.from_wav('audio/ai_scene3.wav')

dur1 = len(s1) / 1000.0
dur2 = len(s2) / 1000.0
dur3 = len(s3) / 1000.0

gap = AudioSegment.silent(duration=350)
composite_voice = s1 + gap + s2 + gap + s3 + AudioSegment.silent(duration=800)
total_master_ms = len(composite_voice)

sr = 44100
t = np.linspace(0, total_master_ms / 1000.0, int(sr * total_master_ms / 1000.0), False)

# Lofi synth ambient bed
c3, eb3, g3, bb3 = 130.81, 155.56, 196.00, 233.08
music_signal = (
    0.15 * np.sin(2 * np.pi * c3 * t) +
    0.12 * np.sin(2 * np.pi * eb3 * t) +
    0.10 * np.sin(2 * np.pi * g3 * t) +
    0.08 * np.sin(2 * np.pi * bb3 * t)
)
pulse = 0.85 + 0.15 * np.sin(2 * np.pi * (100/60) * t)
music_signal = music_signal * pulse
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
    t_arr = np.linspace(0, dur_ms/1000.0, int(sr * dur_ms/1000.0), False)
    sig = np.sin(2 * np.pi * freq * t_arr)
    if fade:
        env = np.linspace(1, 0, len(t_arr))
        sig = sig * env
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
sfx_ding = generate_tone(880, 500) + generate_tone(1760, 500)

sfx_track = AudioSegment.silent(duration=total_master_ms)
sfx_track = sfx_track.overlay(sfx_whoosh, position=200)
stamp_time_ms = int(dur1 * 1000) - 800
sfx_track = sfx_track.overlay(sfx_stamp, position=stamp_time_ms)
sfx_track = sfx_track.overlay(sfx_whoosh, position=int(dur1*1000) + 350)
cta_time_ms = int((dur1 + dur2) * 1000) + 350
sfx_track = sfx_track.overlay(sfx_ding, position=cta_time_ms)

master_mix = bg_music.overlay(sfx_track).overlay(composite_voice)
master_mix = normalize(master_mix, headroom=0.5)

master_mix.export('audio/master_preset_reel_audio.wav', format='wav')
master_mix.export('public/media/master_reel_audio.wav', format='wav')

print(f"Exported master preset reel audio ({len(master_mix)/1000.0:.2f}s) successfully!")
