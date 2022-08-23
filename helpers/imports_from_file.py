import yaml
import datetime as dt


def import_settings(settings_yaml: str) -> dict:
    """
    :param settings_yaml: ссылка на родительские настройки
    :return: словарь с настройками
    """
    # Загружаем родительские настройки в словарь
    with open(settings_yaml, 'r') as ymlfile:
        parent_cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    return parent_cfg


def get_sql_script(sql_path: str, change_dict: dict) -> str:
    """
    :param sql_path: путь к файлу с sql скриптом
    :param change_dict: мы меняем токены на нужные нам вещи
    :return: sql скрипт =с измненными данными
    """

    with open(sql_path, 'r', encoding='utf-8') as sql_file:
        sql_script = sql_file.read()

    if change_dict is not None:
        for key, value in change_dict.items():
            sql_script = sql_script.replace(key, str(value))

    return sql_script


def log_into_terminal(message: str) -> None:
    """
    Отправляет лог по текущему действию
    :param message: сообщение
    :return: None
    """
    print(message, dt.datetime.now().strftime("%Y-%m-%d %H:%M"))


def from_list_to_srt(list_of_str: list):
    """
    Переводим данные из list в string через запятую в одинарных кавычках
    :param list_of_str:
    :return:
    """
    return "'" + "', '".join(list_of_str) + "'"

