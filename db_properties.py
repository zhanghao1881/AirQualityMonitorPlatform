#coding:utf-8


class DbParam:
    def __init__(self, host='localhost', user='test', password='wangbo1012',database='django_data'):
        #端口号
        self.host =host
        #用户名
        self.user =user
        #密码
        self.password =password
        #数据库
        self.database =database

db_param = DbParam()