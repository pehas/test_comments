# Комментарии
---
## Тестовый сервер на heroku

>[https://frozen-hamlet-61348.herokuapp.com/](https://frozen-hamlet-61348.herokuapp.com/)

## Усатновка зависимостей
```bash
virtualenv .env
. .env/bin/activate
pip install -r requirements.txt
```

## Миграция и загрузка тестовых данных
```bash
./manage.py migrate
```

## Создания администратора
```bash
./manage.py createsuperuser
```

## Запуск проекта
```bash
./manage.py runserver
```

## Админка проекта
 >[/admin](https://frozen-hamlet-61348.herokuapp.com/admin/)