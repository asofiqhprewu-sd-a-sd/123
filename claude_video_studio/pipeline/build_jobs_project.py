import json
import os

FPS = 60

# Timings from timed_segments.json
# [s1] 0.00s - 2.85s (2.85s) = 171 frames
# [s2] 2.85s - 6.78s (3.93s) = 236 frames
# [s3] 6.78s - 12.77s (5.99s) = 359 frames
# [s4] 12.77s - 15.64s (2.87s) = 172 frames
# [s5] 15.64s - 19.33s (3.69s) = 221 frames
# [s6] 19.33s - 23.86s (4.53s) = 272 frames
# [s7] 23.86s - 25.87s (2.01s) = 121 frames
# Total = 1552 frames = 25.87s @ 60 FPS

scenes_meta = [
    {
        "id": "s1_intro",
        "durationInFrames": 171,
        "headline": "дерзкая сделка века",
        "text": "в 1979 году стив джобс провернул дерзкую сделку века",
        "badge": { "icon": "📍", "text": "1979 год • Кремниевая долина" },
        "glowColor": "radial-gradient(circle, rgba(56, 189, 248, 0.22) 0%, transparent 70%)",
        "sfx": "sfx/whoosh.wav"
    },
    {
        "id": "s2_xerox_deal",
        "durationInFrames": 236,
        "headline": "100 000 акций apple",
        "text": "он пришел в лабораторию ксерокс и предложил акции эппл за один визит",
        "badge": { "icon": "🤝", "text": "Секретная сделка" },
        "glowColor": "radial-gradient(circle, rgba(250, 204, 21, 0.20) 0%, transparent 70%)",
        "sfx": "sfx/pop.wav"
    },
    {
        "id": "s3_secret_discovery",
        "durationInFrames": 359,
        "headline": "окна, папки и мышь",
        "text": "ученые открыли секретную дверь и показали то от чего джобс онемел окна папки и первую в мире мышь",
        "badge": { "icon": "⚡", "text": "Секретная лаборатория PARC" },
        "glowColor": "radial-gradient(circle, rgba(56, 189, 248, 0.25) 0%, transparent 70%)",
        "sfx": "sfx/ping.wav"
    },
    {
        "id": "s4_blind_bosses",
        "durationInFrames": 172,
        "headline": "боссы были слепы",
        "text": "слепые боссы ксерокс считали это глупой игрушкой",
        "badge": { "icon": "❌", "text": "Фатальная ошибка Xerox" },
        "glowColor": "radial-gradient(circle, rgba(239, 68, 68, 0.25) 0%, transparent 70%)",
        "sfx": "sfx/drop.wav"
    },
    {
        "id": "s5_jobs_reaction",
        "durationInFrames": 221,
        "headline": "почему мы не делаем это?!",
        "text": "джобс выбежал на улицу с криком почему мы еще не делаем это",
        "badge": { "icon": "🔥", "text": "Ярость гения" },
        "glowColor": "radial-gradient(circle, rgba(250, 204, 21, 0.30) 0%, transparent 70%)",
        "sfx": "sfx/pop.wav"
    },
    {
        "id": "s6_macintosh_empire",
        "durationInFrames": 272,
        "headline": "империя на $3 триллиона",
        "text": "спустя три года эппл выпустила макинтош и построила империю на три триллиона долларов",
        "badge": { "icon": "🏆", "text": "Триумф Apple Macintosh" },
        "glowColor": "radial-gradient(circle, rgba(16, 185, 129, 0.30) 0%, transparent 70%)",
        "sfx": "sfx/cash.wav"
    },
    {
        "id": "s7_xerox_irony",
        "durationInFrames": 121,
        "headline": "бумага и принтеры",
        "text": "а ксерокс так и остался продавать бумагу",
        "badge": { "icon": "🖨️", "text": "Ирония судьбы" },
        "glowColor": "radial-gradient(circle, rgba(148, 163, 184, 0.18) 0%, transparent 70%)",
        "sfx": "sfx/click.wav"
    }
]

scenes = []
for sc in scenes_meta:
    dur_sec = sc['durationInFrames'] / FPS
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
        'durationInFrames': sc['durationInFrames'],
        'headline': sc['headline'],
        'text': sc['text'],
        'words': words,
        'badge': sc['badge'],
        'glowColor': sc['glowColor'],
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
    'bgMusicVolume': 0.12,
    'voiceAudio': 'audio/jobs_voice.wav',
    'voiceVolume': 1.0,
    'showProgressBar': True,
    'progressBarColor': '#38bdf8',
    'scenes': scenes
}

BASE_DIR = r"C:\Users\Admin\Desktop\бурмолда\claude_video_studio"
out_dir = os.path.join(BASE_DIR, 'projects', 'steve_jobs')
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, 'script.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(project_data, f, ensure_ascii=False, indent=2)

print(f"Generated Steve Jobs project: {total_frames} frames @ {FPS}fps = {total_frames/FPS:.2f} seconds")
