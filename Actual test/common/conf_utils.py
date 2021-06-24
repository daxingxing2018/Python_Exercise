# 读取配置文件
from DB_tuples import MySQL
import configparser


class ConfigReader:
    # path为配置文件的完整路径，由调用者传入
    def __init__(self, path):
        if path is None or len(path) < 1:
            raise ValueError('The config ini file path required.')
        else:
            self.conf = configparser.ConfigParser()
            self.conf.read(path)

    # 取得MySQL服务连接信息，返回MySQL（host,user.password,port,charset,schema）
    def get_mysql_info(self):
        host = self.conf.get('MySQL', 'host')
        user = self.conf.get('MySQL', 'user')
        password = self.conf.get('MySQL', 'password')
        port = self.conf.get('MySQL', 'port')
        schema = self.conf.get('MySQL', 'schema')
        charset = self.conf.get('MySQL', 'charset')

        return MySQL(host,user,password,int(port),charset,schema)
