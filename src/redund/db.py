import psycopg2
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy as _SQLALchemy

class db(_SQLALchemy):
    # conn = psycopg2.connect(database="dbtest", user="postgres", password="7733188", host="127.0.0.1")

    def __init__(self):
        self._user_name = 'postgres'
        self._pass_word = '7733188'
        self._host = '127.0.0.1'
        self._database = 'dbtest'
        self._port = '5432'

    # @contextmanager
    def get_connection(self):
        try:
            conn = psycopg2.connect(database=self._database, user=self._user_name, password=self._pass_word,
                                    host=self._host,port = self._port)
        except:
            try:
                conn.close()
            except Exception as e:
                print("%" ,e)
        return conn




