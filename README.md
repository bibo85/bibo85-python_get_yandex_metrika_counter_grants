# Получение информации о разрешениях, выданных на счетчиках Яндекс.Метрики

![Static Badge](https://img.shields.io/badge/python-3.10.6-blue)
![Static Badge](https://img.shields.io/badge/termcolor-1.1.0-purple)
![Static Badge](https://img.shields.io/badge/gspread-5.4.0-green)


## Описание проекта
Скрипт подключается к аккаунту Яндекса и получает информацию обо всех счетчиках Яндекс.Метрики, которые есть на аккаунте или на которые у аккаунта есть доступ.
По каждому счетчику скрипт получает список логинов и их разрешения. Дальше вся эта информация заносится в Google таблицу.

## Документация
1. Все зависимости описаны в файле __requirements.txt__
2. В файле __instruction.txt__ прописана инструкция для получения json ключа для доступа к Google таблицам
3. Необходимо прописать настройки в файле ___settings.py__. Заполняем все поля, кроме HEADERS_PARAMS. После добавления информации нижнее подчеркивание в названии файла необходимо убрать

Для получения токена Яндекса используем эту инструкцию: https://yandex.ru/dev/id/doc/ru/how-to
```python
ACCESS_TOKEN = ""  # yandex token
GOOGLE_JSON = ''  # google sheet token. Пример: 'callibri-statistics-es23ad738329c6.json. Получать по инструкции'
URL_SHEET = ''  # Пример: 'https://docs.google.com/spreadsheets/d/1NsL_AI0sapXqQ37dxmtcFqOUNq25w3e_8/edit#gid=12564186'
NAME_WORKSHEET = ''  # имя рабочего листа гугл таблицы. Пример: 'Тест'
START_ROW = 2  # строка, с которой скрипт будет записывать данные. По умолчанию стоит вторая строка
HEADERS_PARAMS = {  # header, который передается в get запросе к api метрики
    'GET': '/management/v1/counters HTTP/1.1',
    'Host': 'api-metrika.yandex.net',
    'Authorization': 'OAuth ' + ACCESS_TOKEN,
    'Content-Type': 'application/x-yametrika+json',
    'Content-Length': '123'
}
```
4. Предоставляем доступ на редактирование в рабочие Google таблицы для почты сервисного аккаунта гугла, который создали по инструкции.
   Пример такой почты: parser@parser377917.iam.gserviceaccount.com
