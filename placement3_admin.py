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
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sims"
)
mycursor = mydb.cursor()
font = 'consolas 12 bold'

root = Tk()
root.geometry("1200x600+0+0")
root.title("Placement Officer Details")
root.resizable(False, False)

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def update_place1():
    plfirstname = inpplfname.get().strip()
    pllastname = inppllname.get().strip()
    plphno = inpplph.get().strip()
    pldepart = clickedplDepart.get()
    plmail = inpplemail.get().strip()

    if inpplfname.get().strip() == "" or inppllname.get().strip() == "" or inpplph.get().strip() == "" or clickedplDepart.get() == "" or inpplemail.get()=='':
        messagebox.showerror("Error", "Enter all the Details")


    else:
        if re.search(r'^[789]\d{9}$', plphno) and re.search(emailValidate, plmail):
            try:
                sql = (
                    "UPDATE placementofficer SET fname = %s, lname = %s, phone = %s, depart = %s, email = %s WHERE plid = {}".format(
                        sys.argv[1]))
                values = (plfirstname, pllastname, plphno, pldepart, plmail)
                mycursor.execute(sql, values)
                mydb.commit()
                messagebox.showinfo("Message", "Details Updated Sucessfully")
            except mysql.connector.Error as e:
                print(e)
                messagebox.showerror("Error", "Some Error Occured")

            finally:
                root.destroy()
        else:
            messagebox.showerror('Message', 'Ensure that phone number and email ID are valid')


Label(root, text="Old Details", font=font, padx=10, pady=10).grid(row=0, column=0)

Label(root, text="First Name", font=font, padx=10, pady=10).grid(row=1, column=0)
Label(root, text="Last Name", font=font, padx=10, pady=10).grid(row=2, column=0)
Label(root, text="Placement Officer ID", font=font, padx=10, pady=10).grid(row=3, column=0)
Label(root, text="Phone Number", font=font, padx=10, pady=10).grid(row=4, column=0)
Label(root, text="Department", font=font, padx=10, pady=10).grid(row=5, column=0)
Label(root, text="Email Id", font=font, padx=10, pady=10).grid(row=6, column=0)

try:

    sql = ("select * from placementofficer where plid = {}".format(sys.argv[1]))
    mycursor.execute(sql)
    res = mycursor.fetchall()
    for row in res:
        res = row
        plfname = res[0]
        pllname = res[1]
        plphone = res[2]
        pldepart = res[3]
        # facdesig = res[4]
        plemail = res[5]
        plid = res[4]

    Label(root, text=plfname, font=font, padx=10, pady=10).grid(row=1, column=1)
    Label(root, text=pllname, font=font, padx=10, pady=10).grid(row=2, column=1)
    Label(root, text=plid, font=font, padx=10, pady=10).grid(row=3, column=1)
    Label(root, text=plphone, font=font, padx=10, pady=10).grid(row=4, column=1)
    Label(root, text=pldepart, font=font, padx=10, pady=10).grid(row=5, column=1)
    Label(root, text=plemail, font=font, padx=10, pady=10).grid(row=6, column=1)

except mysql.connector.Error as e:
    messagebox.showerror("Error", "Something went wrong !!")

Label(root, text="Enter Here New Details to Update/Change", font=font, pady=10, padx=10).grid(row=0, column=2)

Label(root, text="First Name", font=font, padx=10, pady=10).grid(row=1, column=2)
Label(root, text="Last Name", font=font, padx=10, pady=10).grid(row=2, column=2)
Label(root, text="Placement Officer Id", font=font, padx=10, pady=10).grid(row=3, column=2)
Label(root, text="Phone Number", font=font, padx=10, pady=10).grid(row=4, column=2)
Label(root, text="Department", font=font, padx=10, pady=10).grid(row=5, column=2)
Label(root, text="Email Id", font=font, padx=10, pady=10).grid(row=6, column=2)

inpplfname = StringVar()
Entry(root, width=30, textvariable=inpplfname, font=font).grid(row=1, column=3, padx=10, pady=10)

inppllname = StringVar()
Entry(root, width=30, textvariable=inppllname, font=font).grid(row=2, column=3, padx=10, pady=10)

Label(root, text=plid, font=font, padx=10, pady=10).grid(row=3, column=3)

inpplph = StringVar()
Entry(root, width=30, textvariable=inpplph, font=font).grid(row=4, column=3, padx=10, pady=10)


optionplDepart = ["Information Technology",
                  "Computer Engineering",
                  "Electronics",
                  "Electronics and Telecommunications"]
clickedplDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedplDepart, *optionplDepart)
inputstdDepart.grid(row=5, column=3, padx=10, pady=10)
inputstdDepart.configure(font=font)

inpplemail = StringVar()
Entry(root, width=30, textvariable=inpplemail, font=font).grid(row=6, column=3, pady=10, padx=10)

b = Button(root, text="Update Details", width=30, command=update_place1, font=font, cursor='hand2')
b.grid(row=7, column=3, padx=10, pady=10)
b.configure(background='#a8a9ad')
b.bind("<Enter>", on_enter)
b.bind("<Leave>", on_leave)

root.mainloop()
