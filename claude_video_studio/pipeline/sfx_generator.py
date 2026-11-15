"""Procedural Sound Design Generator for Claude Video Studio.
Generates royalty-free UI sound effects and ambient music.
"""

import math
import os
import random
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
    print(f"Generated {filepath} ({len(samples)} samples)")


def generate_pop(filepath):
    duration = 0.08
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        freq = 950 - 750 * (t / duration)
        env = math.exp(-t * 50)
        sample = math.sin(2 * math.pi * freq * t) * env
        samples.append(sample * 0.85)
    write_wav(filepath, samples)


def generate_whoosh(filepath):
    duration = 0.35
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    random.seed(42)
    last_noise = 0
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        progress = t / duration
        env = math.sin(progress * math.pi) ** 2
        white = random.uniform(-1, 1)
        smoothed = 0.3 * white + 0.7 * last_noise
        last_noise = smoothed
        freq = 120 + 350 * math.sin(progress * math.pi)
        sine = math.sin(2 * math.pi * freq * t)
        sample = (smoothed * 0.5 + sine * 0.5) * env
        samples.append(sample * 0.7)
    write_wav(filepath, samples)


def generate_click(filepath):
    duration = 0.02
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        freq = 2400 - 1800 * (t / duration)
        env = math.exp(-t * 180)
        sample = math.sin(2 * math.pi * freq * t) * env
        samples.append(sample * 0.7)
    write_wav(filepath, samples)


def generate_ping(filepath):
    duration = 0.45
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        env = math.exp(-t * 8)
        s1 = math.sin(2 * math.pi * 1046.5 * t) * 0.6
        s2 = math.sin(2 * math.pi * 2093.0 * t) * 0.3
        s3 = math.sin(2 * math.pi * 3135.9 * t) * 0.1
        sample = (s1 + s2 + s3) * env
        samples.append(sample * 0.75)
    write_wav(filepath, samples)


def generate_drop(filepath):
    duration = 0.25
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        freq = 140 - 90 * (t / duration)
        env = math.exp(-t * 14)
        sample = math.sin(2 * math.pi * freq * t) * env
        samples.append(sample * 0.9)
    write_wav(filepath, samples)


def generate_camera(filepath):
    duration = 0.12
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        env1 = math.exp(-abs(t - 0.02) * 150)
        env2 = math.exp(-abs(t - 0.06) * 120)
        noise = random.uniform(-0.8, 0.8)
        sample = noise * (env1 * 0.6 + env2 * 0.8)
        samples.append(sample * 0.7)
    write_wav(filepath, samples)


# NEW SOUND EFFECTS:


def generate_cash(filepath):
    """Cash register chaching / coin chime."""
    duration = 0.45
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        # Initial mechanical latch click
        latch = math.exp(-t * 120) * math.sin(2 * math.pi * 800 * t) * 0.5
        # High metallic silver coin ringing
        env = math.exp(-t * 9)
        c1 = math.sin(2 * math.pi * 2489.0 * t) * 0.5  # D#7
        c2 = math.sin(2 * math.pi * 3729.3 * t) * 0.35  # A#7
        c3 = math.sin(2 * math.pi * 4978.0 * t) * 0.15
        coins = (c1 + c2 + c3) * env
        samples.append((latch + coins) * 0.8)
    write_wav(filepath, samples)


def generate_keyboard(filepath):
    """Tactile mechanical typing burst (4 quick key clacks)."""
    duration = 0.35
    n_samples = int(SAMPLE_RATE * duration)
    samples = [0.0] * n_samples
    tap_times = [0.02, 0.08, 0.16, 0.24]
    random.seed(99)
    for tap in tap_times:
        freq = random.uniform(1200, 1800)
        for i in range(n_samples):
            t = i / SAMPLE_RATE
            dt = t - tap
            if dt >= 0 and dt < 0.04:
                env = math.exp(-dt * 200)
                noise = random.uniform(-0.4, 0.4)
                click = math.sin(2 * math.pi * freq * dt) * env * 0.6
                samples[i] += (click + noise * env) * 0.65
    write_wav(filepath, samples)


