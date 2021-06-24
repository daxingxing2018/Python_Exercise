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
sql = "delete from employee where AGE=%s and income=%s"
cursor.execute(sql,(25,5000))  #这里的数据元组里面只有一个元素时不加逗号也可以正常删除，但是最好加上

sql = "delete from employee where AGE=%s or income=%s or income=%s or income=%s"
cursor.execute(sql,(25,6000,7000,8000))

connect.commit()
cursor.close()
connect.close()