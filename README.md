# Тестовое задание
___
## Основные технологии: ##
- Язык: Python
- Фреймворк: DjangoRestFramework
- Зависимости: Pip-tools
- БД: SQLite - для удобства, но обычно использую PostgreSQL
- Айтентификация: JWT
- Тестирование: Postman
---

## Использование: ##

После создания и активации виртуальной среды:

> внутри settings.py установите любое значение для SECRET_KEY

> pip install pip-tools

> make install-deps

> python manage.py runserver

Для удобства закинул файл с БД сюда, но для тестовых целей можете заругистрировать новых пользователей с помощью 
http://localhost:8000/api/v1/register/
___
## По безопасности: ##
- Защита от SQL-инъекций вшита в django ORM
- Реализовал кастомный permission класс для того, чтобы пользователь мог узнавать информацию только о себе
- Использовал .env
___

Если будут какие-то вопросы, буду рад ответить!