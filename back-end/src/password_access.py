import handleDB
import password_encryption
import base64



def modify_password(password):
    update_password = password_encryption.encrypt_password(password)
    sql_modify = "UPDATE user SET password='%s' WHERE username='%s'" % (
    str(base64.b64encode(update_password).decode()), "admin")
    conn,cur = handleDB.execute_mysql(sql_modify)
    cur.close()
    conn.close()


# insert modified password into mysql
def insert_password(username, password):
    update_password = password_encryption.encrypt_password(password)
    sql_insert = "INSERT INTO user(username,password,role)VALUES('%s','%s','%s')" % (
        username, str(base64.b64encode(update_password).decode()), "admin")
    conn,cur = handleDB.execute_mysql(sql_insert)
    cur.close()
    conn.close()


# password comparison
def password_deposit(username, password):
    sql_search = "SELECT password FROM user WHERE username = '%s';" % (username)
    count, result,conn= handleDB.find_mysql(sql_search)
    sto_password = base64.b64decode(result)
    vali_password = password_encryption.validate_password(sto_password, password)
    conn.close()
    return vali_password


if __name__ == '__main__':
    # password_deposit('zhmingyu','zhangmingyu')

    password_deposit('admin', 'cccc')
