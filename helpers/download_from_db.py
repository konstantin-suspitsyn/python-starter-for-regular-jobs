import os

import pandas as pd
import sqlalchemy
import warnings

from helpers.imports_from_file import import_settings


class DownloadDataFromDB:
    """
    Загружаем данные из базы данных
    """

    def __init__(self):
        # Получаем настройки
        self.settings = import_settings(os.path.join(os.path.dirname(__file__), r"../resources/settings/settings.yml"))
        # Получаем пароли
        self.passwords = import_settings(
            os.path.join(os.path.dirname(__file__), r"../resources/passwords/passwords.yml"))

    def get_data_from_gp(self, sql_script: str) -> pd.DataFrame:
        """
        Получаем данные из GreenPlum c помощью pandas
        :param sql_script:
        :return:
        """

        postgres_connection_string = r"postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            self.passwords["user_gp"],
            self.passwords["password_gp"],
            self.settings["host_gp"],
            self.settings["port_gp"],
            self.settings["db_gp"])

        engine = sqlalchemy.create_engine(postgres_connection_string)

        df_dcs = pd.read_sql(sql_script, con=engine)
        engine.dispose()

        return df_dcs

    def read_data_from_bw(self, sql_script: str) -> pd.DataFrame:
        """
        Получаем данные из BW c помощью pandas
        :param sql_script:
        :return:
        """

        bw_connection_string = "hana+hdbcli://{}:{}@{}:{}".format(self.passwords["user_bw"],
                                                                  self.passwords["password_bw"],
                                                                  self.settings["host_bw"],
                                                                  self.settings["port_bw"])

        engine = sqlalchemy.create_engine(bw_connection_string)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", sqlalchemy.exc.SAWarning)
            df_data = pd.read_sql(sql_script, con=engine)

        engine.dispose()

        return df_data
