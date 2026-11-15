import math
import os
import struct
import wave

SAMPLE_RATE = 44100

def write_wav(filepath, samples, channels=1):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with wave.open(filepath, "w") as f:
        f.setnchannels(channels)
        f.setsampwidth(2)
        f.setframerate(SAMPLE_RATE)
        packed = bytearray()
        for s in samples:
            val = int(max(-32767, min(32767, s * 32767)))
            packed.extend(struct.pack("<h", val))
        f.writeframes(packed)
    print(f"Generated {filepath} ({len(samples)} samples = {len(samples)/SAMPLE_RATE:.1f}s)")

def generate_casino_thriller(filepath, duration=66.0):
    """Deep tense cinematic soundtrack: ticking rhythm, sub-bass pulse, dark ambient synth pad."""
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    
    # Dark suspense chord progressions in D minor:
    # Dm -> Bb -> Gm -> A
    chord_progressions = [
        [146.83, 220.0, 261.63, 349.23], # Dm
        [116.54, 174.61, 233.08, 293.66], # Bb
        [98.00, 146.83, 196.00, 246.94],  # Gm
        [110.00, 164.81, 220.00, 277.18], # A
    ]
    chord_len = 8.0 # 8 seconds per chord cycle
    
    bpm = 110.0
    beat_interval = 60.0 / bpm
    
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        
        # 1. Dark evolving synth pad
        c_idx = int((t / chord_len)) % len(chord_progressions)
        chord = chord_progressions[c_idx]
        pad = sum(
            math.sin(2 * math.pi * f * t) * 0.5 + 
            math.sin(2 * math.pi * (f * 1.003) * t) * 0.5
            for f in chord
        ) / len(chord)
        # Slow filter sweep LFO
        lfo = 0.5 + 0.5 * math.sin(2 * math.pi * 0.15 * t)
        pad *= (0.4 + 0.6 * lfo)
        
        # 2. Deep Sub-bass 808 pulse on quarter beats
        sub_beat = t % beat_interval
        sub_env = math.exp(-sub_beat * 6.0)
        sub_freq = chord[0] * 0.5 # root bass
        sub = math.sin(2 * math.pi * sub_freq * sub_beat) * sub_env * 0.45
        
        # 3. Subtle clockwork tension tick (clock ticker)
        tick_beat = (t * 2) % beat_interval
        tick_env = math.exp(-tick_beat * 40.0)
        tick = math.sin(2 * math.pi * 1800.0 * tick_beat) * tick_env * 0.08
        
        # 4. Master Mix with gentle fade-in and fade-out
        master_env = 1.0
        if t < 1.5:
            master_env = t / 1.5
        elif t > duration - 2.5:
            master_env = (duration - t) / 2.5
            
        sample = (pad * 0.45 + sub * 0.4 + tick * 0.15) * master_env * 0.65
        samples.append(sample)
        
    write_wav(filepath, samples)

if __name__ == '__main__':
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(base, 'assets', 'music', 'casino_thriller.wav')
    generate_casino_thriller(out, 66.0)
