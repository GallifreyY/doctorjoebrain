from read_config import ReadConfig
import pymysql

# connect mysql
def conn_mysql():
    config = {
            'host': 'dj-mysql',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': 'doctorjoe',
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.Cursor,
        }
    # data = ReadConfig()
    # config = {
    #     'host': data.get_db("host"),
    #     'port': int(data.get_db("port")),
    #     'user': data.get_db("user"),
    #     'password': data.get_db("password"),
    #     'database': data.get_db("database"),
    #     'charset': data.get_db("charset"),
    #     'cursorclass': pymysql.cursors.Cursor,
    # }
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    return conn,cur


# execute mysql
def execute_mysql(sql):
   conn,cur = conn_mysql()
   cur.execute(sql)
   conn.commit()
   return conn,cur


# select mysql
def find_mysql(sql):
    conn,cur = conn_mysql()
    count = cur.execute(sql)
    if count > 0:
        return count, cur.fetchall()[0][0],conn
    else:
        return count,"",conn



if __name__ == '__main__':
    sql = "select * from user"
    print(find_mysql(sql))
