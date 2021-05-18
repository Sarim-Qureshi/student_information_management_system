import os
from tkinter import messagebox
from tkinter import *
import mysql.connector
import re
from time import sleep
import random
import yagmail
import string

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="classroom"
# )
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sims"
)
mycursor = mydb.cursor()
font = 'consolas 12 bold'


def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


root = Tk()
root.geometry("730x500+0+0")
root.wm_iconbitmap('zicon.ico')
root.title("Exam Officer Details")
root.resizable(False, False)

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def examofficer_reg():
    tname = ecfname.get().strip()
    tlname = eclname.get().strip()
    tphno = ecphno.get().strip()
    depart = clickedecDepart.get()
    tmail = ecmail.get().strip()
    tfid = ecid.get().strip()

    if ecfname.get().strip() == "" or eclname.get().strip() == "" or ecphno.get().strip() == "" or clickedecDepart.get() == "" or ecmail.get() == "" or ecid.get().strip() == "":
        messagebox.showerror("Error", "Enter all the Credentials")
    else:
        if re.search(emailValidate, tmail) and re.search(r'^[789]\d{9}$', tphno):
            try:
                # registering the faculty
                sql = ("insert into examcell values(%s,%s,%s,%s,%s,%s,%s,%s)")
                username = str(tname + str(tfid) + "@sakec")
                pswd = ''.join(
                    (random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8)))
                values = (tname, tlname, tphno, depart, tmail, tfid, username, pswd)
                mycursor.execute(sql, values)

                # Giving role
                # sql1 = ("insert into login values(%s,%s,%s,%s)")
                sql1 = "insert into login values(%s,%s,%s)"
                # val = (username, pswd, "examofficer", tfid)
                val = (username, pswd, "exam")
                mycursor.execute(sql1, val)

                messagebox.showinfo("Sucess", "Exam Officer Registered")

                # #Seding mail
                reciever = ecmail.get().strip()
                message = "Congratulation, You are now Registered  for Exam Cell of SIMS !! \nKindly find your Username and password for Student Information Management System\n Username: {} \n Password: {} \n Change Your Password as soon as possible from the Exam Cell Dashboard \n Thank You".format(
                    username, pswd)
                sender = yagmail.SMTP('studentmanagement336@gmail.com', 'admin1234admin')
                sender.send(to=reciever, subject="Username And Password for SIMS", contents=message)
                messagebox.showinfo("Sucess", "Username and Password Sent Sucessfully")

                # commiting the database

                mydb.commit()

            except mysql.connector.Error as  e:
                messagebox.showerror("Error", "Something went Wrong !! Try Again")
            finally:
                ecfname.set("")
                eclname.set("")
                ecphno.set("")
                clickedecDepart.set("")
                ecmail.set("")
                ecid.set("")
        else:
            messagebox.showerror("Error", "Check your email and Phone Number")


Label(root, text="Register New Exam Officer", font='consolas 13 bold', pady=10, padx=10).grid(row=0, column=1)
Label(root, text="Enter First Name", font=font, pady=10, padx=10).grid(row=1, column=0)

ecfname = StringVar()
Entry(root, textvariable=ecfname, width=30, font=font).grid(row=1, column=1, pady=10, padx=10)

Label(root, text="Enter Last Name", font=font, pady=10, padx=10).grid(row=2, column=0)
eclname = StringVar()
Entry(root, textvariable=eclname, width=30, font=font).grid(row=2, column=1, pady=10, padx=10)

Label(root, text="Enter the Phone Number of Faculty", font=font, pady=10, padx=10).grid(row=3, column=0)
ecphno = StringVar()
Entry(root, textvariable=ecphno, width=30, font=font).grid(row=3, column=1, pady=10, padx=10)

Label(root, text="Select Department", font=font, pady=10, padx=10).grid(row=4, column=0)

optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]
clickedecDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedecDepart, *optionDepart)
inputstdDepart.grid(row=4, column=1, pady=10, padx=10)
inputstdDepart.configure(font=font)

Label(root, text="Enter the Email ID", font=font, pady=10, padx=10).grid(row=5, column=0)

ecmail = StringVar()
Entry(root, textvariable=ecmail, width=30, font=font).grid(row=5, column=1, pady=10, padx=10)

Label(root, text="Enter the Id", font=font, pady=10, padx=10).grid(row=6, column=0)

ecid = StringVar()
Entry(root, textvariable=ecid, width=30, font=font).grid(row=6, column=1, pady=10, padx=10)

b = Button(root, text="Register", command=examofficer_reg, width=30, font=font, cursor='hand2')
b.grid(row=7, column=1, pady=10, padx=10)
b.bind("<Enter>", on_enter)
b.bind("<Leave>", on_leave)
b.configure(background='#0277bd')

root.mainloop()
