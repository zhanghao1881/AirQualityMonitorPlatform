import MySQLdb


def get_city_eng(param):
    db = MySQLdb.connect(param.host, param.user, param.password, param.database, charset='utf8' )
    cursor = db.cursor()
    sql = "SELECT city_name_eng from WeatherSystem_city"
    cursor.execute(sql)
    results = cursor.fetchall()
    result = []
    for row in results:
        result.append(row[0])
    db.close()
    return result


def get_city_name(param, eng):
    db = MySQLdb.connect(param.host, param.user, param.password, param.database, charset='utf8')
    cursor = db.cursor()
    sql = f"SELECT city_name from WeatherSystem_city where city_name_eng='{eng}'"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    db.close()
    return result


if __name__ == '__main__':
    from db_properties import db_param
    ret = get_city_name(db_param, "hongkong")
    print(ret)