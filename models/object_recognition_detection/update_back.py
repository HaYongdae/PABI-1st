#-*- coding:utf-8 -*-
import pymysql
import datetime
import make_t
import object_detection_webcam
def print_update():
    ele =object_detection_webcam.odw()
    ele = odwdh
    ele = set(ele)
    ele = list(ele)
    numele =len(ele)
    con = pymysql.connect(user='root', password='12345678', db='teamp')

    curs = con.cursor()

    sql="select * from RecoDishes"
    curs.execute(sql)

    rows=curs.fetchall()
    rows=list(rows)
    rows.sort(key=lambda e:e[2], reverse=True)
    count = 1
    elels = []
    wls,fls,yls=make_t.mt(rows,ele,numele)
    con.commit()
    con.close()
    return rows,wls,fls,yls