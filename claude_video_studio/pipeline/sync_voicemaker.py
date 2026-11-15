import os
import shutil
import subprocess
import json
import glob

FFPROBE = r'C:\Users\Admin\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffprobe.exe'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'projects', 'paris_history')
SCRIPT_PATH = os.path.join(PROJECT_DIR, 'script.json')
AUDIO_DIR = os.path.join(BASE_DIR, 'assets', 'audio', 'paris')
TARGET_VOICE = os.path.join(AUDIO_DIR, 'voice.mp3')
DOWNLOADS_DIR = os.path.expanduser('~\\Downloads')

def find_latest_audio():
    # Check target first
    if os.path.exists(TARGET_VOICE):
        return TARGET_VOICE
        
    # Check Downloads
    mp3s = glob.glob(os.path.join(DOWNLOADS_DIR, '*.mp3'))
    if mp3s:
        # sort by mod time
        latest = max(mp3s, key=os.path.getmtime)
        print(f"Found latest audio in Downloads: {latest}")
        shutil.copy2(latest, TARGET_VOICE)
        return TARGET_VOICE
        
    return None

def sync():
    audio_file = find_latest_audio()
    if not audio_file:
        print("No voice file found yet.")
        return False
        
    # Probe duration
    dur_str = subprocess.check_output([
        FFPROBE, '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        audio_file
    ]).decode('utf-8').strip()
    total_dur = float(dur_str)
    print(f"Total audio duration: {total_dur:.2f}s")
    
    with open(SCRIPT_PATH, 'r', encoding='utf-8') as f:
        project = json.load(f)
        
    FPS = 60
    # Proportions based on sentence lengths in short 216-char script
    # Scene 1: "Париж родился на острове Сите среди туманов Сены." (~24%)
    # Scene 2: "Римляне построили здесь Лютецию," (~16%)
    # Scene 3: "а в двенадцатом веке вырос Нотр-Дам." (~18%)
    # Scene 4: "Город пережил пожары и штурм Бастилии." (~18%)
    # Scene 5: "Сегодня Эйфелева башня и Лувр — сердце романтики всего мира!" (~24%)
    weights = [0.24, 0.16, 0.18, 0.18, 0.24]
    
    scenes = project.get('scenes', [])
    total_frames = 0
    for i, sc in enumerate(scenes):
        w = weights[i] if i < len(weights) else 0.2
        sc_dur = total_dur * w
        frames = max(90, int(sc_dur * FPS))
        sc['durationInFrames'] = frames
        sc.pop('voiceAudio', None) # clear per-scene audio
        total_frames += frames
        
    project['fps'] = FPS
    project['voiceAudio'] = 'audio/paris/voice.mp3'
    project['voiceVolume'] = 1.0
    
    with open(SCRIPT_PATH, 'w', encoding='utf-8') as f:
        json.dump(project, f, ensure_ascii=False, indent=2)
        
    print(f"Updated script.json: {total_frames} frames @ {FPS}fps = {total_frames/FPS:.2f}s")
    return True

if __name__ == '__main__':
    sync()
