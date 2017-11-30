import pymysql
import datetime


con=pymysql.connect(user='root', password='12345678', db='teamp')

curs=con.cursor()

d=datetime.date(2017,9,1)
d2=datetime.date(2017,8,3)
d3=datetime.date(2017,6,7)
d4=datetime.date(2017,9,1)
d5=datetime.date(2017,9,1)
d6=datetime.date(2017,9,1)
d7=datetime.date(2017,8,2)
d8=datetime.date(2017,10,2)
i3 = ('egg',)
i4 = ('orange',)
i5 = ('corn',)
i6 = ('paprica',)
i7 = ('tomato',)
data=(
      (('pork',),'samgyepsal',0,d2,345),
      (('chicken',),'roasted_chicken', 0, d3,453),
      ('beef','steak', 0, d4, 649),
      ('apple','applepie', 0, d5, 100),
      ('tomato', 'tomato_spaghetti', 0, d8, 433),
      (str(i3),'Sausage Egg Casserole',0,d,50),
      (str(i3),'Egg Noodles',0,d,550),
      (str(i6),'salad',0,d,120),
      (str(i4),'Orange Pork Carnitas',0,d,210),
      (str(i5),'Shoepeg Corn Salad',0,d,540),
      (str(i4),'Orange Tilapia',3,d,54),
      (str(i4),'Orange Turkey ',2,d3,555),
      (str(i5),'Mexican Grilled Corn',5,d4,444),
      (str(i5),'Elote Grilled Corn',0,d6,331),
      (str(i6),'paprica',0,d4,48),
      (str(i7),'sweet tomato',0,d2,147)
      )
sql="insert into RecoDishes values (%s, %s, %s, %s, %s)"

curs.executemany(sql,data)
con.commit()

con.close()