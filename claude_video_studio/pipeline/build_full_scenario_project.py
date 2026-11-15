import json
import os

FPS = 60

# Exact beat durations from scenario_timed_scenes.json
# B1: 0.00s - 10.86s = 652 frames (speech: 0.60s - 10.36s)
# B2: 10.86s - 18.56s = 462 frames (speech: 10.86s - 18.06s)
# B3: 18.56s - 28.16s = 576 frames (speech: 18.56s - 27.66s)
# B4: 28.16s - 32.66s = 270 frames (speech: 28.16s - 32.16s)
# B5: 32.66s - 39.73s = 424 frames (speech: 32.66s - 39.23s)
# B6: 39.73s - 44.34s = 276 frames (speech: 39.73s - 42.83s, plus 1.5s outro hold)

scenes_meta = [
    {
        "id": "beat_1_hook",
        "durationInFrames": 652,
        "headline": "самый дорогой секрет xx века",
        "text": "в тысяча девятьсот семьдесят девятом году один человек вошёл в здание ксерокс через час он вышел оттуда с самым дорогим секретом двадцатого века и заплатил за него акциями своей компании",
        "speech_start_rel": 0.60,
        "speech_dur": 9.76,
        "sfx": "sfx/typewriter.wav",
        "sfxVolume": 0.35,
    },
    {
        "id": "beat_2_deal",
        "durationInFrames": 462,
        "headline": "сделка века",
        "text": "эппл предложила ксерокс свои акции всего за один визит в секретную лабораторию это была самая дерзкая сделка в истории технологий",
        "speech_start_rel": 0.0,
        "speech_dur": 7.20,
        "sfx": "sfx/pop.wav",
        "sfxVolume": 0.15,
    },
    {
        "id": "beat_3_robbery",
        "durationInFrames": 576,
        "headline": "окна, папки и первая мышь",
        "text": "учёные открыли секретную дверь и показали ему окна папки и первую в мире компьютерную мышь джобс онемел а слепые боссы ксерокс назвали это просто глупой игрушкой",
        "speech_start_rel": 0.0,
        "speech_dur": 9.10,
        "sfx": "sfx/door_creak.wav",
        "sfxVolume": 0.25,
    },
    {
        "id": "beat_4_climax",
        "durationInFrames": 270,
        "headline": "«почему мы ещё не делаем это?!»",
        "text": "джобс выбежал на улицу и закричал своим инженерам почему мы ещё не делаем это",
        "speech_start_rel": 0.0,
        "speech_dur": 4.00,
        "sfx": "sfx/bass_drop.wav",
        "sfxVolume": 0.40,
    },
    {
        "id": "beat_5_empire_vs_paper",
        "durationInFrames": 424,
        "headline": "$3 000 000 000 000 vs бумага",
        "text": "спустя три года эппл выпустила макинтош и построила империю на три триллиона долларов а ксерокс так и остался продавать обычную бумагу",
        "speech_start_rel": 0.0,
        "speech_dur": 6.58,
        "sfx": "sfx/cash.wav",
        "sfxVolume": 0.25,
    },
    {
        "id": "beat_6_punchline",
        "durationInFrames": 276,
        "headline": "финал",
        "text": "иногда самое дорогое это то что вы считаете просто игрушкой",
        "speech_start_rel": 0.0,
        "speech_dur": 3.10,
        "sfx": "sfx/ping.wav",
        "sfxVolume": 0.15,
    }
]

scenes = []
for sc in scenes_meta:
    dur_sec = sc['durationInFrames'] / FPS
    words = []
    raw_words = sc['text'].split()
    speech_start = sc.get('speech_start_rel', 0.0)
    speech_dur = sc.get('speech_dur', dur_sec)
    step = speech_dur / max(1, len(raw_words))
    for wi, w in enumerate(raw_words):
        words.append({
            'text': w,
            'start': round(speech_start + wi * step, 2),
            'end': round(speech_start + (wi + 1) * step, 2)
        })
    scenes.append({
        'id': sc['id'],
        'durationInFrames': sc['durationInFrames'],
        'headline': sc['headline'],
        'text': sc['text'],
        'words': words,
        'sfx': sc['sfx'],
        'sfxVolume': sc.get('sfxVolume', 0.2)
    })

total_frames = sum(s['durationInFrames'] for s in scenes)

project_data = {
    'title': 'Стив Джобс и Xerox: Величайшая афера века',
    'fps': FPS,
    'width': 1080,
    'height': 1920,
    'bgMusic': 'music/ambient_epic.wav',
    'bgMusicVolume': 0.12,
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

print(f"Generated scenario project: {total_frames} frames @ {FPS}fps = {total_frames/FPS:.2f} seconds")
