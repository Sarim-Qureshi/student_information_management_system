import os
from tkinter import messagebox
from tkinter import *
import mysql.connector
import re
import sys


def on_enter(e):
    e.widget['background'] = '#b29700'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#a8a9ad'
    e.widget['foreground'] = 'black'


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="classroom"
# )
font = 'consolas 12 bold'
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sims"
)
mycursor = mydb.cursor()

root = Tk()
root.geometry("1200x600+0+0")
root.title("Exam Officer Details")
root.wm_iconbitmap('zicon.ico')
root.resizable(False, False)

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def update_examcell1():
    ecfirstname = inpecfname.get().strip()
    eclastname = inpeclname.get().strip()
    ecphno = inpecph.get().strip()
    ecdepart = clickedecDepart.get()
    ecmail = inpecmail.get().strip()

    if inpecfname.get().strip() == "" or inpeclname.get().strip() == "" or inpecph.get().strip() == "" or clickedecDepart.get() == "" or inpecmail.get() == '':
        messagebox.showerror("Error", "Enter all the Details")

    else:
        if re.search(r'^[789]\d{9}$', ecphno) and re.search(emailValidate, ecmail):
            try:
                sql = ("UPDATE examcell SET fname = %s, lname = %s, phone = %s, depart = %s, email = %s WHERE ecid = {}".format(
                    sys.argv[1]))
                values = (ecfirstname, eclastname, ecphno, ecdepart, ecmail)
                mycursor.execute(sql, values)
                mydb.commit()
                messagebox.showinfo("Message", "Details Updated Sucessfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", "Some Error Occured")

            finally:
                root.destroy()
        else:
            messagebox.showerror('Message', 'Ensure that phone number and email are valid')


Label(root, text="Old Details", font=font, padx=10, pady=10).grid(row=0, column=0)

Label(root, text="First Name", font=font, padx=10, pady=10).grid(row=1, column=0)
Label(root, text="Last Name", font=font, padx=10, pady=10).grid(row=2, column=0)
Label(root, text="Exam Officer ID", font=font, padx=10, pady=10).grid(row=3, column=0)
Label(root, text="Phone Number", font=font, padx=10, pady=10).grid(row=4, column=0)
Label(root, text="Department", font=font, padx=10, pady=10).grid(row=5, column=0)
Label(root, text="Email Id", font=font, padx=10, pady=10).grid(row=6, column=0)

try:

    sql = ("select * from examcell where ecid = {}".format(sys.argv[1]))
    mycursor.execute(sql)
    res = mycursor.fetchall()
    for row in res:
        res = row
    ecfname = res[0]
    eclname = res[1]
    ecphone = res[2]
    ecdepart = res[3]
    ecemail = res[4]
    ecid = res[5]

    Label(root, text=ecfname, font=font, padx=10, pady=10).grid(row=1, column=1)
    Label(root, text=eclname, font=font, padx=10, pady=10).grid(row=2, column=1)
    Label(root, text=ecid, font=font, padx=10, pady=10).grid(row=3, column=1)
    Label(root, text=ecphone, font=font, padx=10, pady=10).grid(row=4, column=1)
    Label(root, text=ecdepart, font=font, padx=10, pady=10).grid(row=5, column=1)
    Label(root, text=ecemail, font=font, padx=10, pady=10).grid(row=6, column=1)

except mysql.connector.Error as e:
    messagebox.showerror("Error", "Something went wrong !!")

Label(root, text="Enter Here New Details to Update/Change", font=font).grid(row=0, column=2)

Label(root, text="First Name", font=font, padx=10, pady=10).grid(row=1, column=2)
Label(root, text="Last Name", font=font, padx=10, pady=10).grid(row=2, column=2)
Label(root, text="Exam Officer Id", font=font, padx=10, pady=10).grid(row=3, column=2)
Label(root, text="Phone Number", font=font, padx=10, pady=10).grid(row=4, column=2)
Label(root, text="Department", font=font, padx=10, pady=10).grid(row=5, column=2)
Label(root, text="Email Id", font=font, padx=10, pady=10).grid(row=6, column=2)

inpecfname = StringVar()
Entry(root, width=30, textvariable=inpecfname, font=font).grid(row=1, column=3, padx=10, pady=10)

inpeclname = StringVar()
Entry(root, width=30, textvariable=inpeclname, font=font).grid(row=2, column=3, padx=10, pady=10)

Label(root, text=ecid, font=font, padx=10, pady=10).grid(row=3, column=3)

inpecph = StringVar()
Entry(root, width=30, textvariable=inpecph, font=font).grid(row=4, column=3, padx=10, pady=10)

optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]
clickedecDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedecDepart, *optionDepart)
inputstdDepart.grid(row=5, column=3, padx=10, pady=10)
inputstdDepart.configure(font=font)

inpecmail = StringVar()
Entry(root, width=30, textvariable=inpecmail, font=font).grid(row=6, column=3, padx=10, pady=10)

b = Button(root, text="Update Details", width=30, command=update_examcell1, font=font, cursor='hand2')
b.grid(row=7, column=3, padx=10, pady=10)
b.configure(background='#a8a9ad')
b.bind("<Enter>", on_enter)
b.bind("<Leave>", on_leave)

root.mainloop()
