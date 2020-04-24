#coding:utf-8
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import MySQLdb
import os
import sys
sys.path.append("..")
from db_properties import db_param




class Plot(object):
    class CityData(object):
        def __init__(self):
            self.name = None
            self.time = []
            self.aqi = []
            self.pm25 = []
            self.pm10 = []
            self.co = []
            self.no2 = []
            self.o3 = []
            self.so2 = []

    def __init__(self, host=db_param.host, user=db_param.user,
                 pwd=db_param.password, database=db_param.database):
        self._host = host
        self._user = user
        self._pwd = pwd
        self._database = database
        self._db = None

    def _open_db(self):
        self._db = MySQLdb.connect(self._host, self._user, self._pwd,
                                   self._database, charset='utf8')

    def _close_db(self):
        self._db.close()

    def plot_single(self, city_id):

        self._open_db()
        _cursor = self._db.cursor()
        city_data = []
        for id in city_id:
            city = self.CityData()
            sql_cmd = f"SELECT city_name from weathersystem_city where id={id}"
            _cursor.execute(sql_cmd)
            name = _cursor.fetchall()[0][0]
            city.name = name
            sql_cmd = f"SELECT * from recent_items where city_name='{name}'"
            _cursor.execute(sql_cmd)
            _ret = _cursor.fetchall()
            for row in _ret:
                city.time.append(row[8])
                city.aqi.append(row[1])
                city.pm25.append(row[2])
                city.pm10.append(row[3])
                city.co.append(row[4])
                city.no2.append(row[5])
                city.o3.append(row[6])
                city.so2.append(row[7])
            city_data.append(city)
        self._close_db()
        city_list = list(map(lambda x: x.name, city_data))
        city_time = list(map(lambda x: x.time, city_data))
        city_aqi = list(map(lambda x: x.aqi, city_data))
        city_pm25 = list(map(lambda x: x.pm25, city_data))
        city_pm10 = list(map(lambda x: x.pm10, city_data))
        city_co = list(map(lambda x: x.co, city_data))
        city_o3 = list(map(lambda x: x.o3, city_data))
        city_so2 = list(map(lambda x: x.so2, city_data))
        city_no2 = list(map(lambda x: x.no2, city_data))

        self.draw(city_list,   city_time, city_aqi , "aqi"  )
        self.draw(city_list,   city_time, city_pm25, "pm25" )
        self.draw(city_list,   city_time, city_pm10, "pm10" )
        self.draw(city_list,   city_time, city_co  , "co"   )
        self.draw(city_list,   city_time, city_o3  , "o3"   )
        self.draw(city_list,   city_time, city_so2 , "so2"  )
        self.draw(city_list,   city_time, city_no2 , "no2"  )

    def draw(self, city_name, x, y, targe):
        plt.figure(num=3, figsize=(6, 3),)
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        plt.plot(x[0], y[0], color='green', linewidth=1.0, linestyle='-', label=city_name[0])
        plt.plot(x[1], y[1], color='red', linewidth=1.0, linestyle='-', label=city_name[1])
        plt.plot(x[2], y[2], color='blue', linewidth=1.0, linestyle='-', label=city_name[2])
        plt.plot(x[3], y[3], color='purple', linewidth=1.0, linestyle='-', label=city_name[3])
        #设置坐标轴与图例等
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        plt.gcf().autofmt_xdate()
        plt.xlabel("时间")
        plt.xticks(x[0])
        plt.ylabel(f"{targe}含量")
        plt.title(f"{targe} 城市对比图")
        plt.legend(loc='upper right', fontsize='x-small')
        #保存
        plt.savefig(f'{os.path.dirname(os.getcwd())}/DjangoProject/static/img/{targe}.png')
        plt.close('all')


    def plot(self, city_name):
        self._open_db()
        _cursor = self._db.cursor()
        sql_cmd = f"SELECT * from recent_items where city_name='{city_name}'"
        print(sql_cmd)
        _cursor.execute(sql_cmd)
        _ret = _cursor.fetchall()
        x = []
        y_aqi = []
        y_pm25 = []
        y_pm10 = []
        y_co = []
        y_no2 = []
        y_o3 = []
        y_so2 = []
        city_id = []
        if len(_ret) == 0:
            print(_ret)
            return False
        #保存选择城市近期数据
        for row in _ret:
            x.append(row[8])
            y_aqi.append(row[1])
            y_pm25.append(row[2])
            y_pm10.append(row[3])
            y_co.append(row[4])
            y_no2.append(row[5])
            y_o3.append(row[6])
            y_so2.append(row[7])
            city_id.append(row[9])
        self._close_db()
        #画图
        plt.figure(num=3, figsize=(10, 5),)
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        plt.plot(x,y_aqi, color='green', linewidth=1.0, linestyle='-',label='AQI')
        plt.plot(x,y_pm25, color='purple', linewidth=1.0, linestyle='-',label='PM2.5')
        plt.plot(x,y_pm10, color='black', linewidth=1.0, linestyle='-',label='PM10')
        plt.plot(x,y_co, color='blue', linewidth=1.0, linestyle='-',label='CO')
        plt.plot(x,y_no2, color='red', linewidth=1.0, linestyle='-',label='NO2')
        plt.plot(x,y_o3, color='pink', linewidth=1.0, linestyle='-',label='O3')
        plt.plot(x,y_so2, color='orange', linewidth=1.0, linestyle='-',label='SO2')
        #设置坐标轴与图例等
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        plt.gcf().autofmt_xdate()
        plt.xlabel("时间")
        plt.xticks(x)
        plt.ylabel("空气质量指数")
        plt.title(city_name+"历史空气质量")
        plt.legend(loc='upper right', fontsize='x-small')
        #保存
        plt.savefig(f'{os.path.dirname(os.getcwd())}/DjangoProject/static/img/'+str(city_id[0])+'.png')
        plt.close('all')
        return True

    def plot_all(self):
        self._open_db()
        _cursor = self._db.cursor()
        sql = "SELECT city_name from WeatherSystem_city"
        _cursor.execute(sql)
        results = _cursor.fetchall()
        city_name_list = []
        # 获取全部城市名称
        for row in results:
            city_name_list.append(row[0])
        self._close_db()
        # 对全部城市绘制空气质量曲线
        for city_name in city_name_list:
            if not self.plot(city_name):
                break
