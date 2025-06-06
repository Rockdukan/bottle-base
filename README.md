# Bottle Base — базовый шаблон для приложений на Bottle
Bottle — это простой и лёгкий Python-фреймворк для создания веб-приложений.
Он идеально подходит для небольших проектов.
![screenshot](screenshot.jpg)

## 🔧 В шаблоне реализовано:
- Базовая структура проекта
- Конфигурация через `config.py`
- Тестовый HTML-маршрут(`/`) и API(`GET  /api/ping`)
- Поддержка статики (CSS, JS, изображения, шрифты)
- Логирование:
    - Ротация логов: ежедневно
    - Хранятся: 7 дней
    - Уровни логов: от `INFO` до `CRITICAL`

## 📦 Структура проекта
```
├── app/
│   ├── controllers/
│   │   ├── api.py
│   │   ├── html.py
│   │   └── static.py
│   │   
│   ├── models/
│   ├── services/
│   ├── views/
│   └── log.py
│
├── logs/
├── media/
├── static/
├── config.py
├── main.py
└── README.md
```

## ⚙️ Установка и запуск
```bash
git clone https://gitverse.ru/Rockdukan/bottle-base.git
cd bottle-base
uv venv
uv run main.py
```
