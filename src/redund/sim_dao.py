import psycopg2
from redund.db import db
import pandas as pd
import redund.tools as tools
from contextlib import contextmanager
from flask import request
import json

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
        conn = db.get_connection(self)
        cur = conn.cursor()
        try:
            yield cur
            conn.commit()
        finally:
            try:
                cur.close()
                conn.close()
            except:
                print('error cur')

    def read_sql_query(self,sql : str = ''):
        with self.conn() as conn:
            return pd.read_sql_query(sql,conn)

    def execute(self,sql : str = ''):
        with self.cur() as cur:
            return cur.execute(sql)

    def execute_many(self,sql : str = '' ,rows : list= []):
        with self.cur() as cur:
            return cur.executemany(sql,rows)

    def p_report(self):
        sql1 = """select * from public.user_info"""
        df = self.read_sql_query(sql1)
        print(df)
        return df

    def p_exe(self):
        sql1 = """select * from public.user_info"""
        df = self.read_sql_query(sql1)
        # column_list = df.columns.values.tolist()
        # rows = [tuple(x) for x in df.values]


        # print(df.index)
        for i in df.index:
            # print(df.loc[i,'json_info'])
            json_info = df.loc[i, 'json_info']
            # json_info.replace('[','')
            json_str = json.dumps(json_info)
            print(json_str)

            # json_str2 =
        # column_str = "("
        #
        # for column in column_list:
        #     print(column)
        #     column_str += column+","
        # column_str = column_str[:-1]+")"
        # # "'{user_id}','J')"""
        # value_str = " values ("
        # for i in range(len(column_list)):
        #     value_str += "%s" +","
        # value_str = value_str[:-1] + ")"
        # sql2 = "insert into public.user_info" +column_str + value_str
        # para = request.json
        # user_id = para.get("user_id")[0]
        #
        # user_name = para.get("user_name")
        # sql1 = """insert into public.user_info(user_id,user_name) values ('{user_id}','k')""".replace('{user_id}',user_id)
        # try:
        #     self.execute_many(sql2,rows)
        # except Exception as e:
        #     print( e)
        # return co

    def p_json(self):
        sql1 = """select * from public.user_info"""
        df = self.read_sql_query(sql1)
        df.columns = df.columns.map(lambda x : x.lower())
        # column_list = df.columns.values.tolist()
        # rows = [tuple(x) for x in df.values]
        print(df.columns)

        # print(df.index)
        for i in df.index:
            # print(df.loc[i,'json_info'])
            json_info = df.loc[i, 'json_info']
            # json_info.replace('[','')     xfcv
            json_str = json.dumps(json_info)
            print(json_str)

            # json_str2 =
