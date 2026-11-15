import subprocess
import json
import os

scenes_data = [
    {
        'id': 's1_hook',
        'theme': 'dark',
        'text': 'как появился париж',
        'voice_text': 'Как появился самый красивый город на Земле?',
        'photo': {
            'src': 'photos/paris/seine_island.jpg',
            'tag': 'Остров Сите • Река Сена',
            'glowColor': 'rgba(245, 158, 11, 0.4)'
        },
        'sfx': 'sfx/whoosh.wav',
        'pills': [
            {'text': 'остров сите', 'color': '#1f2937'},
            {'text': 'река сена', 'color': '#0284c7'}
        ]
    },
    {
        'id': 's2_origins',
        'theme': 'blue',
        'text': 'две тысячи лет назад',
        'voice_text': 'Более двух тысяч лет назад кельтское племя паризиев основало здесь поселение Лютеция.',
        'photo': {
            'src': 'photos/paris/paris_street.jpg',
            'tag': 'Древняя Лютеция • III век до н.э.',
            'glowColor': 'rgba(56, 189, 248, 0.35)'
        },
        'sfx': 'sfx/camera.wav',
        'pills': [
            {'text': 'племя паризиев', 'color': '#1e3a8a'},
            {'text': 'лютеция', 'color': '#0369a1'}
        ]
    },
    {
        'id': 's3_notre_dame',
        'theme': 'dark',
        'text': 'нотр дам де пари',
        'voice_text': 'В двенадцатом веке началось грандиозное строительство Нотр-Дама, продлившееся почти два века.',
        'photo': {
            'src': 'photos/paris/notre_dame.jpg',
            'tag': 'Нотр-Дам де Пари • 1163 год',
            'glowColor': 'rgba(239, 68, 68, 0.35)'
        },
        'sfx': 'sfx/impact.wav',
        'pills': [
            {'text': '1163 год', 'color': '#b91c1c'},
            {'text': 'готика', 'color': '#1f2937'},
            {'text': '182 года стройки', 'color': '#1f2937'}
        ]
    },
    {
        'id': 's4_louvre',
        'theme': 'dark',
        'text': 'от крепости до музея',
        'voice_text': 'А знаменитый Лувр сначала был неприступной военной крепостью королей, и лишь потом стал главным музеем мира.',
        'photo': {
            'src': 'photos/paris/louvre.jpg',
            'tag': 'Лувр • Пирамида и дворец',
            'glowColor': 'rgba(168, 85, 247, 0.35)'
        },
        'sfx': 'sfx/camera.wav',
        'pills': [
            {'text': 'крепость 1190', 'color': '#581c87'},
            {'text': 'музей 1793', 'color': '#1f2937'},
            {'text': '35 000 шедевров', 'color': '#7e22ce'}
        ]
    },
    {
        'id': 's5_eiffel_drama',
        'theme': 'red',
        'text': 'башня которую ненавидели',
        'voice_text': 'Когда Гюстав Эйфель строил свою башню, триста писателей требовали немедленно снести это чудовище.',
        'photoComparison': {
            'leftPhoto': 'photos/paris/eiffel_construction.jpg',
            'rightPhoto': 'photos/paris/gustave_eiffel.jpg',
            'leftLabel': 'Стройка 1888',
            'rightLabel': 'Гюстав Эйфель',
            'tag': 'Протест художников'
        },
        'sfx': 'sfx/drop.wav',
        'pills': [
            {'text': 'протест 1887', 'color': '#991b1b'},
            {'text': '300 писателей', 'color': '#b91c1c'},
            {'text': 'временный проект', 'color': '#1f2937'}
        ]
    },
    {
        'id': 's6_eiffel_glory',
        'theme': 'dark',
        'text': 'главный символ мира',
        'voice_text': 'Но сегодня Эйфелева башня — сердце Парижа и самый романтичный символ мира.',
        'photo': {
            'src': 'photos/paris/eiffel_tower.jpg',
            'tag': 'Эйфелева башня • 330 метров',
            'glowColor': 'rgba(234, 179, 8, 0.4)'
        },
        'sfx': 'sfx/impact.wav',
        'pills': [
            {'text': '330 метров', 'color': '#ca8a04'},
            {'text': '300 млн гостей', 'color': '#1f2937'},
            {'text': 'город света', 'color': '#2563eb'}
        ]
    },
    {
        'id': 's7_finale',
        'theme': 'blue',
        'text': 'город который живет вечно',
        'voice_text': 'Сохрани это видео, чтобы не забыть, когда полетишь в Париж!',
        'photo': {
            'src': 'photos/paris/arc_de_triomphe.jpg',
            'tag': 'Триумфальная арка • Париж',
            'glowColor': 'rgba(56, 189, 248, 0.4)'
        },
        'sfx': 'sfx/ping.wav',
        'pills': [
            {'text': 'сохраняй', 'color': '#0284c7'},
            {'text': 'город огней', 'color': '#1e3a8a'}
        ]
    }
]

FPS = 60
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
audio_dir = os.path.join(BASE_DIR, 'assets', 'audio', 'paris')
os.makedirs(audio_dir, exist_ok=True)

processed_scenes = []

for i, sc in enumerate(scenes_data):
    audio_filename = f'voice_{i+1}.mp3'
    vtt_filename = f'voice_{i+1}.vtt'
    audio_full = os.path.join(audio_dir, audio_filename)
    vtt_full = os.path.join(audio_dir, vtt_filename)
    
    print(f"Synthesizing scene {i+1}: {sc['voice_text']}")
    cmd = [
        r'C:\Users\Admin\AppData\Local\Python\pythoncore-3.14-64\python.exe',
        '-m', 'edge_tts',
        '--voice', 'ru-RU-DmitryNeural',
        '--rate', '+12%',
        '--text', sc['voice_text'],
        '--write-media', audio_full,
        '--write-subtitles', vtt_full
    ]
    subprocess.run(cmd, check=True)
    
    # Probe duration
    ffprobe_cmd = [
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        audio_full
    ]
    dur_str = subprocess.check_output(ffprobe_cmd).decode('utf-8').strip()
    dur_sec = float(dur_str)
    
    # Calculate duration in 60 FPS frames (audio duration + 0.35s padding for visual rhythm)
    frames = int((dur_sec + 0.35) * FPS)
    print(f"Scene {i+1} audio: {dur_sec:.2f}s -> {frames} frames @ {FPS}fps")
    
    # Simple word breakdown for kinetic captioning
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
        'pills': sc['pills']
    }
    if 'photo' in sc:
        scene_obj['photo'] = sc['photo']
    if 'photoComparison' in sc:
        scene_obj['photoComparison'] = sc['photoComparison']
        
    processed_scenes.append(scene_obj)

final_project = {
    'title': 'История Парижа (Реальные Кадры, 60 FPS)',
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

print('SUCCESS: build_paris_real.py finished, script.json updated!')
