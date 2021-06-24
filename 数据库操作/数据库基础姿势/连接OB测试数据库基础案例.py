import pymysql

# 连接数据库
connect = pymysql.Connect(
    host='db-policy.cbazirqvyxn8.us-east-2.rds.amazonaws.com',
    port=3306,
    user='test',
    passwd='o123456',
    db='db_ad_policy_dev',   #选择连接哪个数据库
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










'''

# SQL插入语句。查询数据；db_ad_policy_dev.ad_region.iso_codes 中 db_ad_policy_dev是数据库，ad_region是表，iso_codes是字段
sql = 'SELECT db_ad_policy_dev.ad_region.iso_codes FROM db_ad_policy_dev.ad_region WHERE name = "欧盟"'
try:
    #执行sql语句
    cursor.execute(sql)

except:
    #如果发生错误则回滚
    connect.rollback()

#提交对数据库的修改
conn.commit()

'''

