import pymysql
import password_encryption
import base64


# 连接数据库
def conn_mysql():
    config = {
        'host': '10.117.43.99',
        'port': 3306,
        'user': 'zwx',
        'password': '123456',
        'database': 'doctorjoe',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.Cursor,
    }
    connection = pymysql.connect(**config)
    cur = connection.cursor()
    return connection, cur


# 执行数据库
def execute_mysql(sql):
    conn, cur = conn_mysql()
    cur.execute(sql)
    conn.commit()
    return conn


# 查询数据库
def find_mysql(sql):
    conn, cur = conn_mysql()
    count = cur.execute(sql)
    conn.commit()
    if count > 0:
        return count, cur.fetchall()[0][0], conn
    else:
        return count, "", conn


# 修改admin密码
def modify_password(password):
    update_password = password_encryption.encrypt_password(password)
    sql_modify = "UPDATE user SET password='%s' WHERE username='%s'" % (
    str(base64.b64encode(update_password).decode()), "admin")
    conn = execute_mysql(sql_modify)
    conn.close()


# 配置密码插入数据库
def insert_password(username, password):
    update_password = password_encryption.encrypt_password(password)
    sql_insert = "INSERT INTO user(username,password,role)VALUES('%s','%s','%s')" % (
    username, str(base64.b64encode(update_password).decode()), "admin")
    conn = execute_mysql(sql_insert)
    conn.close()


# 密码对比
def password_deposit(username, password):
    sql_search = "SELECT password FROM user WHERE username = '%s';" % (username)
    count, result, conn = find_mysql(sql_search)
    sto_password = base64.b64decode(result)
    vali_password = password_encryption.validate_password(sto_password, password)
    print(result)
    conn.close()
    return vali_password


if __name__ == '__main__':
    # password_deposit('zhmingyu','zhangmingyu')
    modify_password('cccc')
    password_deposit('admin', 'cccc')
