import gspread
from termcolor import cprint
import settings

import funcs

print('Получаем счетчики метрики аккаунта')
response = funcs.get_metric_counters()

if not response:
    print('Счетчики не получены')
    raise Exception('Выполнение скрипта прервано')

# создаем список из id счетчиков
print('Получаем id счетчиков')
metriks_counters = funcs.get_list_of_counters(response.json()['counters'])

print('Счетчики получены')
print(metriks_counters)

# настройка гугл таблицы
gc = gspread.service_account(filename=settings.GOOGLE_JSON)
sh = gc.open_by_url(settings.URL_SHEET)
worksheet = sh.worksheet(settings.NAME_WORKSHEET)

# заносим данные по счетчикам
row = settings.START_ROW

for counter in metriks_counters:
    print(f'Получаем настройки по счетчику: {counter}')
    response = funcs.get_grants_from_counter_settings(counter)
    if not response:
        print('Данные по счетчику не получены')
        continue
    print('\t Обновляем данные в гугл таблице')
    metric_id = response.json()['counter']['id']
    grants = response.json()['counter']['grants']
    try:
        funcs.update_cells(worksheet, row, 1, metric_id)  # добавляем в таблицу номер счетчика
        if grants:
            for grant in grants:
                funcs.update_cells(worksheet, row, 2, grant['email'])
                funcs.update_cells(worksheet, row, 3, grant['perm'])
                row += 1
        else:
            row += 1
    except Exception as exc:
        cprint(f'При обновлении данных по счетчику {counter} возникла ошибка:', color='red')
        print(exc)
        row += 1

cprint('Все настройки по счетчикам получены', color='green')
