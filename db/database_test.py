import pymysql
from pymysql.cursors import DictCursor

class DATABASE:
    def __init__(self, host='192.168.88.6', port=3306, user='skysys', password='tmzkdl11@!', db='test', charset='utf8mb4'):
        self.db_config = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'db': db,
            'charset': charset,
            'cursorclass': DictCursor,
            'autocommit': False,
        }

    def _get_connection(self):
        return pymysql.connect(**self.db_config)

    def execute(self, sql, params=None, return_rowcount=False):
        print(f'----------------------- SQL:\n{sql}')
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    print(f'----------------------- EXECUTE SQL:\n{sql}')
                    print(f'----------------------- PARAMS:\n{params}')
                    cursor.execute(sql, params)
                    conn.commit()
                    if return_rowcount:
                        return cursor.rowcount
                    else:
                        return cursor.lastrowid
        except Exception as e:
            print(f'-- EXECUTE ERROR: {e}')
            try:
                conn.rollback()
            except:
                pass
            raise


    def fetch_all(self, sql, params=None):
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    # print(f'----------------------- FETCH ALL SQL:\n{sql}')
                    # print(f'----------------------- PARAMS:\n{params}')
                    cursor.execute(sql, params)
                    return cursor.fetchall()
        except Exception as e:
            print(f'----------------------- FETCH ALL ERROR: {e}')
            raise
