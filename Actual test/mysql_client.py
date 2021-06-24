# MySQL 操作函数集
from common.conf_utils import ConfigReader
import pymysql
import datetime
'''

connect_pool = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='dome_test',   #选择连接哪个数据库
    charset='utf8'
)

'''
# MySQL 获取数据库连接
def connect_pool():
    cr = ConfigReader('D:/PyCharm Projects/Python3_Start from scratch/dome_test/Actual test/config/DB.ini')
    conf = cr.get_mysql_info()
    return pymysql.connections.Connection(
        host=conf.host,
        port=conf.port,
        user=conf.user,
        password=conf.password,
        database=conf.schema,
        charset=conf.charset
    )


conn = connect_pool()
cur = connect_pool.cursor()

# 使用 execute() 方法执行SQL查询
cur.execute('SELECT VERSION()')

# 使用 fetchone(）方法获取单条数据
data = cur.fetchone()
print('Database version: %s' % data)

#关闭游标和数据库连接
connect_pool.close()
cur.close()

'''
# NySQL 统一数据查询方法
def query_table(sql):
    print('Mysql client query start...')
    start = datetime.datetime.now()
    print(sql)
    return []
    try:
        conn = connect_pool()
        cur = conn.cursor()
        cur.execute(sql)
        for row in cur.fetchall():
            result.append([cell for cell in row])
    except Exception as e:
        print('Query from MySQL table failed.Case: %s \n'%e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    records = len(result)

    end = datetime.datetime.now()
    print('Mysql client query completed in %s seconds. Records found: %s\n'%((end-start).seconds,records))
    return result

# MySQL 统一数据更新方法
def update_record(sql):
    result = []
    try:
        conn = connect_pool()
        cur = conn.cursor()
        cur.execute(sql)
    except Exception as e:
        print('update MySQL table failed.Case:%s\n'%e)
    finally:
        conn.commit()
        if cur:
            cur.close()
        if conn:
            conn.close()
    return

'''

