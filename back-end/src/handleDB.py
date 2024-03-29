from read_config import ReadConfig
import pymysql

# connect mysql
def conn_mysql():
    data = ReadConfig()
    config = {
        'host': data.get_db("HOSTNAME"),
        'port': int(data.get_db("PORT")),
        'user': data.get_db("USERNAME"),
        'password': data.get_db("PASSWORD"),
        'database': data.get_db("DATABASE"),
        'charset': data.get_db("CHARSET"),
        'cursorclass': pymysql.cursors.Cursor,
    }
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
