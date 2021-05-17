from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
import re
import yagmail
from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar
from datetime import date

today = date.today()


def on_enter2(e):
    e.widget['background'] = '#033500'
    e.widget['foreground'] = 'white'


def on_leave2(e):
    e.widget['background'] = '#3cb043'
    e.widget['foreground'] = 'black'

font = 'consolas 14 bold'
font2 = 'consolas 11 bold'
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="classroom"
# )


root = Tk()
root.geometry("810x670+0+0")
root.title("Attendance")


def addrecord():
    additem = inpRegisterID.get()
    print(additem)
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sims"
        )
        mycursor = mydb.cursor()
        # sql = ("select * from register where registerId = {} ".format(additem))
        sql = ("select firstname, lastname, registration_id, phone_no, year, department, sem"
               " from register where registration_id = {} and sem = {}".format(additem, sys.argv[1]))
        # sql = ("select * from register where depart = \"Information Technology\"")
        mycursor.execute(sql)
        res = mycursor.fetchall()
        print(res)
        for row in res:
            tree.insert("", tk.END, values=row)
        mydb.close()

    except mysql.connector.Error as e:
        print(e)
    # finally:
    #     inpRegisterID.set("")


def selectItem(a):
    curItem = tree.focus()
    # additem = tree.item(curItem)['values'][2]
    # name = tree.item(curItem)['values'][0] + " " + tree.item(curItem)['values'][1]
    # year = tree.item(curItem)['values'][4]
    # depart = tree.item(curItem)['values'][5]
    sid = tree.item(curItem)['values'][2]
    fid = 11
    dept = tree.item(curItem)['values'][5]
    sem = tree.item(curItem)['values'][6]

    subj = clickedSubj.get()

    dat = cal.get_date()

    if clickedSubj.get() == "" or inpRegisterID.get() == "" or cal.get_date() == "":
        messagebox.showinfo("messagebox", "Enter fields")
    else:
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="sims"
            )
            mycursor = mydb.cursor()
            # response = messagebox.askyesno("Message Box", "Mark Attendance for {}".format(additem))
            # if response == 1:
            #     sql = "insert into attendance values (%s,%s, %s, %s,%s,%s,%s,%s)"
            #     val = (name, additem, year, depart, 78965, "teacher1", dat, subj)
            #     # sql = "insert into attendance values(%s, %s, %s, %s, %s)"
            #     # val = (name, )
            #     mycursor.execute(sql, val)
            #     mydb.commit()
            #     mydb.close()
            #     messagebox.showinfo("Message Box", "Attendance Marked")

            response = messagebox.askyesno("Message Box", "Mark Attendance for {}".format(sid))
            if response == 1:
                sql = "insert into attendance values (%s, %s, %s, %s, %s, %s)"
                val = (sid, fid, sem, dept, subj, dat)
                # sql = "insert into attendance values(%s, %s, %s, %s, %s)"
                # val = (name, )
                mycursor.execute(sql, val)
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Message Box", "Attendance Marked")
                return

        except mysql.connector.Error as e:
            print("not sucess")
            print(e)


Label(root, text="Add Attendance", font=font, padx=20).grid(row=0, column=1, columnspan=2)

Label(root, text="Enter Register Id", font=font2, padx=20).grid(row=1, column=0)

inpRegisterID = StringVar()
registerId = Entry(root, textvariable=inpRegisterID, font=font2).grid(row=1, column=1)
b = Button(root, text="Show", command=addrecord, font='consolas 13 bold', cursor='hand2')
b.grid(row=3, column=0, pady=20)
b.bind("<Enter>", on_enter2)
b.bind("<Leave>", on_leave2)
b.configure(background='#3cb043')

import sys
dept = ''
for index, x in enumerate(sys.argv):
    if index > 1:
        dept += f'{x} '

dept = dept.strip()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sims"
)
mycursor = mydb.cursor()
if sys.argv[1] == "1" or sys.argv[1] == "2":
    mycursor.execute(f"select * from sem{sys.argv[1]}_subjects")
    res = mycursor.fetchall()
    optionSubj = res[0]
else:
    mycursor.execute("select * from subjects where sem=%s and department=%s", (sys.argv[1], dept, ))
    res = mycursor.fetchall()
    print(res)
    optionSubj = (res[0])[2:]
mydb.close()
# optionSubj = ["EM-4",
#               "OS",
#               "COA",
#               "CNND",
#               "AT"]
stdSubj = Label(root, text=" Select Subject", font=font2, padx=10).grid(row=2, column=0)
clickedSubj = StringVar()
inputSubj = OptionMenu(root, clickedSubj, *optionSubj)
inputSubj.grid(row=2, column=1)
inputSubj.configure(font=font2)

cal = Calendar(root, selectmode='day')
cal.grid(row=1, column=4)

tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings', selectmode='browse')
style = ttk.Style()
style.configure("Treeview.Heading", font='consolas 12 bold')

tree.column("#1", anchor=tk.CENTER, width=100)
tree.heading("#1", text="First Name")

tree.column("#2", anchor=tk.CENTER, width=100)
tree.heading("#2", text="Last Name")

tree.column("#3", anchor=tk.CENTER, width=150)
tree.heading("#3", text="Registration Id")

tree.column("#4", anchor=tk.CENTER, width=120)
tree.heading("#4", text="Phone Number")

tree.column("#5", anchor=tk.CENTER, width=80)
tree.heading("#5", text="Year")

tree.column("#6", anchor=tk.CENTER, width=100)
tree.heading("#6", text="Department")

tree.column("#7", anchor=tk.CENTER, width=100)
tree.heading("#7", text="Semester")

tree.bind('<ButtonRelease-1>', selectItem)

tree.place(x=20, y=330)

# Button(root, text = "Mark Attendance", command = markAttendance).place(x = 300 , y = 530)

root.mainloop()
