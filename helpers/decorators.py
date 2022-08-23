from helpers.alarming import TelebotMWLWatchers


def message_wrapper(process: str):

    def handle_exceptions(f):

        def wrapper(*args, **kw):
            telebot_mvm = TelebotMWLWatchers()
            try:
                telebot_mvm.send_log_message("progress", process, "Начало процесса")
                f(*args, **kw)
                telebot_mvm.send_log_message("ok", process, "Готово")
                del telebot_mvm
                return
            except Exception as e:
                error_message = "Fucked Up: " + str(e)
                telebot_mvm.send_log_message("error", process, error_message[:500])
                del telebot_mvm

        return wrapper

    return handle_exceptions


if __name__ == "__main__":
    @message_wrapper("successful function")
    def do():
        print("do")

    @message_wrapper("error test")
    def dont():
        print(0 / "a")

    do()
    print("______________________________________")
    dont()
