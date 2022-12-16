import openpyxl
import json
from datetime import datetime

from DB import Database


def calculate_and_add_allocations():
    """Функция расчета аллокаций и добавления в БД"""
    db_connect = Database('well_data_db')
    query = '''     INSERT INTO rate_split
                    SELECT splits.dt, splits.well_id, splits.layer_id,
                    splits.oil_split*rates.oil_rate/100 as oil_rate_split,
                    splits.gas_split*rates.gas_rate/100 as gas_rate_split,
                    splits.water_split*rates.water_rate/100 as water_rate_split
                    FROM splits
                    JOIN rates ON rates.well_id=splits.well_id AND rates.dt=splits.dt'''

    return db_connect.get_query_result(query)


def to_xlsx_rate_split():
    """Функция конвертер из БД в xlsx"""
    db_connect = Database('well_data_db')
    book = openpyxl.Workbook()
    sheet = book.active
    query = '''SELECT * FROM rate_split'''
    db_connect.get_query_result(query)
    result = db_connect.cur.fetchall()
    i = 0
    for row in result:
        i += 1
        j = 1
        for col in row:
            cell = sheet.cell(row=i, column=j)
            cell.value = col
            j += 1

    return book.save('rate_split.xlsx')


def table_to_json():
    """Функция форматирования данных из таблицы rate_split в JSON файл"""
    db_connect = Database('well_data_db')
    query = '''SELECT * FROM rate_split'''
    data = db_connect.get_query_result(query).fetchall()
    res = {'allocation': {'data': []}}
    for obj in data:
        res['allocation']['data'].append(
            {
                        'wellId': obj[1],
                        'dt': datetime.strptime(obj[0], '%Y-%m-%d').isoformat(),
                        'layerId': obj[2],
                        'oilRate': obj[3],
                        'gasRate': obj[4],
                        'waterRate': obj[5]
                    }
        )

    with open("rate_split.json", "w") as file:
        json.dump(res, file)


if __name__ == '__main__':
    calculate_and_add_allocations()
    to_xlsx_rate_split()
    table_to_json()
