import math
import random
import struct
import wave
import os

SAMPLE_RATE = 44100

def write_wav(filepath, samples):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with wave.open(filepath, "w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SAMPLE_RATE)
        packed = bytearray()
        for s in samples:
            val = int(max(-32767, min(32767, s * 32767)))
            packed.extend(struct.pack("<h", val))
        f.writeframes(packed)
    print(f"Generated {filepath} ({len(samples)} samples)")

def generate_typewriter(filepath):
    # 3 seconds of realistic mechanical typewriter keystrokes followed by a ding bell
    duration = 3.5
    n_samples = int(SAMPLE_RATE * duration)
    samples = [0.0] * n_samples
    
    # Keystrokes every 0.12s - 0.22s
    key_times = [0.1, 0.28, 0.44, 0.65, 0.82, 1.05, 1.25, 1.42, 1.68, 1.88, 2.15, 2.38, 2.62]
    random.seed(42)
    for kt in key_times:
        freq = random.uniform(1400, 2400)
        for i in range(n_samples):
            t = i / SAMPLE_RATE
            dt = t - kt
            if 0 <= dt < 0.05:
                env = math.exp(-dt * 180)
                noise = random.uniform(-0.6, 0.6)
                click = math.sin(2 * math.pi * freq * dt) * env
                samples[i] += (click * 0.5 + noise * env * 0.5) * 0.7
                
    # Carriage bell at 2.85s
    bell_t = 2.85
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        dt = t - bell_t
        if 0 <= dt < 0.6:
            env = math.exp(-dt * 7)
            b1 = math.sin(2 * math.pi * 2793.8 * dt) * 0.6 # F7
            b2 = math.sin(2 * math.pi * 4186.0 * dt) * 0.3 # C8
            samples[i] += (b1 + b2) * env * 0.5
            
    write_wav(filepath, samples)

def generate_door_creak(filepath):
    duration = 1.2
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    random.seed(123)
    phase = 0
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        # Low vibrating creak frequency that wobbles
        wobble = math.sin(2 * math.pi * 8 * t) * 40
        freq = 110 + wobble + random.uniform(-10, 10)
        phase += 2 * math.pi * freq / SAMPLE_RATE
        
        # Staccato friction grain
        friction = (math.sin(phase) > 0.3)
        env = math.sin((t / duration) * math.pi) ** 1.5
        noise = random.uniform(-0.3, 0.3)
        sample = (math.sin(phase) * 0.7 + noise * 0.3) * env * (1.0 if friction else 0.2)
        samples.append(sample * 0.75)
    write_wav(filepath, samples)

def generate_bass_drop(filepath):
    duration = 1.6
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        # Deep 808 pitch drop from 160Hz down to 32Hz
        freq = 32 + 130 * math.exp(-t * 3.5)
        env = math.exp(-t * 2.2)
        # Distortion / saturation
        sub = math.sin(2 * math.pi * freq * t)
        val = math.tanh(sub * 2.2) * env
        samples.append(val * 0.9)
    write_wav(filepath, samples)

def generate_epic_soundtrack(filepath, duration=46.0):
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    # Cinematic dark progression: Dm -> Bb -> F -> C
    chords = [
        [146.83, 174.61, 220.0, 293.66], # Dm
        [116.54, 146.83, 174.61, 233.08], # Bb
        [130.81, 164.81, 196.0, 261.63], # C
        [146.83, 174.61, 220.0, 349.23], # Dm tension
    ]
    chord_len = 5.75 # 4 chords per 23s cycle
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        cycle_t = t % (chord_len * 4)
        c_idx = min(int(cycle_t / chord_len), len(chords) - 1)
        chord = chords[c_idx]
        
        # Slow cinematic breath
        lfo = 0.65 + 0.35 * math.sin(2 * math.pi * 0.25 * t)
        chord_val = sum(
            math.sin(2 * math.pi * f * t) + math.sin(2 * math.pi * f * 1.003 * t)
            for f in chord
        ) / (len(chord) * 2)
        chord_val *= lfo
        
        # Sub pulse every 2 seconds
        pulse_t = t % 2.0
        sub = math.sin(2 * math.pi * 50.0 * t) * math.exp(-pulse_t * 2.5) * 0.35
        
        # Subtle rising tension string
        string_harm = math.sin(2 * math.pi * 587.33 * t) * 0.15 * min(1.0, t / 15.0)
        
        val = (chord_val * 0.5 + sub * 0.35 + string_harm * 0.15) * 0.5
        samples.append(val)
    write_wav(filepath, samples)

if __name__ == "__main__":
    base = r"c:\Users\Admin\Desktop\бурмолда\claude_video_studio"
    sfx_dir = os.path.join(base, "public", "sfx")
    music_dir = os.path.join(base, "public", "music")
    
    generate_typewriter(os.path.join(sfx_dir, "typewriter.wav"))
    generate_door_creak(os.path.join(sfx_dir, "door_creak.wav"))
    generate_bass_drop(os.path.join(sfx_dir, "bass_drop.wav"))
    generate_epic_soundtrack(os.path.join(music_dir, "ambient_epic.wav"), duration=46.0)
    print("All scenario sound effects & music generated successfully!")
