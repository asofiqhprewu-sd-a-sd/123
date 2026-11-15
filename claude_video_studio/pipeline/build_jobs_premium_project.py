import json
import os

FPS = 60

# Padded Timings (0.5s pre-roll buffer, 1.2s post-roll outro buffer)
# S1: 201 frames (3.35s) - speech starts at frame 30 (0.5s)
# S2: 236 frames (3.93s)
# S3: 359 frames (5.99s)
# S4: 172 frames (2.87s)
# S5: 221 frames (3.69s)
# S6: 272 frames (4.53s)
# S7: 193 frames (3.21s) - speech ends at frame 121 (2.01s), 72 frames outro hold
# Total: 1654 frames = 27.567s

scenes_meta = [
    {
        "id": "s1_intro",
        "durationInFrames": 201,
        "headline": "дерзкая сделка века",
        "text": "в 1979 году стив джобс провернул дерзкую сделку века",
        "speech_start_sec": 0.50,
        "speech_dur_sec": 2.50,
        "hero_label": "стив джобс",
        "hero_sublabel": "1979",
        "sfx": "sfx/whoosh.wav"
    },
    {
        "id": "s2_xerox_deal",
        "durationInFrames": 236,
        "headline": "100 000 акций apple",
        "text": "он пришел в лабораторию ксерокс и предложил акции эппл за один визит",
        "speech_start_sec": 0.0,
        "speech_dur_sec": 3.58,
        "hero_label": "секретная сделка",
        "sfx": "sfx/pop.wav"
    },
    {
        "id": "s3_secret_discovery",
        "durationInFrames": 359,
        "headline": "окна, папки и мышь",
        "text": "ученые открыли секретную дверь и показали то от чего джобс онемел окна папки и первую в мире мышь",
        "speech_start_sec": 0.0,
        "speech_dur_sec": 5.64,
        "hero_label": "лаборатория xerox parc",
        "sfx": "sfx/ping.wav"
    },
    {
        "id": "s4_blind_bosses",
        "durationInFrames": 172,
        "headline": "боссы xerox были слепы",
        "text": "слепые боссы ксерокс считали это глупой игрушкой",
        "speech_start_sec": 0.0,
        "speech_dur_sec": 2.52,
        "hero_label": "фатальная ошибка",
        "sfx": "sfx/drop.wav"
    },
    {
        "id": "s5_jobs_reaction",
        "durationInFrames": 221,
        "headline": "почему мы не делаем это?!",
        "text": "джобс выбежал на улицу с криком почему мы еще не делаем это",
        "speech_start_sec": 0.0,
        "speech_dur_sec": 3.34,
        "hero_label": "ярость гения",
        "sfx": "sfx/pop.wav"
    },
    {
        "id": "s6_macintosh_empire",
        "durationInFrames": 272,
        "headline": "империя на $3 триллиона",
        "text": "спустя три года эппл выпустила макинтош и построила империю на три триллиона долларов",
        "speech_start_sec": 0.0,
        "speech_dur_sec": 4.17,
        "hero_label": "apple macintosh",
        "sfx": "sfx/cash.wav"
    },
    {
        "id": "s7_xerox_irony",
        "durationInFrames": 193,
        "headline": "а xerox остался с бумагой",
        "text": "а ксерокс так и остался продавать бумагу",
        "speech_start_sec": 0.0,
        "speech_dur_sec": 2.01,
        "hero_label": "xerox",
        "sfx": "sfx/click.wav"
    }
]

scenes = []
for sc in scenes_meta:
    dur_sec = sc['durationInFrames'] / FPS
    words = []
    raw_words = sc['text'].split()
    speech_start = sc.get('speech_start_sec', 0.0)
    speech_dur = sc.get('speech_dur_sec', dur_sec)
    step = speech_dur / max(1, len(raw_words))
    for wi, w in enumerate(raw_words):
        words.append({
            'text': w,
            'start': round(speech_start + wi * step, 2),
            'end': round(speech_start + (wi + 1) * step, 2)
        })
    scene_obj = {
        'id': sc['id'],
        'durationInFrames': sc['durationInFrames'],
        'headline': sc['headline'],
        'text': sc['text'],
        'words': words,
        'hero_label': sc.get('hero_label', ''),
        'hero_sublabel': sc.get('hero_sublabel', ''),
        'sfx': sc['sfx']
    }
    scenes.append(scene_obj)

total_frames = sum(s['durationInFrames'] for s in scenes)

project_data = {
    'title': 'Стив Джобс и Xerox: Величайшая афера в истории технологий',
    'fps': FPS,
    'width': 1080,
    'height': 1920,
    'bgMusic': 'music/ambient_tech.wav',
    'bgMusicVolume': 0.10,
    'voiceAudio': 'audio/jobs_voice.wav',
    'voiceVolume': 1.0,
    'scenes': scenes
}

BASE_DIR = r"C:\Users\Admin\Desktop\бурмолда\claude_video_studio"
out_dir = os.path.join(BASE_DIR, 'projects', 'steve_jobs')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'script.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(project_data, f, ensure_ascii=False, indent=2)

print(f"Generated Premium Steve Jobs project: {total_frames} frames @ {FPS}fps = {total_frames/FPS:.2f} seconds")
