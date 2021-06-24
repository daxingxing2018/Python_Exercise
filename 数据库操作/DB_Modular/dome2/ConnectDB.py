import pymysql

def connect_mysql():

    db_config = {
        'host':'localhost',
        'port':3306,
        'user':'root',
        'passwd':'123456',
        'db':'dome_test',
        'charset':'utf8'
    }

    conn = pymysql.connect(**db_config)

    return conn
    cursor = connect_mysql.conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from EMPLOYEE")
    data = cursor.fetchall()
    print(data)

# 注意：端口不能加引号，因为port接受的数据类型为整型
# 注意：charset的字符集不是utf-8，是utf8