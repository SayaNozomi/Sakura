import pymysql

f = open("sakura.jpg", 'rb')
data = f.read()
print(data)

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='saya',
                     database='favorite')

cursor = db.cursor()

sql = "update wife set photo=%s where name='Sakura';"

cursor.execute(sql, data)

try:
    db.commit()
except:
    db.rollback()
    print("error")
