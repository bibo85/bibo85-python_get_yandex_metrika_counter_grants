import requests
from termcolor import cprint
import settings


def get_metric_counters():
    """ Получение информации по всем счетчикам на аккаунте яндекс метрики

    :return response: json с данными счетчиков
    """
    attempt_counter = 0
    response = None
    while attempt_counter < 3:
        try:
            response = requests.get("https://api-metrika.yandex.net/management/v1/counters",
                                    headers=settings.HEADERS_PARAMS,
                                    timeout=90
                                    )
            if response.status_code == 200:
                break
            attempt_counter += 1
        except Exception as exc:
            attempt_counter += 1
            cprint('Не удалось получить счетчики метрики', color='red')
            print('Ошибка:')
            print(exc)
            print('Пробуем еще раз')

    return response


def get_list_of_counters(counters_data) -> list:
    """
    Создаем список из id счетчиков метрики

    :param counters_data: данные по счетчикам метрики
    :return: list список из id счетчиков
    """
    metriks_counters = []
    for counter in counters_data:
        metriks_counters.append(counter['id'])
    return metriks_counters


def get_grants_from_counter_settings(counter):
    """ Получение логинов, которые имеют доступ к счетчику метрики, и  их разрешений

    :return response: json с данными доступов к счетчику - логины и разрешения
    """
    attempt_counter = 0
    response = None
    while attempt_counter < 3:
        try:
            response = requests.get(f"https://api-metrika.yandex.net/management/v1/counter/{counter}?field=grants",
                                    headers=settings.HEADERS_PARAMS,
                                    timeout=90
                                    )
            if response.status_code == 200:
                break
            attempt_counter += 1
        except Exception as exc:
            attempt_counter += 1
            cprint('Не удалось получить данные по счетчику', color='red')
            print('Ошибка:')
            print(exc)
            print('Пробуем еще раз')

    return response


def update_cells(worksheet, row, col, data) -> None:
    """
    Обновление ячейки таблицы

    :param worksheet: рабочий лист гугл таблицы
    :param row: строка
    :param col: колонка
    :param data: данные для обновления
    :return: None
    """
    worksheet.update_cell(row, col, data)
