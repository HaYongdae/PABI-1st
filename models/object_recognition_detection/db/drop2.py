import pymysql

con = pymysql.connect(user='root', password='africa', db='team')

curs = con.cursor()

sql = "DROP TABLE RecoDate"
curs.execute(sql)
con.commit()


con.close()