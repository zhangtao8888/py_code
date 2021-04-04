import psycopg2

class sim_dao():
    def __init__(self):
        self.user_name = 'user_name'
        self.pass_word = 'pass_word'
        self.url = ''
    def p_report(self):
        conn = psycopg2.connect(database="dbtest",user="postgres",password="7733188",host="127.0.0.1")
        cursor = conn.cursor()
        cursor.execute("select * from public.user_info")
        rows = cursor.fetchall()
        for row in rows :
            print('id=',row[0],' name=',row[1],'\n')
            cursor.close
            conn.close