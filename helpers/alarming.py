import os

import requests

from helpers.imports_from_file import import_settings


class TelebotBasic:
    """
    Базовый бот для телеграмм
    """

    URL = r'https://api.telegram.org/bot'
    TOKEN = r''
    CHAT_ID = r''
    SM = r'/sendMessage?chat_id='
    SMT = r'&text='
    SP = r'/sendPhoto?chat_id='
    SD = r'/sendDocument?chat_id='
    SPC = r'&caption='
    HTML_PARSE = r"&parse_mode=HTML"

    EMOJI = {
        "progress": b'\xE2\x8C\x9A'.decode('utf-8'),
        "error": b'\xE2\x9D\x8C'.decode('utf-8'),
        "ok": b'\xE2\x9C\x85'.decode('utf-8'),
        "warning": b'\xE2\x9D\x97'.decode('utf-8'),
        "delivery": b'\xF0\x9F\x9A\x9A'.decode('utf-8')
    }

    def send_message(self, message: str) -> None:
        """
        Отправка сообщений через бота
        :param message: строка сообщений
        :return: None
        """
        link = self.URL + self.TOKEN + self.SM + self.CHAT_ID + self.SMT + message + self.HTML_PARSE
        requests.get(link)

    def send_image(self, file_link: str, caption: str) -> None:
        """
        Отправка изображений через бота
        :param file_link: Путь к файлу
        :param caption: подпись к картинке
        :return:
        """

        files = {'photo': open(file_link, 'rb')}
        link = self.URL + self.TOKEN + self.SP + self.CHAT_ID + self.SPC + caption
        requests.post(link, files=files)

    def send_document(self, file_link: str, caption: str) -> None:
        """
        Отправка документов через бот
        :param file_link: Путь к файлу
        :param caption: подпись к картинке
        :return:
        """

        files = {'document': open(file_link, 'rb')}
        link = self.URL + self.TOKEN + self.SD + self.CHAT_ID + self.SPC + caption
        requests.post(link, files=files)

    def send_log_message(self, emoji: str, process: str, message: str) -> None:
        """
        Отправляет в лог сообщения через телеграмм
        :param emoji: должно быть emoji из {self.EMOJI}
        :param process: название процесса
        :param message: сообщение, если нужнто что-то добавить
        :return:
        """

        message_to_send = self.EMOJI[emoji] + " <b>[" + process + "]</b> " + message + " " + caption_date_time()

        self.send_message(message_to_send)


class TelebotMWLWatchers(TelebotBasic):
    # Бот MWLWatchers
    def __init__(self):
        # Получаем настройки
        settings = import_settings(os.path.join(os.path.dirname(__file__), r"../resources/passwords/passwords.yml"))

        self.TOKEN = settings["TOKEN"]
        self.CHAT_ID = settings["CHAT_ID"]


def caption_date_time(md='date+time'):
    # по умолчанию дата и время
    import datetime as dt
    now = dt.datetime.now()

    if md == 'date+time':
        t0 = now.strftime("%d-%m-%Y %H:%M")
    elif md == 'date':
        t0 = now.strftime("%d-%m-%Y")

    res = '(дата: ' + t0 + ')'
    return res


if __name__ == "__main__":
    testBot = TelebotMWLWatchers()
    testBot.send_log_message("warning", "Test process", "Тестирую по-маленьку")
