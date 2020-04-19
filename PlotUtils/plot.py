#coding:utf-8
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import MySQLdb
import os
import sys
sys.path.append("..")
from db_properties import db_param

def plot(city_name):
    #中文字体 MacOS可用，WIN自行更改
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    #连接数据库并获取数据
    db = MySQLdb.connect(db_param.host, db_param.user, db_param.password, db_param.database, charset='utf8' )
    cursor = db.cursor()
    sql = f"SELECT * from recent_items where city_name='{city_name}'"
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    x = []
    y_aqi = []
    y_pm25 = []
    y_pm10 = []
    y_co = []
    y_no2 = []
    y_o3 = []
    y_so2 = []
    city_id = []
    if len(results) == 0:
        print(results)
        return False
    #保存选择城市近期数据
    for row in results:
        x.append(row[8])
        y_aqi.append(row[1])
        y_pm25.append(row[2])
        y_pm10.append(row[3])
        y_co.append(row[4])
        y_no2.append(row[5])
        y_o3.append(row[6])
        y_so2.append(row[7])
        city_id.append(row[9])
    db.close()
    #画图
    plt.figure(num=3, figsize=(20, 10),)
    plt.plot(x,y_aqi, color='green', linewidth=1.0, linestyle='-',label='AQI')
    plt.plot(x,y_pm25, color='purple', linewidth=1.0, linestyle='-',label='PM2.5')
    plt.plot(x,y_pm10, color='black', linewidth=1.0, linestyle='-',label='PM10')
    plt.plot(x,y_co, color='blue', linewidth=1.0, linestyle='-',label='CO')
    plt.plot(x,y_no2, color='red', linewidth=1.0, linestyle='-',label='NO2')
    plt.plot(x,y_o3, color='pink', linewidth=1.0, linestyle='-',label='O3')
    plt.plot(x,y_so2, color='orange', linewidth=1.0, linestyle='-',label='SO2')
    #设置坐标轴与图例等
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gcf().autofmt_xdate()
    plt.xlabel("时间")
    plt.xticks(x)
    plt.ylabel("空气质量指数")
    plt.title(city_name+"历史空气质量")
    plt.legend(loc=1)
    #保存
    plt.savefig('DjangoProject/static/img/'+str(city_id[0])+'.png')
    plt.close('all')
    return True

def plotAll():
    #连接数据库
    db = MySQLdb.connect(db_param.host, db_param.user, db_param.password, db_param.database, charset='utf8' )
    cursor = db.cursor()
    sql = "SELECT city_name from WeatherSystem_city"
    cursor.execute(sql)
    results = cursor.fetchall()
    city_name_list = []
    #获取全部城市名称
    for row in results:
        city_name_list.append(row[0])
    db.close()
    #对全部城市绘制空气质量曲线
    os.chdir('..')
    for city_name in city_name_list:
        if not plot(city_name):
            break

plotAll()