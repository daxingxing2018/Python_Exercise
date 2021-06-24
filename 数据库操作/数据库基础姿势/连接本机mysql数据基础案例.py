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

# 使用 execute() 方法执行SQL查询
cursor.execute('SELECT VERSION()')

# 使用 fetchone(）方法获取单条数据
data = cursor.fetchone()
print('Database version: %s' % data)

#关闭游标和数据库连接
cursor.close()
connect.close()