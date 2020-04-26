# Air Quality Monitor Platform
### 基于 Django + Scrapy 框架实现的空气质量监测系统
An air quality monitor platform based on Django frame. Related data are crawled by Scrapy on [PM25](https://www.tianqi.com/air/)  



## 环境

### 要求

* Environment：Anaconda3 (x86) python3.7 version

* Django：3.0.3 以及其上
* [MySQL](https://www.mysql.com/)： 5.6 及其以上
* Scarpy： 2.0.1及其以上

### 配置

#### PyCharm

1. 使用**PyCharm**打开项目，随后通过进入 `File` -> `settings` -> `Project Interpreter` ，点击小齿轮添加`Conda Environment` 构建项目虚拟环境。
2. 等待环境初始化完成后，在**Terminal**键入 `pip install -r requirements.txt` 命令完成依赖配置。

#### MySQL

1. 通过**MySQL Installer** 安装**MySQL 5.6** 或更高版本，并创建一个名为**django_data**的数据库。
2. 通过**Navicat**连接该数据库，并创建一用户。
   * 用户名：test
   * 密码：wangbo1012

### 初始化  



### 运行

* 本项目目录下，**Terminal** 执行命令 `python runserver.py` 启动Web服务器。打开浏览器访问 *http://localhost:8000/WeatherSystem* 即可打开 Web 页面。  
* 本项目目录下，**Terminal** 执行命令 `python capturedata.py` 启动爬虫爬取空气质量数据，时间间隔1h 

### Powered by [AlbertoWang](https://github.com/AlbertoWang) and  [ShaneCN](https://github.com/ShaneCN)

##### 免责声明 : 本项目仅供学习交流使用,项目内相关网站爬虫使用请遵守相关法律法规,若产生纠纷或问题,本 Repo 作者不承担一切责任。
##### Disclaimer : This project is only for learning and communication. Please use the website crawlers in the project under complying with relevant laws and regulations. In case of disputes or problems, the author of this Repo is not responsible for them all.
