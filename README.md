# Django URL Shortener

Веб-приложение для сокращения URL-ссылок. Пользователь вводит длинный URL, получает короткую ссылку, по которой происходит автоматическое перенаправление на исходный адрес.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-5.1-green)

## Возможности

- Сокращение длинных URL в короткие 6-символьные ссылки
- Автоматическое перенаправление по короткой ссылке
- Повторный ввод того же URL возвращает ранее созданную короткую ссылку
- Копирование короткой ссылки в буфер обмена

## Стек

- **Django 5.1** — веб-фреймворк
- **SQLite** — база данных
- **HTML/CSS/JavaScript** — фронтенд

## Структура проекта

```
url_shortener/
├── url_shortener/         # Настройки Django
├── main_app/              # Основное приложение
│   ├── models.py          # Модель для хранения URL
│   ├── views.py           # Логика сокращения и редиректа
│   ├── forms.py           # Форма ввода URL
│   ├── static/            # CSS, JS
│   └── templates/         # HTML-шаблон
├── manage.py
└── requirements.txt
```

## Установка и запуск

```bash
git clone https://github.com/makel0ve/short-URL.git
cd short-URL
pip install -r requirements.txt
cp .env.example .env
python url_shortener/manage.py migrate
python url_shortener/manage.py runserver
```

Открыть в браузере: `http://127.0.0.1:8000`