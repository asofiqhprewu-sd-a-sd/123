import json
import os

FPS = 60

# 14 slides with gentle notification sound effects and exact speech timings
slides_data = [
    {
        "id": "slide01_vegas_intro",
        "durationInFrames": 288,
        "photo": "photos/thorp/slides/slide01.jpg",
        "text": "в 1960 году владельцы казино лас-вегаса считали себя богами",
        "badge": {
            "icon": "📍",
            "label": "Лас-Вегас • 1960 год",
            "sub": "Золотая эра казино"
        },
        "sfx": "sfx/whoosh.wav",
        "sfxVolume": 0.12
    },
    {
        "id": "slide02_mafia_rule",
        "durationInFrames": 252,
        "photo": "photos/thorp/slides/slide02.jpg",
        "text": "математика была на их стороне а за порядком следила вооружённая мафия",
        "badge": {
            "icon": "⚠️",
            "label": "Мафия Лас-Вегаса",
            "sub": "Железный контроль"
        },
        "widget": {
            "icon": "🕶️",
            "title": "Контроль игорного бизнеса",
            "value": "Вооружённая мафия и криминал",
            "glowColor": "rgba(239, 68, 68, 0.4)",
            "borderColor": "rgba(239, 68, 68, 0.6)",
            "valueColor": "#f87171"
        },
        "sfx": "sfx/pop.wav",
        "sfxVolume": 0.12
    },
    {
        "id": "slide03_casino_vault",
        "durationInFrames": 150,
        "photo": "photos/thorp/slides/slide03.jpg",
        "text": "никто не мог уйти с их деньгами",
        "badge": {
            "icon": "🔒",
            "label": "Сейфы казино",
            "sub": "Нулевые шансы"
        },
        "sfx": "sfx/click.wav",
        "sfxVolume": 0.10
    },
    {
        "id": "slide04_professor_thorp",
        "durationInFrames": 300,
        "photo": "photos/thorp/slides/slide04.jpg",
        "text": "пока за игорный стол не сел скромный профессор математики эдвард торп",
        "badge": {
            "icon": "🎓",
            "label": "Эдвард Торп",
            "sub": "Профессор MIT"
        },
        "widget": {
            "icon": "🧠",
            "title": "Гений теории вероятностей",
            "value": "Доктор математики UCLA & MIT",
            "glowColor": "rgba(56, 189, 248, 0.4)",
            "borderColor": "rgba(56, 189, 248, 0.6)",
            "valueColor": "#38bdf8"
        },
        "sfx": "sfx/pop.wav",
        "sfxVolume": 0.12
    },
    {
        "id": "slide05_no_luck_pure_math",
        "durationInFrames": 114,
        "photo": "photos/thorp/slides/slide05.jpg",
        "text": "торп не верил в удачу",
        "badge": {
            "icon": "📐",
            "label": "Чистый расчёт",
            "sub": "Формула вероятности"
        },
        "sfx": "sfx/ping.wav",
        "sfxVolume": 0.10
    },
    {
        "id": "slide06_ibm704_mit",
        "durationInFrames": 402,
        "photo": "photos/thorp/slides/slide06.jpg",
        "text": "на суперкомпьютере mit он просчитал миллионы комбинаций и создал подсчёт карт",
        "badge": {
            "icon": "💻",
            "label": "Лаборатория MIT • 1960",
            "sub": "Суперкомпьютер IBM 704"
        },
        "widget": {
            "icon": "⚙️",
            "title": "Суперкомпьютер IBM 704",
            "value": "Миллионы комбинаций блэкджека",
            "glowColor": "rgba(56, 189, 248, 0.4)",
            "borderColor": "rgba(56, 189, 248, 0.6)",
            "valueColor": "#7dd3fc"
        },
        "sfx": "sfx/pop.wav",
        "sfxVolume": 0.12
    },
    {
        "id": "slide07_arrival_nevada",
        "durationInFrames": 204,
        "photo": "photos/thorp/slides/slide07.jpg",
        "text": "когда профессор приехал в неваду казино замерли",
        "badge": {
            "icon": "🎲",
            "label": "Прибытие в Неваду",
            "sub": "Начало операции"
        },
        "sfx": "sfx/whoosh.wav",
        "sfxVolume": 0.10
    },
    {
        "id": "slide08_blackjack_jackpot",
        "durationInFrames": 192,
        "photo": "photos/thorp/slides/slide08.jpg",
        "text": "за одну ночь он выносил десятки тысяч долларов",
        "badge": {
            "icon": "💵",
            "label": "Разгром казино",
            "sub": "Триумф математики"
        },
        "widget": {
            "icon": "💰",
            "title": "Выигрыш за 1 ночь",
            "value": "+$20,000 чистыми наличными",
            "glowColor": "rgba(34, 197, 94, 0.4)",
            "borderColor": "rgba(34, 197, 94, 0.6)",
            "valueColor": "#4ade80"
        },
        "sfx": "sfx/cash.wav",
        "sfxVolume": 0.12
    },
    {
        "id": "slide09_dealers_panic",
        "durationInFrames": 366,
        "photo": "photos/thorp/slides/slide09.jpg",
        "text": "дилеры потели охрана не понимала в чём дело он считал быстрее человека",
        "badge": {
            "icon": "👀",
            "label": "Паника дилеров",
            "sub": "Охрана в шоке"
        },
        "widget": {
            "icon": "⚡",
            "title": "Скорость ума профессора",
            "value": "Счёт карт быстрее дилера",
            "glowColor": "rgba(245, 158, 11, 0.4)",
            "borderColor": "rgba(245, 158, 11, 0.6)",
            "valueColor": "#facc15"
        },
        "sfx": "sfx/pop.wav",
        "sfxVolume": 0.12
    },
    {
        "id": "slide10_mob_hunt",
        "durationInFrames": 180,
        "photo": "photos/thorp/slides/slide10.jpg",
        "text": "владельцы казино объявили на торпа охоту",
        "badge": {
            "icon": "🚨",
            "label": "Охота мафии",
            "sub": "Чрезвычайные меры"
        },
        "sfx": "sfx/pop.wav",
        "sfxVolume": 0.12
    },
    {
        "id": "slide11_poison_ambush",
        "durationInFrames": 354,
        "photo": "photos/thorp/slides/slide11.jpg",
        "text": "ему подсыпали яд в кофе блокировали колёса и переломали пальцы напарнику",
        "badge": {
            "icon": "⚠️",
            "label": "Покушения мафии",
            "sub": "Угроза жизни"
        },
        "widget": {
            "icon": "☠️",
            "title": "Попытки устранить Торпа",
            "value": "Яд в кофе • Саботаж авто",
            "glowColor": "rgba(239, 68, 68, 0.45)",
            "borderColor": "rgba(239, 68, 68, 0.65)",
            "valueColor": "#f87171"
        },
        "sfx": "sfx/click.wav",
        "sfxVolume": 0.10
    },
    {
        "id": "slide12_rules_changed",
        "durationInFrames": 402,
        "photo": "photos/thorp/slides/slide12.jpg",
        "text": "казино изменили правила игры по всей америке но торп пошёл дальше",
        "badge": {
            "icon": "📜",
            "label": "Изменение правил США",
            "sub": "Новый уровень"
        },
        "widget": {
            "icon": "🏛️",
            "title": "Реакция казино",
            "value": "Переписаны правила блэкджека в США",
            "glowColor": "rgba(245, 158, 11, 0.4)",
            "borderColor": "rgba(245, 158, 11, 0.6)",
            "valueColor": "#fbbf24"
        },
        "sfx": "sfx/whoosh.wav",
        "sfxVolume": 0.10
    },
    {
        "id": "slide13_shannon_wearable",
        "durationInFrames": 312,
        "photo": "photos/thorp/slides/slide13.jpg",
        "text": "вместе с гением клодом шенноном он создал первый в истории носимый микрокомпьютер",
        "badge": {
            "icon": "⚡",
            "label": "Шеннон & Торп • 1961",
            "sub": "Секретная лаборатория"
        },
        "widget": {
            "icon": "👟",
            "title": "Первый в мире носимый ПК",
            "value": "12 транзисторов • Передатчик в обуви",
            "glowColor": "rgba(16, 185, 129, 0.45)",
            "borderColor": "rgba(16, 185, 129, 0.65)",
            "valueColor": "#34d399"
        },
        "sfx": "sfx/pop.wav",
        "sfxVolume": 0.12
    },
    {
        "id": "slide14_shoe_computer_climax",
        "durationInFrames": 297,
        "photo": "photos/thorp/slides/slide14.jpg",
        "text": "устройство размером с сигаретную пачку спрятали прямо в каблук ботинка",
        "badge": {
            "icon": "🎯",
            "label": "Секретное оружие",
            "sub": "Имба математики"
        },
        "widget": {
            "icon": "👞",
            "title": "Компьютер в подошве",
            "value": "Микрокликер в пальце ноги",
            "glowColor": "rgba(245, 158, 11, 0.5)",
            "borderColor": "rgba(245, 158, 11, 0.7)",
            "valueColor": "#facc15"
        },
        "sfx": "sfx/ping.wav",
        "sfxVolume": 0.12
    }
]

