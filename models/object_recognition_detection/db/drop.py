import pymysql

con = pymysql.connect(user='root', password='12345678', db='teamp')

curs = con.cursor()

sql = "DROP TABLE RecoDishes "
curs.execute(sql)
con.commit()


con.close()