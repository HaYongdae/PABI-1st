import threading
from threading import Timer
import Tkinter as tk
import cv2
import webbrowser
import numpy as np
from PIL import Image, ImageTk
import time,sys,os
from time import sleep
import update_back
import GUI_f2
import pymysql,datetime
##########################################################################
# Define the Tkinter functions
def restart():
    con = pymysql.connect(user='root', password='12345678', db='teamp')
    curs = con.cursor()
    #-- QUIT_ --#
    #-----------#
    def quit_(root):
        root.destroy()
    #---------------------
    #---------------#

    def function1(root):

        rows, dish = call_value_f_db()
        url = "http://www.allrecipes.com/search/results/?wt={}".format(dish[0])
        b = webbrowser.get('firefox')
        b.open(url)
        for t in rows:
            if dish[0] in t[1]:
                d = datetime.datetime.now()

                d = d.strftime('%Y-%m-%d')
                sql2 = "UPDATE RecoDishes SET Counts = '%s', Recodate = '%s' WHERE Dishes = '%s'" % (
                (t[2] + 1), d, dish[0])
                sql3 = "insert into RecoDate (Dishes,Recodate) values ('%s' , '%s')" % (dish[0], d)

        curs.execute(sql2)
        curs.execute(sql3)

        con.commit()
        con.close()
    #---------------------

    #-- FUNCTION2 --#
    #---------------#
    def function2(root):

        rows, dish = call_value_f_db()
        url = "http://www.allrecipes.com/search/results/?wt={}".format(dish[1])
        b = webbrowser.get('firefox')
        b.open(url)
        for t in rows:
            if dish[1] in t[1]:
                d = datetime.datetime.now()

                d = d.strftime('%Y-%m-%d')
                sql2 = "UPDATE RecoDishes SET Counts = '%s', Recodate = '%s' WHERE Dishes = '%s'" % (
                (t[2] + 1), d, dish[1])
                sql3 = "insert into RecoDate (Dishes,Recodate) values ('%s' , '%s')" % (dish[1], d)

        curs.execute(sql2)
        curs.execute(sql3)

        con.commit()
        con.close()
    #---------------------

    #-- FUNCTION3 --#
    #---------------#
    def function3(root):

        rows, dish = call_value_f_db()
        url = "http://www.allrecipes.com/search/results/?wt={}".format(dish[2])
        b = webbrowser.get('firefox')
        b.open(url)
        for t in rows:
            if dish[2] in t[1]:
                d = datetime.datetime.now()

                d = d.strftime('%Y-%m-%d')
                sql2 = "UPDATE RecoDishes SET Counts = '%s', Recodate = '%s' WHERE Dishes = '%s'" % (
                (t[2] + 1), d, dish[2])
                sql3 = "insert into RecoDate (Dishes,Recodate) values ('%s' , '%s')" % (dish[2], d)

                curs.execute(sql2)
                curs.execute(sql3)

        con.commit()
        con.close()
    #---------------------

    def restart_program():
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, *sys.argv)
    #---------------------
    def call_value_f_db():
        rows,wls, food_list,_ = update_back.print_update()
        return   rows,food_list

    ##########################################################################
    ##########################################################################

    if __name__ == '__main__':
            root = tk.Tk()

            #lo = tk.Label(root, text="Hello world")
            rows,b,_,w=update_back.print_update()
            for i in w:

                lo = tk.Label(root, text=i)

                lo.grid(padx=0, pady=0)
                lo.config(font=("Courier", 17))
            print _,len(_),len(w)
            if len(_)==1:
                button1 = tk.Button(master=root, text="%s" % _[0], command=lambda: function1(root))
                button1.grid(column=4, columnspan=2, row=0, padx=10, pady=10)
            elif len(_)==2:
                button1 = tk.Button(master=root, text="%s" % _[0], command=lambda: function1(root) )
                button1.grid(column=4, columnspan=2, row=0, padx=10, pady=10)
                button2 = tk.Button(master=root, text='{}'.format(_[1]), command=lambda: function2(root))
                button2.grid(column=4, columnspan=2, row=1, padx=10, pady=10)

            elif len(_)==3:
                button1 = tk.Button(master=root, text="%s"%_[0], command=lambda: function1(root))
                button1.grid(column=4, columnspan=2, row=0, padx=10, pady=10)
                button2 = tk.Button(master=root, text='{}'.format(_[1]), command=lambda: function2(root))
                button2.grid(column=4, columnspan=2, row=1, padx=10, pady=10)
                button3 = tk.Button(master=root, text='{}'.format(_[2]), command=lambda: function3(root))
                button3.grid(column=4, columnspan=2, row=2, padx=10, pady=10)
            quit_button = tk.Button(master=root, text='Quit',bg="red3", fg="white", command=lambda: quit_(root))
            quit_button.grid(column=4, row=3, padx=12, pady=12)

            restart_button = tk.Button(master=root, text='Restart', bg="red3", fg="white", command=  restart_program )
            restart_button.grid(column=4, row=4, padx=14, pady=14)
            root.mainloop()
restart()