scenes = []
for sc in slides_data:
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
        'photo': sc['photo'],
        'text': sc['text'],
        'words': words,
        'badge': sc['badge'],
        'sfx': sc['sfx'],
        'sfxVolume': sc.get('sfxVolume', 0.12)
    }
    if 'widget' in sc:
        scene_obj['widget'] = sc['widget']
    scenes.append(scene_obj)

total_frames = sum(s['durationInFrames'] for s in scenes)

project_data = {
    'title': 'Эдвард Торп: Как математик обыграл мафию Лас-Вегаса',
    'fps': FPS,
    'width': 1080,
    'height': 1920,
    'bgMusic': 'music/casino_thriller.wav',
    'bgMusicVolume': 0.14,
    'voiceAudio': 'audio/thorp_voice.wav',
    'voiceVolume': 1.0,
    'showProgressBar': True,
    'progressBarColor': '#f59e0b',
    'scenes': scenes
}

BASE_DIR = r"c:\Users\Admin\Desktop\бурмолда\claude_video_studio"
out_path = os.path.join(BASE_DIR, 'projects', 'edward_thorp', 'script.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(project_data, f, ensure_ascii=False, indent=2)

print(f"Regenerated script.json: {total_frames} frames @ {FPS}fps = {total_frames/FPS:.2f} seconds")
