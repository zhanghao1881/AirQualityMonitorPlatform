import MySQLdb


def get_city_eng(host, user, password, database):
    db = MySQLdb.connect(host, user, password, database, charset='utf8' )
    cursor = db.cursor()
    sql = "SELECT city_name_eng from WeatherSystem_city"
    cursor.execute(sql)
    results = cursor.fetchall()
    result = []
    for row in results:
        result.append(row[0])
    db.close()
    return result


def get_city_name(host, user, password, database, eng):
    db = MySQLdb.connect(host, user, password, database, charset='utf8')
    cursor = db.cursor()
    sql = f"SELECT city_name from WeatherSystem_city where city_name_eng='{eng}'"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    db.close()
    return result

if __name__ == '__main__':
    import db_properties
    ret = get_city_name(db_properties.HOST, db_properties.USER, db_properties.PASSWORD, db_properties.DATABASE, "hongkong")
    print(ret)