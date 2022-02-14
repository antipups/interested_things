"""
    Демонстрация паттерна "фабричный метод"
"""

import re
from sqlite3 import Connection
from loguru import logger
from my_package import constants
from abc import ABC


class _Database(ABC):
    """
        Класс для работы с бд через запросы
    """

    def __init__(self):
        """
            Возможно переобределение конктруктора в случае смены драйвера базы данных
        """
        self._connect = Connection(constants.Filenames.SqliteDb)
        self._cursor = self._connect.cursor()

    def __enter__(self):
        """
            Для работы контекстного менеджера with
        :return:
        """
        logger.info(f'Open DB connection')
        return self

    def execute(self, queries: str | tuple | list, description: bool = False):
        """
            Для уменьшения кол-ва строк
        :param queries: запросы
        :param description: нужно ли возвращать названия столбцов
        :return: если выборка - результат выборки, если изменение - айди изменной строки
        """
        if isinstance(queries, str):
            queries = (queries, )

        commit = False
        for query in queries:

            try:
                self._cursor.execute(query)

            except Exception as e:
                logger.error(f'Error in sql query - """{query}"""\n'
                             f'error - """{e}"""')
                return False

            else:
                logger.info(f'Make a query - """{query}"""')
                if re.search('INSERT|DELETE|UPDATE', query):
                    commit = True

        if commit:
            self._connect.commit()
            logger.info('Make a commit.')
            return self._cursor.lastrowid

        else:
            result: list = self._cursor.fetchall()

            if description:
                result.insert(0, tuple(x[0] for x in self._cursor.description))

            return result

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
            Для работы контекстногом менеджера with
        """
        self._cursor.close()
        self._connect.close()
        logger.info(f'Close DB connection')


class Database(_Database):
    """
        Пишу кастомные запросы к БД
    """
    def __init__(self):
        super().__init__()

