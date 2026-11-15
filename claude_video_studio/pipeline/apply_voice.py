import os
import subprocess
import json

FFPROBE = r'C:\Users\Admin\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffprobe.exe'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'projects', 'paris_history')
SCRIPT_PATH = os.path.join(PROJECT_DIR, 'script.json')
AUDIO_DIR = os.path.join(BASE_DIR, 'assets', 'audio', 'paris')
VOICE_PATH = os.path.join(AUDIO_DIR, 'voice.mp3')

def apply_voice():
    if not os.path.exists(VOICE_PATH):
        print(f"Waiting for audio file at: {VOICE_PATH}")
        return False

    # Probe duration
    dur_str = subprocess.check_output([
        FFPROBE, '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        VOICE_PATH
    ]).decode('utf-8').strip()
    total_dur = float(dur_str)
    print(f"Detected voice.mp3: {total_dur:.2f} seconds")

    with open(SCRIPT_PATH, 'r', encoding='utf-8') as f:
        project = json.load(f)

    fps = project.get('fps', 60)
    scenes = project.get('scenes', [])
    scene_count = len(scenes)

    # Distribute frames proportionally across the 5 scenes
    per_scene_dur = total_dur / scene_count
    total_frames = 0

    for i, sc in enumerate(scenes):
        frames = int(per_scene_dur * fps)
        sc['durationInFrames'] = frames
        sc.pop('voiceAudio', None) # remove per-scene audio in favor of global master track
        total_frames += frames

    project['voiceAudio'] = 'audio/paris/voice.mp3'
    project['voiceVolume'] = 1.0

    with open(SCRIPT_PATH, 'w', encoding='utf-8') as f:
        json.dump(project, f, ensure_ascii=False, indent=2)

    print(f"Updated script.json: {total_frames} frames @ {fps}fps ({total_frames/fps:.1f}s)")
    return True

if __name__ == '__main__':
    apply_voice()
