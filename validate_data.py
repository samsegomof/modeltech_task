import sqlite3
import prettytable

con = sqlite3.connect('well_data_db')
cur = con.cursor()
query = '''SELECT * FROM invalid_splits'''


def show_invalid_splits(sqlite_query):
    """Функция вывода на экран сплитов меньше 100"""
    cur.execute(sqlite_query)
    task_query = ''' 
                    SELECT dt as Дата, well_id as Скважина, 
                    SUM(oil_split) as Итого_нефти,
                    SUM(gas_split)as Итого_газа, 
                    SUM(water_split) as Итого_воды
                    FROM invalid_splits 
                    GROUP BY dt, well_id
                    HAVING 
                        sum(oil_split) < 100 or 
                        sum(gas_split) < 100 or 
                        sum(water_split) < 100;
             '''
    result = cur.execute(task_query)
    pretty_table = prettytable.from_db_cursor(result)
    pretty_table.max_width = 30
    print(pretty_table)


if __name__ == '__main__':
    show_invalid_splits(query)
