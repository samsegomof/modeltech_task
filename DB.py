import sqlite3


class Database:
    """Класс для работы с БД"""
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

    def get_query_result(self, query):
        """Функция, извлекающая запросы"""
        if 'INSERT' in query:
            # Добавление в БД
            self.cur.execute(query)
            self.con.commit()

        return self.cur.execute(query)

    def __enter__(self):
        """Открыть подключение с БД"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Закрыть подключение"""
        self.cur.close()
        self.con.close()
        if exc_val:
            raise "Error, check database settings."
