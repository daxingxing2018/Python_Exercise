import pymysql

# 打开数据库连接
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='dome_test',   #选择连接哪个数据库
    charset='utf8'
)

# 使用cursor()方法获取操作游标
cursor = connect.cursor()

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
      ('Windows','Paidaxing',25,'S',4000)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    connect.commit()
except:
    # 发生错误时回滚
    connect.rollback()

# 关闭游标和数据库连接
cursor.close()
connect.close()