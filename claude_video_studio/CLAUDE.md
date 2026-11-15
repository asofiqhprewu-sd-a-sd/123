# CLAUDE VIDEO STUDIO - AI Motion Graphics & Video Editing Suite

Этот документ — мастер-руководство для Claude Code и AI-ассистентов по созданию, озвучке и монтажу динамичных вертикальных видео (Reels / Shorts / TikTok) в визуальном стиле технологических расследований и сторителлинга (стиль референса `референс.mp4`).

---

## 1. Обзор архитектуры

Студия построена на базе:
- **Remotion (React 18 + Node.js)**: Программный рендеринг видео кинематографического качества (1080x1920, 30fps).
- **Python CLI Orchestrator (`studio.py`)**: Управление проектами, генерация речи и сборка.
- **Neural TTS Engine (`pipeline/tts_engine.py`)**: Синтез речи (Microsoft Neural / OpenAI / ElevenLabs) с таймингами слов.
- **Procedural Sound Engine (`pipeline/sfx_generator.py`)**: Библиотека звуковых эффектов (попы, вуши, клики, пинги, кассовый аппарат, клавиатура, бас-дропы) и ambient-музыки.
- **Motion Components (`src/components/`)**: Библиотека готовых визуальных блоков из референса и современных медиа.

---

## 2. Быстрые команды терминала

Все команды запускаются из папки `claude_video_studio`:

```bash
# Посмотреть список всех проектов
python studio.py list

# Создать новый проект по шаблону
python studio.py new my_project --title "Заголовок проекта"

# Сгенерировать нейросетевую озвучку и расставить тайминги слов
python studio.py voice my_project --voice ru-RU-DmitryNeural

# Отрендерить финальный MP4 ролик
python studio.py render my_project

# Запустить интерактивный визуальный предпросмотр в браузере (Remotion Studio)
python studio.py preview my_project

# Или запустить полную генерацию в одну команду (озвучка + рендер)
python studio.py create my_project
```

---

## 3. Каталог визуальных компонентов

Все компоненты поддерживают плавные пружинные анимации входа и левитацию.

### 1. `KineticText` (Кинетический текст с фокусом)
Активное произносимое слово находится в резком фокусе, а остальные слова мягко размыты (`blur`).
```json
"text": "как за одну ночь стать миллионером",
"fontSize": 58,
"textPosition": "top"
```

### 2. `StatCounter` (Анимированный счетчик чисел)
Числа стремительно растут от `start` до `end` с замедлением. Отлично для выручки, пользователей, процентов:
```json
"counter": {
  "start": 0,
  "end": 100000000,
  "prefix": "$",
  "suffix": "",
  "label": "капитализация компании",
  "color": "#22c55e"
}
```

### 3. `RealFootage` (Реальные кадры и фотографии с эффектом Ken Burns)
Полноразмерные кадры или парящие стеклянные рамки с кинематографичным зумом и геолокацией:
```json
"photo": {
  "src": "photos/paris/scene1.jpg",
  "tag": "Остров Сите • Река Сена",
  "glowColor": "rgba(56, 189, 248, 0.35)",
  "zoomDirection": "in",
  "mode": "card" // или "fullscreen"
}
```

### 4. `PhotoComparison` (Сравнение исторических фото До / После)
Два реальных кадра (например, стройка 1888 года vs современный вид):
```json
"photoComparison": {
  "leftPhoto": "photos/paris/eiffel_construction.jpg",
  "rightPhoto": "photos/paris/eiffel_tower.jpg",
  "leftLabel": "Стройка 1888",
  "rightLabel": "Сегодня",
  "tag": "История создания"
}
```

### 5. `CodeEditor` (Окно редактора кода / терминала)
MacOS-стиль окна с цветными кнопками, вкладкой файла и живым набором кода:
```json
"code": {
  "filename": "ai_agent.py",
  "lines": [
    { "text": "import antigravity, ai_core", "color": "#f43f5e" },
    { "text": "agent = AutonomousAgent('v2')", "color": "#38bdf8" },
    { "text": "while True: solve_impossible()", "color": "#4ade80" }
  ]
}
```

