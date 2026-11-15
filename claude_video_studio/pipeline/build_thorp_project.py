import json
import os

scenes_config = [
    {
        'id': 's1_vegas_intro',
        'durationInFrames': 1014,
        'photo': 'photos/thorp/scene1.jpg',
        'text': 'в 1960 году владельцы казино считали себя богами',
        'badge': {
            'icon': '📍',
            'label': 'Лас-Вегас • 1960 год',
            'sub': 'Математик против Мафии'
        },
        'sfx': 'sfx/whoosh.wav'
    },
    {
        'id': 's2_mit_computer',
        'durationInFrames': 516,
        'photo': 'photos/thorp/scene2.jpg',
        'text': 'на суперкомпьютере mit он просчитал миллионы комбинаций',
        'badge': {
            'icon': '💻',
            'label': 'Лаборатория MIT • IBM 704',
            'sub': 'Теория вероятностей'
        },
        'widget': {
            'icon': '⚙️',
            'title': 'Суперкомпьютер IBM 704',
            'value': 'Миллионы комбинаций карт просчитаны',
            'glowColor': 'rgba(56, 189, 248, 0.3)',
            'borderColor': 'rgba(56, 189, 248, 0.5)'
        },
        'sfx': 'sfx/keyboard.wav'
    },
    {
        'id': 's3_blackjack_win',
        'durationInFrames': 762,
        'photo': 'photos/thorp/scene3.jpg',
        'text': 'за одну ночь профессор выносил десятки тысяч долларов',
        'badge': {
            'icon': '🃏',
            'label': 'Блэкджек • Лас-Вегас',
            'sub': 'Подсчет карт'
        },
        'widget': {
            'icon': '💵',
            'title': 'Выигрыш за одну ночь',
            'value': '+$20,000 • Дилеры в шоке',
            'glowColor': 'rgba(34, 197, 94, 0.35)',
            'borderColor': 'rgba(34, 197, 94, 0.5)',
            'valueColor': '#4ade80'
        },
        'sfx': 'sfx/cash.wav'
    },
    {
        'id': 's4_mob_rules',
        'durationInFrames': 534,
        'photo': 'photos/thorp/scene4.jpg',
        'text': 'казино изменили правила игры по всей америке',
        'badge': {
            'icon': '⚠️',
            'label': 'Охота мафии • Невада',
            'sub': 'Чрезвычайные меры'
        },
        'widget': {
            'icon': '🚨',
            'title': 'Реакция владельцев казино',
            'value': 'Правила блэкджека изменены по всей США',
            'glowColor': 'rgba(239, 68, 68, 0.4)',
            'borderColor': 'rgba(239, 68, 68, 0.6)',
            'valueColor': '#f87171'
        },
        'sfx': 'sfx/drop.wav'
    },
    {
        'id': 's5_shoe_computer',
        'durationInFrames': 402,
        'photo': 'photos/thorp/scene5.jpg',
        'text': 'первый в истории носимый компьютер в каблуке ботинка',
        'badge': {
            'icon': '👟',
            'label': 'Тайное изобретение • 1961',
            'sub': 'Шеннон & Торп'
        },
        'widget': {
            'icon': '⚡',
            'title': 'Первый носимый микрокомпьютер',
            'value': 'Транзисторы в каблуке • Кликер в пальце',
            'glowColor': 'rgba(245, 158, 11, 0.35)',
            'borderColor': 'rgba(245, 158, 11, 0.6)',
            'valueColor': '#facc15'
        },
        'sfx': 'sfx/camera.wav'
    },
    {
        'id': 's6_roulette_edge',
        'durationInFrames': 312,
        'photo': 'photos/thorp/scene6.jpg',
        'text': 'они обыгрывали рулетку с перевесом в сорок четыре процента',
        'badge': {
            'icon': '🎯',
            'label': 'Разгром рулетки',
            'sub': 'Имба математики'
        },
        'widget': {
            'icon': '📊',
            'title': 'Математический перевес над казино',
            'value': '+44% преимущество в пользу игрока',
            'glowColor': 'rgba(16, 185, 129, 0.4)',
            'borderColor': 'rgba(16, 185, 129, 0.6)',
            'valueColor': '#34d399'
        },
        'sfx': 'sfx/impact.wav'
    },
    {
        'id': 's7_wallstreet_climax',
        'durationInFrames': 273,
        'photo': 'photos/thorp/scene7.jpg',
        'text': 'против законов математики бессильны любые корпорации мира',
        'badge': {
            'icon': '📈',
            'label': 'Уолл-стрит • Хедж-фонд',
            'sub': 'Легенда финансов'
        },
        'widget': {
            'icon': '🏆',
            'title': 'Princeton Newport Partners',
            'value': '$273,000,000 • 30 лет без убытков',
            'glowColor': 'rgba(245, 158, 11, 0.4)',
            'borderColor': 'rgba(245, 158, 11, 0.6)',
            'valueColor': '#fbbf24'
        },
        'sfx': 'sfx/ping.wav'
    }
]

FPS = 60
scenes = []
for sc in scenes_config:
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
        'sfx': sc['sfx']
    }
    if 'widget' in sc:
        scene_obj['widget'] = sc['widget']
    scenes.append(scene_obj)

total_frames = sum(s['durationInFrames'] for s in scenes)

project_data = {
    'title': 'Эдвард Торп: Как математик обыграл казино и создал Уолл-стрит',
    'fps': FPS,
    'width': 1080,
    'height': 1920,
    'bgMusic': 'music/casino_thriller.wav',
    'bgMusicVolume': 0.16,
    'voiceAudio': 'audio/thorp_voice.wav',
    'voiceVolume': 1.0,
    'showProgressBar': True,
    'progressBarColor': '#f59e0b',
    'scenes': scenes
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_path = os.path.join(BASE_DIR, 'projects', 'edward_thorp', 'script.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(project_data, f, ensure_ascii=False, indent=2)

print(f"Generated script.json: {total_frames} frames @ {FPS}fps = {total_frames/FPS:.2f} seconds")