def generate_impact(filepath):
    """Deep cinematic trailer boom/impact."""
    duration = 0.85
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        # Sub-bass sweep 80Hz -> 28Hz
        freq = 80 * math.exp(-t * 2.5) + 24
        env = math.exp(-t * 4.5)
        # Low punch + soft distortion
        sub = math.sin(2 * math.pi * freq * t)
        noise = random.uniform(-0.2, 0.2) * math.exp(-t * 25)
        val = math.tanh((sub + noise) * 1.5) * env
        samples.append(val * 0.95)
    write_wav(filepath, samples)


def generate_glitch(filepath):
    """Digital glitch / stutter transition hit."""
    duration = 0.25
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        # Stutter gate at 30Hz
        gate = 1.0 if (int(t * 30) % 2 == 0) else 0.15
        freq = 400 + 800 * math.sin(t * 200)
        saw = (2 * ((t * freq) % 1.0) - 1.0)
        noise = random.uniform(-0.3, 0.3)
        env = math.sin((t / duration) * math.pi)
        samples.append((saw * 0.6 + noise * 0.4) * gate * env * 0.7)
    write_wav(filepath, samples)


def generate_heartbeat(filepath):
    """Tense biological double pulse (lub-dub)."""
    duration = 0.6
    n_samples = int(SAMPLE_RATE * duration)
    samples = [0.0] * n_samples
    pulses = [(0.05, 55.0, 0.8), (0.22, 45.0, 0.6)]
    for p_time, freq, amp in pulses:
        for i in range(n_samples):
            t = i / SAMPLE_RATE
            dt = t - p_time
            if dt >= 0 and dt < 0.15:
                env = math.sin((dt / 0.15) * math.pi) ** 2
                val = math.sin(2 * math.pi * freq * dt) * env * amp
                samples[i] += val
    write_wav(filepath, samples)


def generate_ambient_music(filepath, duration=30.0):
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    chords = [
        [220.0, 261.63, 329.63, 440.0],
        [174.61, 220.0, 261.63, 349.23],
        [196.0, 246.94, 293.66, 392.0],
        [164.81, 196.0, 246.94, 329.63],
    ]
    chord_len = duration / len(chords)
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        c_idx = min(int(t / chord_len), len(chords) - 1)
        chord = chords[c_idx]
        lfo = 0.7 + 0.3 * math.sin(2 * math.pi * 0.5 * t)
        chord_val = sum(
            math.sin(2 * math.pi * f * t) + math.sin(2 * math.pi * f * 1.002 * t)
            for f in chord
        ) / (len(chord) * 2)
        chord_val *= lfo
        pulse_t = t % 1.5
        sub = math.sin(2 * math.pi * 55.0 * t) * math.exp(-pulse_t * 3) * 0.25
        samples.append((chord_val * 0.5 + sub * 0.5) * 0.4)
    write_wav(filepath, samples)


if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sfx_dir = os.path.join(base, "assets", "sfx")
    music_dir = os.path.join(base, "assets", "music")

    generate_pop(os.path.join(sfx_dir, "pop.wav"))
    generate_whoosh(os.path.join(sfx_dir, "whoosh.wav"))
    generate_click(os.path.join(sfx_dir, "click.wav"))
    generate_ping(os.path.join(sfx_dir, "ping.wav"))
    generate_drop(os.path.join(sfx_dir, "drop.wav"))
    generate_camera(os.path.join(sfx_dir, "camera.wav"))

    # Newly added SFX
    generate_cash(os.path.join(sfx_dir, "cash.wav"))
    generate_keyboard(os.path.join(sfx_dir, "keyboard.wav"))
    generate_impact(os.path.join(sfx_dir, "impact.wav"))
    generate_glitch(os.path.join(sfx_dir, "glitch.wav"))
    generate_heartbeat(os.path.join(sfx_dir, "heartbeat.wav"))

    generate_ambient_music(os.path.join(music_dir, "ambient_tech.wav"), duration=30.0)
    print("All sound effects and music generated!")
