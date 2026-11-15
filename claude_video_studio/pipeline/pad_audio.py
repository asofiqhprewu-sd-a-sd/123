import wave
import numpy as np
import json
import os

in_wav = r'c:\Users\Admin\Desktop\бурмолда\claude_video_studio\assets\audio\jobs\jobs_voice_eugene.wav'
out_wav = r'c:\Users\Admin\Desktop\бурмолда\claude_video_studio\assets\audio\jobs\jobs_voice_padded.wav'
public_wav = r'c:\Users\Admin\Desktop\бурмолда\claude_video_studio\public\audio\jobs_voice.wav'

with wave.open(in_wav, 'rb') as f:
    params = f.getparams()
    raw = f.readframes(f.getnframes())

audio_data = np.frombuffer(raw, dtype=np.int16)
rate = params.framerate

# 0.5s silence at start, 1.2s silence at end
START_PAD = 0.5
END_PAD = 1.2
pad_start = np.zeros(int(rate * START_PAD), dtype=np.int16)
pad_end = np.zeros(int(rate * END_PAD), dtype=np.int16)

padded = np.concatenate([pad_start, audio_data, pad_end])

for p in [out_wav, public_wav]:
    with wave.open(p, 'wb') as f:
        f.setparams(params)
        f.writeframes(padded.tobytes())

total_duration = len(padded) / rate
print(f"Padded audio successfully saved! Total duration: {total_duration:.3f}s")
