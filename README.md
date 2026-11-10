# My First Autotests (Playwright + Pytest)

Учебный проект по автоматизации тестирования UI на Python.

## Требования
- Python 3.12+
- Установленный Git

## Установка и запуск

1. Клонируйте репозиторий:
   `git clone <ссылка_на_твой_репозиторий>`
2. Перейдите в папку проекта:
   `cd my-first-autotests`
3. Создайте виртуальное окружение:
   `python -m venv .venv`
4. Активируйте окружение:
   - Windows: `.\.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`
5. Установите зависимости:
   `pip install -r requirements.txt`
6. Установите браузеры для Playwright:
   `playwright install chromium`

## Запуск тестов
Запуск всех UI-тестов:
`pytest -m ui -v`

Запуск всех тестов:
`pytest -v`