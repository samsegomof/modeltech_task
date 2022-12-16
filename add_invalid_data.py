from DB import Database


def add_invalid_totals():
    db_connect = Database('well_data_db')

    query = '''
                    INSERT INTO invalid_totals
                    SELECT dt, well_id,
                    SUM(oil_split) as total_oil_split,
                    SUM(gas_split)as total_gas_split, 
                    SUM(water_split) as total_water_split
                    FROM invalid_splits 
                    GROUP BY dt, well_id
                    HAVING 
                        sum(oil_split) < 100 or 
                        sum(gas_split) < 100 or 
                        sum(water_split) < 100;
                '''
    return db_connect.get_query_result(query)


if __name__ == '__main__':
    add_invalid_totals()
