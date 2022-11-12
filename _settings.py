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
