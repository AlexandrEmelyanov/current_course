# Current course

Проект - курс валют, предназначен для непрерывного получения актуального курса доллара к рублю.

В проекте реализована работа с внешним Currency API для получения актуальной информации о курсе валют и дальнейшей 
её обработки.

**Стек:**
+ [Python](https://www.python.org/downloads/)
+ [Redis](https://redis.io/)
+ [Celery](https://docs.celeryq.dev/en/stable/index.html#)
+ [SQLite3](https://www.sqlite.org/index.html)
+ [Currency API](https://currencyapi.com/)


## Локальная разработка:

Все действия должны выполняться из исходного каталога проекта и только после установки всех требований.

1. Создайте и активируйте новую виртуальную среду:

```shell
python -m venv venv
venv\Scripts\activate
```

2. Установите пакеты:

```shell
pip install --upgrade pip
pip install -r requirements.txt
```

3. Выполните миграции в базу данных:

```shell
python manage.py migrate
```


4. Создайте суперпользователя:

```shell
python manage.py createsuperuser
```


5. Запустите Redis: [инструкция по запуску](https://redis.io/docs/install/install-redis/).


6. Запустите сервер:
```shell
python manage.py runserver
```


8. Запустите **Celery**:
   + если вы используете ОС Windows, необходимо запустить через **eventlet**:

    ```shell
    celery -A current_course worker --loglevel=info -P eventlet
    ```

   + если другую ОС:

    ```shell
    celery -A current_course worker -l INFO
    ```
   
    + Запустите **Celery beat** (для передачи задач каждые 15 минут на выполнение celery worker):
    
    ```shell
    celery -A current_course beat --loglevel=info
    ```

После успешного запуска, проект будет доступен по адресу: http://127.0.0.1:8000/get-current-usd/


## Админ-панель

Админ-панель доступна по адресу: http://127.0.0.1:8000/admin/ 

Вы можете выполнять все **CRUD-операции** по полученным запросам.


## Тестовые данные

Вы можете загрузить файлы фикстур, для заполнения данными БД.

```shell
python manage.py loaddata <path_to_fixture_files>
```

**Примечание 1:** файл фикстур в проекте находится по следующему пути:
+ currency/fixtures/currency.json


**Примечание 2:** после загрузки фикстур может потребоваться выполнить команды:

```shell
python manage.py makemigration 
python manage.py migrate
```

**Примечание 3:** если после загрузки фикстур в логах Celery возникают ошибки, очистите содержимое модели CurrencyRate 
и создайте новые.


## Логирование

В файле **log.log** отображается информация об ошибках отправки запроса на **внешний API (Currency API)**, также 
информация об успешных запросах и добавления этих запросов в БД.