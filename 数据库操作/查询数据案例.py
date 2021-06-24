import pymysql

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='dome_test',   #选择连接哪个数据库
    charset='utf8')
# 获取游标
cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)

# cursor.execute("select AGE from EMPLOYEE where INCOME > %s" % (1000))
cursor.execute("select * from EMPLOYEE")
data1 = cursor.fetchone()
print(data1)

cursor.execute("select * from EMPLOYEE")
data = cursor.fetchall()
print(data)
'''
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % (fname, lname, age, sex, income ))

except:
   print ("Error: unable to fetch data")
'''


# 关闭游标和数据库连接
cursor.close()
connect.close()