import pymysql

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='dome_test',   #选择连接哪个数据库
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()

#
sql = "update employee set first_name=%s where age=%s"


cursor.execute(sql,('haimianbaobao',20))
connect.commit()
cursor.close()
connect.close()