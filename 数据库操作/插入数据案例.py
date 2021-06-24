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

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Windows','Paidaxing',25,'S',4000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   connect.commit()
except:
   # 如果发生错误则回滚
   connect.rollback()

#关闭游标和数据库连接
cursor.close()
connect.close()