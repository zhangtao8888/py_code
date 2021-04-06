import psycopg2
from redund.db import db
import pandas as pd
import redund.tools as tools
from contextlib import contextmanager

class sim_dao():

    def __init__(self):
        self._user_name = 'postgres'
        self._pass_word = '7733188'
        self._host = '127.0.0.1'
        self._database = 'dbtest'
        self._port = '5432'

    @contextmanager
    def conn(self):
        conn = db.get_connection(self)
        try:
            yield conn
            conn.commit()
        finally:
            try:
                conn.close()
            except Exception as e:
                print("%", e)

    @contextmanager
    def cur(self):
        conn = self.conn()
        cur = conn.cursor()
        try:
            yield cur
            cur.commmit()
        finally:
            try:
                cur.close()
                conn.close()
            except:
                print('error cur')

    def read_sql_query(self,sql : str = ''):
        with self.conn() as conn:
            return pd.read_sql_query(sql,conn)

    def p_report(self):
        sql1 = """select * from public.user_info"""
        df = self.read_sql_query(sql1)
        print(df)
        return df

