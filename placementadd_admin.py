import os
from tkinter import messagebox
from tkinter import *
import mysql.connector
import re
from time import sleep
import random
import yagmail
import string


font = 'consolas 12 bold'


def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


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

root = Tk()
root.geometry("650x500+0+0")
root.title("Faculty Details")
root.resizable(False, False)

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def placement_reg():
    tname = plfname.get().strip()
    tlname = pllname.get().strip()
    tphno = plphno.get().strip()
    depart = clickedDepart.get()
    # desig  = clickedDesig.get()
    tmail = plmail.get().strip()
    tplid = plid.get().strip()

    if plfname.get().strip() == "" or pllname.get().strip() == "" or plphno.get().strip() == "" or clickedDepart.get() == "" or plmail.get() == "" or plid.get().strip() == "":
        messagebox.showerror("Error", "Enter all the Credentials")
    else:
        if re.search(emailValidate, tmail) and re.search(r'^[789]\d{9}$', tphno):
            try:
                # registering the Placement Officer
                sql = "insert into placementofficer values(%s,%s,%s,%s,%s,%s,%s,%s)"
                username = str(tname + str(tplid) + "@sakec")
                pswd = ''.join(
                    (random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8)))
                values = (tname, tlname, tphno, depart, tplid, tmail, username, pswd)
                mycursor.execute(sql, values)

                # Giving role
                sql1 = ("insert into login values(%s,%s,%s)")
                val = (username, pswd, "placement")
                mycursor.execute(sql1, val)

                messagebox.showinfo("Sucess", "Placement Officer Registered")

                # #Seding mail
                reciever = plmail.get().strip()
                message = "Congratulation, You are now Registered Placement Officer!! \nKindly find your Username and password for Student Information Management System\n Username: {} \n Password: {} \n Change Your Password as soon as possible from the Placement Dashboard \n Thank You".format(
                    username, pswd)
                sender = yagmail.SMTP('studentmanagement336@gmail.com', 'admin1234admin')
                sender.send(to=reciever, subject="Username And Password for SIMS", contents=message)

                messagebox.showinfo("Sucess", "Username and Password Sent Sucessfully")

                # commiting the database
                mydb.commit()

            except mysql.connector.Error as e:
                print(e)
                messagebox.showerror("Error", "Something went Wrong !! Try Again")
            finally:
                plfname.set("")
                pllname.set("")
                plphno.set("")
                clickedDepart.set("")
                # clickedDesig.set("")
                plmail.set("")
                plid.set("")


        else:
            messagebox.showerror("Error", "Check your email and Phone Number")


Label(root, text="Register New Placement Officer", font='consolas 13 bold', pady=10, padx=10).grid(row=0, column=2)
Label(root, text="Enter First Name", font=font, pady=10, padx=10).grid(row=1, column=1)

plfname = StringVar()
Entry(root, textvariable=plfname, width=30, font=font).grid(row=1, column=2, pady=10, padx=10)

Label(root, text="Enter Last Name", font=font, pady=10, padx=10).grid(row=2, column=1)
pllname = StringVar()
Entry(root, textvariable=pllname, width=30, font=font).grid(row=2, column=2, pady=10, padx=10)

Label(root, text="Enter the Phone Number of officer", font=font, pady=10, padx=10).grid(row=3, column=1)
plphno = StringVar()
Entry(root, textvariable=plphno, width=30, font=font).grid(row=3, column=2, pady=10, padx=10)

Label(root, text="Select Department", font=font, pady=10, padx=10).grid(row=4, column=1)

optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]
clickedDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedDepart, *optionDepart)
inputstdDepart.grid(row=4, column=2, pady=10, padx=10)
inputstdDepart.configure(font=font)

Label(root, text="Enter the Email ID", font=font, pady=10, padx=10).grid(row=5, column=1)

plmail = StringVar()
Entry(root, textvariable=plmail, width=30, font=font).grid(row=5, column=2, pady=10, padx=10)

Label(root, text="Enter the Id", font=font, pady=10, padx=10).grid(row=6, column=1)

plid = StringVar()
Entry(root, textvariable=plid, width=30, font=font).grid(row=6, column=2, pady=10, padx=10)

b = Button(root, text="Register", command=placement_reg, width=30, font=font, cursor='hand2')
b.grid(row=7, column=2, pady=10, padx=10)
b.bind("<Enter>", on_enter)
b.bind("<Leave>", on_leave)
b.configure(background='#0277bd')
root.mainloop()
