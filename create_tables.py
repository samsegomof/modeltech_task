from DB import Database


def create_rates():
    """Функция создания таблицы rates"""
    db_connect = Database('well_data_db')
    query = '''
                CREATE TABLE IF NOT EXISTS rates (
                dt DATETIME,
                well_id INTEGER,
                oil_rate FLOAT,
                gas_rate FLOAT,
                water_rate FLOAT    
                )
    '''
    return db_connect.get_query_result(query)


def create_splits():
    """Функция создания таблицы splits"""
    db_connect = Database('well_data_db')
    query = '''
                CREATE TABLE IF NOT EXISTS splits (
                dt DATETIME,
                well_id INTEGER,
                layer_id INTEGER,
                oil_split FLOAT,
                gas_split FLOAT,
                water_split FLOAT
                )
    '''
    return db_connect.get_query_result(query)


def create_invalid_splits():
    """Функция создания таблицы invalid_splits"""
    db_connect = Database('well_data_db')
    query = '''
                CREATE TABLE IF NOT EXISTS invalid_splits (
                dt DATETIME,
                well_id INTEGER,
                layer_id INTEGER,
                oil_split FLOAT,
                gas_split FLOAT,
                water_split FLOAT
                )
    '''

    return db_connect.get_query_result(query)


def create_invalid_totals():
    """Функция создания таблицы invalid totals"""
    db_connect = Database('well_data_db')
    query = '''CREATE TABLE IF NOT EXISTS invalid_totals (
                        dt DATETIME,
                        well_id INTEGER,
                        total_oil_split FLOAT,
                        total_gas_split FLOAT,
                        total_water_split FLOAT
                        )
                        '''
    return db_connect.get_query_result(query)


def create_rate_split():
    """Функция создания таблицы rate_split"""
    db_connect = Database('well_data_db')
    query = '''CREATE TABLE IF NOT EXISTS rate_split(
                    dt DATETIME,
                    well_id INTEGER,
                    layer_id INTEGER,
                    oil_rate_split FLOAT,
                    gas_rate_split FLOAT,
                    water_rate_split FLOAT
                    )'''

    return db_connect.cur.execute(query)


if __name__ == '__main__':
    create_rates()
    create_splits()
    create_invalid_splits()
    create_invalid_totals()
    create_rate_split()
