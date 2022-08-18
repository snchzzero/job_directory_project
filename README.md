# Тестовое задание
### Разработка веб сервиса, который:
### Задание №1 — Позволяет создавать, редактировать, просматривать список должностей
#### Решение:
В качестве веб фреймворка используется Django 4.0.5. Для создания фронтэнда части сервиса использовались: HTML и Bootstrap v5.2.
Изначально была создана по умолчанию в Django БД "db.sqlite3". Затем выполнена миграция БД на движке "postgresql_psycopg2" на хостинг heroku.com.
#### Окно добавления новой должности
![Screenshot](pic_1a.png)

#### Окно просмотра доступных должностей
(по умолчанию выполнена сортировка по названию должности)
![Screenshot](pic_2.png)

#### Окно редактирования выбранной должности
![Screenshot](pic_3.png)

### Задание №2 — Позволяет создавать, редактировать, просматривать сотрудников. При создании, редактировании сотрудника предусмотреть возможность выбора должности из ранее созданных должностей.
#### Решение:

#### Окно добавления нового сотрудника:
![Screenshot](pic_4.png)

#### Окно просмотра доступных сотрудников:
(по умолчанию выполнена сортировка по фамилии сотрудников)
![Screenshot](pic_5.png)

#### Окно редактирования выбранного сотрудника
![Screenshot](pic_6.png)

#### При создании, редактировании сотрудника предусмотреть возможность выбора должности из ранее созданных должностей.
![Screenshot](pic_7.png)

#### Доступная навигация в веб сервисе
![Screenshot](pic_8.PNG)

Сервис упакован в Docker. Для запуска достаточно находиться в директории с файлом _'manage.py'_ и в терминале ввести следующее:
```shell
    docker-compose build
    docker-compose up
```

Доступ к веб сервису:
```shell
    http://127.0.0.1:8000/ - в браузере
```