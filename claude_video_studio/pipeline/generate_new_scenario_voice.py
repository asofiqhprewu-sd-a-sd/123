import torch
import wave
import os
import json
import numpy as np

# Load local Silero TTS model
model_path = r"C:\Users\Admin\AppData\Local\Temp\silero_model.pt"
device = torch.device('cpu')
imp = torch.package.PackageImporter(model_path)
model = imp.load_pickle("tts_models", "model")
model.to(device)

sample_rate = 48000

# Full phonetically spelled-out script to PREVENT ANY SWALLOWING:
# All numbers in words, English names phonetically transliterated
scenario_beats = [
    {
        "id": "beat_1_hook",
        "title": "самый дорогой секрет",
        # 0:00 - 0:08
        "text": "В тысяча девятьсот семьдесят девятом году один человек вошёл в здание Ксерокс.",
        "text_sub": "Через час он вышел оттуда с самым дорогим секретом двадцатого века. И заплатил за него… акциями своей компании."
    },
    {
        "id": "beat_2_deal",
        "title": "сделка века",
        # Завязка
        "text": "Эппл предложила Ксерокс свои акции всего за один визит в секретную лабораторию.",
        "text_sub": "Это была самая дерзкая сделка в истории технологий."
    },
    {
        "id": "beat_3_robbery",
        "title": "окна, папки и мышь",
        # Ограбление / встреча с мышью
        "text": "Учёные открыли секретную дверь и показали ему окна, папки и первую в мире компьютерную мышь.",
        "text_sub": "Джобс онемел. А слепые боссы Ксерокс назвали это просто глупой игрушкой."
    },
    {
        "id": "beat_4_climax",
        "title": "момент озарения",
        # Кульминация / крик
        "text": "Джобс выбежал на улицу и закричал своим инженерам:",
        "text_sub": "«Почему мы ещё не делаем это?!»"
    },
    {
        "id": "beat_5_empire_vs_paper",
        "title": "империя vs бумага",
        # Развязка (сплит-скрин)
        "text": "Спустя три года Эппл выпустила Макинтош и построила империю на три триллиона долларов.",
        "text_sub": "А Ксерокс так и остался продавать обычную бумагу."
    },
    {
        "id": "beat_6_punchline",
        "title": "финал",
        # Финал-панчлайн
        "text": "Иногда самое дорогое — это то, что вы считаете просто игрушкой.",
        "text_sub": ""
    }
]

out_dir = r"C:\Users\Admin\Desktop\бурмолда\claude_video_studio\assets\audio\jobs"
os.makedirs(out_dir, exist_ok=True)

# 0.6s silence buffer at start
START_PAD = 0.6
all_audio = [0] * int(sample_rate * START_PAD)
timed_scenes = []
current_time = START_PAD

PAUSE_BETWEEN_BEATS = 0.50 # 500ms dramatic pause

for b_idx, beat in enumerate(scenario_beats):
    full_text = f"{beat['text']} {beat['text_sub']}".strip()
    
    # Generate speech
    audio = model.apply_tts(text=full_text, speaker='eugene', sample_rate=sample_rate)
    samples = (audio.numpy() * 32767).astype('int16').tolist()
    
    dur_sec = len(samples) / sample_rate
    start_t = round(current_time, 2)
    end_t = round(current_time + dur_sec, 2)
    
    timed_scenes.append({
        "id": beat["id"],
        "title": beat["title"],
        "text": full_text,
        "start": start_t,
        "end": end_t,
        "duration": round(dur_sec, 2),
    })
    
    all_audio.extend(samples)
    if b_idx < len(scenario_beats) - 1:
        pause_samples = [0] * int(sample_rate * PAUSE_BETWEEN_BEATS)
        all_audio.extend(pause_samples)
        current_time = end_t + PAUSE_BETWEEN_BEATS
    else:
        current_time = end_t

# 1.5s outro hold buffer
END_PAD = 1.5
all_audio.extend([0] * int(sample_rate * END_PAD))
total_duration = len(all_audio) / sample_rate

master_np = np.array(all_audio, dtype=np.int16)

master_wav = os.path.join(out_dir, "jobs_voice_full.wav")
public_wav = r"C:\Users\Admin\Desktop\бурмолда\claude_video_studio\public\audio\jobs_voice.wav"

for p in [master_wav, public_wav]:
    with wave.open(p, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(master_np.tobytes())

print(f"Master voice generated! Total duration: {total_duration:.2f}s ({len(master_np)} samples)")
for s in timed_scenes:
    print(f"  [{s['id']}] {s['start']:5.2f}s - {s['end']:5.2f}s ({s['duration']:4.2f}s): {s['text'][:50]}...")

with open(os.path.join(out_dir, "scenario_timed_scenes.json"), 'w', encoding='utf-8') as f:
    json.dump(timed_scenes, f, ensure_ascii=False, indent=2)
