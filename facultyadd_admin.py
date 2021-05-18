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
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="classroom"
# )
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sims"
)
mycursor = mydb.cursor()

root = Tk()
root.geometry("730x500+0+0")
root.title("Faculty Details")
root.wm_iconbitmap('zicon.ico')
root.resizable(False, False)

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


def faculty_reg():
    tname = fname.get().strip()
    tlname = lname.get().strip()
    tphno = phno.get().strip()
    depart = clickedDepart.get()
    desig = clickedDesig.get()
    tmail = mail.get().strip()
    tfid = fid.get().strip()

    if fname.get().strip() == "" or lname.get().strip() == "" or phno.get().strip() == "" or clickedDepart.get() == "" or clickedDesig.get() == "" or mail.get() == "" or fid.get().strip() == "":
        messagebox.showerror("Error", "Enter all the Credentials")
    else:
        print(tphno, tmail)
        if re.search(emailValidate, tmail) and re.search(r'^[789]\d{9}$', tphno):
            try:
                # registering the faculty
                sql = ("insert into faculty values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                username = str(tname + str(tfid) + "@sakec")
                pswd = ''.join(
                    (random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8)))
                values = (tname, tlname, tphno, depart, desig, tmail, tfid, username, pswd,)
                mycursor.execute(sql, values)
                # Giving role
                sql1 = ("insert into login values(%s,%s,%s)")
                val = (username, pswd, "faculty")
                mycursor.execute(sql1, val)

                messagebox.showinfo("Sucess", "Faculty Registered")

                # #Seding mail
                reciever = mail.get().strip()
                message = "Congratulation, You are now Registered Faculty for SIMS !! \nKindly find your Username and password for Student Information Management System\n Username: {} \n Password: {} \n Change Your Password as soon as possible from the faculty Dashboard \n Thank You".format(
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
                fname.set("")
                lname.set("")
                phno.set("")
                clickedDepart.set("")
                clickedDesig.set("")
                mail.set("")
                fid.set("")


        else:
            messagebox.showerror("Error", "Check your email and Phone Number")


Label(root, text="Register New Faculty", font='consolas 14 bold', pady=10, padx=10).grid(row=0, column=0, columnspan=2)
Label(root, text="Enter First Name", font=font, pady=10, padx=10).grid(row=1, column=0)

fname = StringVar()
Entry(root, textvariable=fname, font=font).grid(row=1, column=1, pady=10, padx=10)

Label(root, text="Enter Last Name", font=font, pady=10, padx=10).grid(row=2, column=0)
lname = StringVar()
Entry(root, textvariable=lname, font=font).grid(row=2, column=1, pady=10, padx=10)

Label(root, text="Enter the Phone Number of Faculty", font=font, pady=10, padx=10).grid(row=3, column=0)
phno = StringVar()
Entry(root, textvariable=phno, font=font).grid(row=3, column=1, pady=10, padx=10)

Label(root, text="Select Department", font=font, pady=10, padx=10).grid(row=4, column=0)

optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]
clickedDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedDepart, *optionDepart)
inputstdDepart.grid(row=4, column=1, pady=10, padx=10)
inputstdDepart.configure(font=font)

Label(root, text="Select the Designation", font=font).grid(row=5, column=0, pady=10, padx=10)
optionDesig = ["Professor",
               "Head of Department",
               "Assistant Professor"]
clickedDesig = StringVar()
inputstdDesig = OptionMenu(root, clickedDesig, *optionDesig)
inputstdDesig.grid(row=5, column=1, pady=10, padx=10)
inputstdDesig.configure(font=font)

Label(root, text="Enter the Email ID", font=font, pady=10, padx=10).grid(row=6, column=0)

mail = StringVar()
Entry(root, textvariable=mail, font=font).grid(row=6, column=1, pady=10, padx=10)

Label(root, text="Enter the Id", font=font, pady=10, padx=10).grid(row=7, column=0)

fid = StringVar()
Entry(root, textvariable=fid, font=font).grid(row=7, column=1, pady=10, padx=10)

b = Button(root, text="Register", command=faculty_reg, width=20, font=font, cursor='hand2')
b.grid(row=8, column=1, pady=10, padx=10)
b.bind("<Enter>", on_enter)
b.bind("<Leave>", on_leave)
b.configure(background='#0277bd')

root.mainloop()
