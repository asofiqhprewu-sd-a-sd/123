import os
import subprocess
import json
import time
from gtts import gTTS

FFPROBE = r'C:\Users\Admin\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffprobe.exe'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
audio_dir = os.path.join(BASE_DIR, 'assets', 'audio', 'paris')
os.makedirs(audio_dir, exist_ok=True)

scenes_data = [
    {
        'id': 's1_flag_birth',
        'theme': 'dark',
        'text': 'рождение парижа',
        'voice': 'История Парижа началась более двух тысяч лет назад на острове Сите, где галльское племя паризиев построило первые хижины среди туманных лесов Сены.',
        'photo': {
            'src': 'photos/paris/scene1.jpg',
            'tag': 'Остров Сите • Племя паризиев',
            'glowColor': 'rgba(56, 189, 248, 0.35)',
            'zoomDirection': 'in'
        },
        'sfx': 'sfx/whoosh.wav',
        'pills': [
            {'text': 'остров сите', 'color': '#1f2937'},
            {'text': 'река сена', 'color': '#0284c7'},
            {'text': 'племя паризиев', 'color': '#1e3a8a'}
        ]
    },
    {
        'id': 's2_roman_lutetia',
        'theme': 'blue',
        'text': 'римская лютеция',
        'voice': 'Затем пришли римские легионы. Они возвели каменный античный город Лютеция с акведуками, форумом и величественными храмами.',
        'photo': {
            'src': 'photos/paris/scene2.jpg',
            'tag': 'Античная Лютеция • Римская империя',
            'glowColor': 'rgba(234, 179, 8, 0.35)',
            'zoomDirection': 'out'
        },
        'sfx': 'sfx/impact.wav',
        'pills': [
            {'text': 'римские легионы', 'color': '#991b1b'},
            {'text': 'лютеция', 'color': '#0369a1'},
            {'text': 'каменные акведуки', 'color': '#1f2937'}
        ]
    },
    {
        'id': 's3_medieval_notredame',
        'theme': 'dark',
        'text': 'нотр дам де пари',
        'voice': 'В двенадцатом веке началось грандиозное возведение Нотр-Дам де Пари — готического шедевра, который строился почти два столетия.',
        'photo': {
            'src': 'photos/paris/scene3.jpg',
            'tag': 'Нотр-Дам де Пари • 1163 год',
            'glowColor': 'rgba(239, 68, 68, 0.35)',
            'zoomDirection': 'in'
        },
        'sfx': 'sfx/camera.wav',
        'pills': [
            {'text': '1163 год', 'color': '#b91c1c'},
            {'text': 'готика', 'color': '#1f2937'},
            {'text': '182 года стройки', 'color': '#1f2937'}
        ]
    },
    {
        'id': 's4_revolution_bastille',
        'theme': 'red',
        'text': 'штурм бастилии',
        'voice': 'Пройдя сквозь Столетнюю войну и огонь штурма Бастилии, Париж стал эпицентром революции, изменившей ход мировой истории.',
        'photo': {
            'src': 'photos/paris/scene4.jpg',
            'tag': 'Штурм Бастилии • 14 июля 1789',
            'glowColor': 'rgba(239, 68, 68, 0.5)',
            'zoomDirection': 'in'
        },
        'sfx': 'sfx/impact.wav',
        'pills': [
            {'text': '1789 год', 'color': '#991b1b'},
            {'text': 'штурм бастилии', 'color': '#b91c1c'},
            {'text': 'свобода', 'color': '#2563eb'}
        ]
    },
    {
        'id': 's5_modern_cityscape',
        'theme': 'dark',
        'text': 'город света',
        'voice': 'Сегодня Париж — мировая столица красоты и романтики. Эйфелева башня, Лувр и Триумфальная арка сияют для миллионов сердец.',
        'photo': {
            'src': 'photos/paris/scene5.jpg',
            'tag': 'Париж • Главный символ мира',
            'glowColor': 'rgba(234, 179, 8, 0.45)',
            'zoomDirection': 'out'
        },
        'sfx': 'sfx/ping.wav',
        'pills': [
            {'text': 'эйфелева башня', 'color': '#ca8a04'},
            {'text': 'лувр', 'color': '#1f2937'},
            {'text': 'город света', 'color': '#2563eb'}
        ]
    }
]

FPS = 60
tlds = ['co.uk', 'ca', 'fr', 'de', 'is', 'com']

def save_voice_with_retry(text, out_path):
    for tld in tlds:
        try:
            print(f"Trying tld={tld} for '{text[:30]}...'")
            tts = gTTS(text, lang='ru', tld=tld)
            tts.save(out_path)
            if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
                print(f"Success with tld={tld} ({os.path.getsize(out_path)} bytes)")
                return True
        except Exception as e:
            print(f"tld={tld} failed: {e}")
            time.sleep(0.5)
    raise RuntimeError(f"Failed to generate voice for: {text}")

processed_scenes = []

for i, sc in enumerate(scenes_data):
    audio_filename = f'scene_{i+1}.mp3'
    audio_full = os.path.join(audio_dir, audio_filename)
    
    save_voice_with_retry(sc['voice'], audio_full)
    
    probe = subprocess.check_output([
        FFPROBE, '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        audio_full
    ]).decode('utf-8').strip()
    dur_sec = float(probe)
    
    # 60 FPS: add 0.4s breathing room
    frames = int((dur_sec + 0.4) * FPS)
    print(f"Scene {i+1}: {dur_sec:.2f}s -> {frames} frames @ {FPS}fps")
    
    # Word timestamps for kinetic text
    words = []
    raw_words = sc['text'].split()
    step = dur_sec / max(1, len(raw_words))
    for wi, w in enumerate(raw_words):
        words.append({
            'text': w,
            'start': round(wi * step, 2),
            'end': round((wi + 1) * step, 2)
        })
        
    scene_obj = {
        'id': sc['id'],
        'durationInFrames': frames,
        'theme': sc['theme'],
        'text': sc['text'],
        'words': words,
        'voiceAudio': f'audio/paris/{audio_filename}',
        'voiceVolume': 1.0,
        'sfx': sc['sfx'],
        'photo': sc['photo'],
        'pills': sc['pills']
    }
    processed_scenes.append(scene_obj)

final_project = {
    'title': 'История Парижа (60 FPS, Реальные Кадры, Озвучка)',
    'fps': FPS,
    'width': 1080,
    'height': 1920,
    'bgMusic': 'music/ambient_tech.wav',
    'bgMusicVolume': 0.12,
    'scenes': processed_scenes
}

out_script = os.path.join(BASE_DIR, 'projects', 'paris_history', 'script.json')
with open(out_script, 'w', encoding='utf-8') as f:
    json.dump(final_project, f, ensure_ascii=False, indent=2)

total_frames = sum(s['durationInFrames'] for s in processed_scenes)
print(f"DONE! Total frames: {total_frames} @ 60fps ({total_frames/FPS:.1f} seconds)")
