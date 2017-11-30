import pymysql


con=pymysql.connect(user='root', password='12345678', db='teamp')

curs=con.cursor()

sql="CREATE TABLE RecoDishes (Elements VARCHAR(30), Dishes VARCHAR(50), Counts int(30), Recodate DATE, kcal int(30))"
curs.execute(sql)

con.close()