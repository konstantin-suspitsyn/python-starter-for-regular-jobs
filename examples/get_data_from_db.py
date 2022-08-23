import os

import pandas as pd

from helpers.download_from_db import DownloadDataFromDB
from helpers.imports_from_file import get_sql_script
from helpers.decorators import message_wrapper


class GetDataFromDB:
    """
    Пример получения данных из базы данных
    """

    # Папка, в которой находится данный класс
    SELF_ADDRESS = os.path.dirname(__file__)

    # Пример скрипта в GP
    EXAMPLE_GP_SQL = r"../resources/sql/sql_example_gp.sql"

    # Пример скрипта в BW
    EXAMPLE_BW_SQL = r"../resources/sql/sql_example_bw.sql"

    def __init__(self):
        self.connection_to_db = DownloadDataFromDB()

    def get_simple_sql_gp(self) -> pd.DataFrame:
        """
        Пример получения данных из sql, GreenPlum
        :return: DataFrame с данными из GreenPlum
        """

        sql_script = get_sql_script(os.path.join(self.SELF_ADDRESS, self.EXAMPLE_GP_SQL), None)

        df_result = self.connection_to_db.get_data_from_gp(sql_script)

        return df_result

    def get_simple_sql_bw(self):
        """
        Пример получения данных из sql, BW
        :return: DataFrame с данными из BW
        """

        sql_script = get_sql_script(os.path.join(self.SELF_ADDRESS, self.EXAMPLE_BW_SQL), None)
        df_result = self.connection_to_db.read_data_from_bw(sql_script)

        return df_result

    def div_by_zero(self) -> None:
        """
        Функция будет возвращать ошибку
        :return:
        """
        return 1/0


if __name__ == "__main__":

    @message_wrapper("Пример работы pipeline без ошибки")
    def pipeline_no_error() -> None:
        """
        Выполняется без ошибки
        :return:
        """
        get_data_from_db_example = GetDataFromDB()
        print(get_data_from_db_example.get_simple_sql_gp().head())
        print(get_data_from_db_example.get_simple_sql_bw().head())

    @message_wrapper("Пример работы pipeline c ошибкой")
    def pipeline_with_error() -> None:
        """
        Вернет ошибку деления на 0
        :return:
        """
        get_data_from_db_example = GetDataFromDB()
        print(get_data_from_db_example.get_simple_sql_gp().head())
        get_data_from_db_example.div_by_zero()


    pipeline_no_error()
    pipeline_with_error()