### 4. `PhoneMockup` (Чат переписка на смартфоне)
Смартфон с Dynamic Island и всплывающими облачками сообщений:
```json
"phone": {
  "contactName": "Sequoia Capital",
  "messages": [
    { "from": "them", "text": "Мы протестировали вашего агента." },
    { "from": "them", "text": "Мы готовы выписать чек на $15M." }
  ]
}
```

### 5. `ComparisonSplit` (Сравнение двух сущностей / VS)
Две карточки по бокам с горящим бейджем `VS` по центру:
```json
"comparison": {
  "leftTitle": "Claude 3.5 Sonnet",
  "leftIcon": "icons/claude.png",
  "leftStat": "93.7% код бенчмарки",
  "rightTitle": "GPT-4o",
  "rightIcon": "icons/openai.png",
  "rightStat": "Мультимодальный флагман"
}
```

### 6. `QuoteCard` (Цитатная карточка с неоновыми кавычками)
Для драматических цитат и ключевых мыслей:
```json
"quote": {
  "text": "Один человек с правильной нейросетью теперь может заменить целую корпорацию.",
  "author": "Основатель стартапа",
  "title": "21 год"
}
```

### 7. `TweetCard` (Виджет твита)
Карточка поста из X/Twitter с аватаром и верификацией:
```json
"tweet": {
  "name": "Ilya Sutskever",
  "handle": "@ilyasut",
  "avatar": "avatars/sutskever.jpg",
  "text": "I deeply regret my participation in the board's actions."
}
```

### 8. `PersonCard` (Карточки персоналий)
Герои с фото и подписью:
```json
"person": {
  "name": "илон маск",
  "image": "avatars/musk.jpg"
}
```

### 9. `ConnectingDiagram` (Пунктирные связи)
Связи между сущностями (например, корпорация <---> стартап):
```json
"diagram": {
  "leftIcon": "icons/building.png",
  "rightIcon": "icons/microsoft.png",
  "leftLabel": "лаборатория",
  "rightLabel": "инвестор"
}
```

### 10. `CalendarCard` (Карточка даты)
```json
"calendar": {
  "month": "ноябрь",
  "day": "30",
  "headerColor": "#ef4444"
}
```

---

## 4. Звуковые эффекты (`sfx/`)

- `sfx/pop.wav` — классический UI-поп (появление карточек).
- `sfx/whoosh.wav` — кинематографичный переход сцен.
- `sfx/cash.wav` — звон монет и кассы (деньги, рост, инвестиции).
- `sfx/keyboard.wav` — тактильный набор на клавиатуре (код, терминал).
- `sfx/impact.wav` — глубокий трейлерный бас-бум (кульминации).
- `sfx/glitch.wav` — цифровой глитч (хакерство, баги, резкие смены).
- `sfx/heartbeat.wav` — напряжённый пульс (драма, ожидание).
- `sfx/drop.wav` — плотный бас-дроп.
- `sfx/ping.wav` — мелодичный колокольчик уведомления.

---

## 5. Доступные иконки (`icons/`)

- `icons/rocket.svg` — 3D ракета стартапа
- `icons/cash_stack.svg` — 3D пачка долларов
- `icons/growth_chart.svg` — неоновый график роста
- `icons/robot_head.svg` — футуристичный робот/ИИ
- `icons/lightning.svg` — кибер-молния
- `icons/fire_viral.svg` — вирусный огонь
- `icons/openai.png` — 3D розета OpenAI
- `icons/claude.png` — коралл-звезда Anthropic
- `icons/xai.png` — лого xAI
- `icons/eiffel.svg` — золотая Эйфелева башня
- `icons/louvre.svg` — стеклянная пирамида Лувра
- `icons/notre_dame.svg` — собор Нотр-Дам

---

## 6. Алгоритм работы для Claude

Когда пользователь просит создать ролик:
1. Выбрать тему и формат (история, стартап, битва технологий, расследование).
2. Создать проект: `python studio.py new <project_name>`.
3. Составить сцены в `projects/<project_name>/script.json`, используя визуальные компоненты выше.
4. Озвучить: `python studio.py voice <project_name>`.
5. Отрендерить: `python studio.py render <project_name>`.
6. Выдать пользователю кликабельную ссылку на MP4 файл!
