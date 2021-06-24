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

# 插入一条数据
sql = "insert into EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) values (%s,%s,%s,%s,%s)"
cursor.execute(sql,('Windows','Paidaxing',25,'S',5000))  # 括号内填写需要增加的数据，此方式为增加一条数据
print(cursor.lastrowid) # 获取最后一行的ID值
connect.commit()  # 对数据的增删改一定要提交，否则更改不成功，而且主键id还会增加，pycharm还不会报错，很坑壁

# 输入多条件数据
data = [('A','a','30','A','6000'),('B','b','40','B','7000'),('C','c','50','C','8000')]
sql = "insert into EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) values (%s,%s,%s,%s,%s)"
cursor.executemany(sql,data)
print(cursor.lastrowid)#获取最后一行的ID值,只是将原来的最后一行id加一，
# 如果一次插入多行，并不能正确显示主键最后一行的id
connect.commit()

cursor.close()
connect.close()