import configparser

# 实例化 configparser 对象
config = configparser.ConfigParser()

# 使用 read() 读取ini文件
#file = config.read('D:/PyCharm Projects/Python3_Start from scratch/dome_test/Actual test/config/DB.ini')
file = config.read('D:\\PyCharm Projects\\Python3_Start from scratch\\dome_test\\Actual test\\config\\DB.ini')


#print(file)
#print(type(file))  # 这里read返回的是文件所在路径组成的列表，输出的格式是class

# 使用 sections() 得到所有的section，并以列表的形式返回
print('sections:','',config.sections())   # 这里输出的是所有sections的标题内容，即使ini中[]里的内容

# 使用 options() 得到指定section下的所有option（即key）
print('options:','',config.options('MySQL'))

# 使用 items() 得到该section下所有的键值对（key,value）
print('items:' ,' ' ,config.items('MySQL'))

# 使用 get() 得到指定section下指定option的值
getfile = config.get('MySQL', 'host')
print('get:' ,' ' , getfile)
print(type(getfile))

# 使用 config.getint() 得到指定section下指定option的值，并指定返回的类型
print('getint:' ,' ' ,config.getint('MySQL', 'password'))   #  得到指定section下指定option的值，返回值为int类型
#print('getfloat:' ,' ' , config.getfloat('MySQL', 'weight'))  #  得到指定section下指定option的值，返回值为float类型
#print('getboolean:' ,'  ', config.getboolean('MySQL', 'isChoice'))  #  得到指定section下指定option的值，返回值为boolean类型

# 判断是否有section
print('getint:' ,' ' ,config.has_section('MySQL'))
# 判断如果section和option都存在则返回True否则False
print('getint:' ,' ' ,config.has_option('MySQL','ALG'))

