import pymysql


con=pymysql.connect(user='root', password='12345678', db='teamp')

curs=con.cursor()

sql="CREATE TABLE RecoDate( Dishes VARCHAR(50),  Recodate DATE )"
curs.execute(sql)

con.close()