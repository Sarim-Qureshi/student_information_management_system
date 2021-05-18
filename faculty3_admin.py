import os
from tkinter import messagebox
from tkinter import *
import mysql.connector
import re
import sys

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="classroom"
# )
font = 'consolas 12 bold'


def on_enter(e):
    e.widget['background'] = '#b29700'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#a8a9ad'
    e.widget['foreground'] = 'black'


root = Tk()
root.geometry("1200x600+0+0")
root.title("Faculty Details")
root.wm_iconbitmap('zicon.ico')
root.resizable(False, False)

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def update_fac1():
    facfirstname = inpfacname.get().strip()
    faclastname = inplacname.get().strip()

    facphno = inpfacph.get().strip()
    facdesig = clickedfacDesig.get()
    facdepart = clickedfacDepart.get()
    facmail = inpfacem.get().strip()

    if inpfacname.get().strip() == "" or inplacname.get().strip() == "" or inpfacph.get().strip() == "" or clickedfacDesig.get() == "" or clickedfacDepart.get() == "" or inpfacem.get() == "":
        messagebox.showerror("Error", "Enter all the Details")


    else:
        if re.search(r'^[789]\d{9}$', facphno) and re.search(emailValidate, facemail):
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="sims"
                )
                mycursor = mydb.cursor()
                sql = (
                    "UPDATE faculty SET fname = %s, lname = %s, phone = %s, depart = %s, desig = %s, emailid = %s WHERE fid = {}".format(
                        sys.argv[1]))
                values = (facfirstname, faclastname, facphno, facdepart, facdesig, facmail)
                mycursor.execute(sql, values)
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Message", "Details Updated Sucessfully")
            except mysql.connector.Error as e:
                print(e)
                messagebox.showerror("Error", "Some Error Occured")

            finally:
                root.destroy()
        else:
            messagebox.showerror('Message', 'Ensure that phone number and email ID are valid')

    pass


Label(root, text="Old Details", font=font, pady=10, padx=10).grid(row=0, column=1)

Label(root, text="First Name", font=font, pady=10, padx=10).grid(row=1, column=0)
Label(root, text="Last Name", font=font, pady=10, padx=10).grid(row=2, column=0)
Label(root, text="Faculty ID", font=font, pady=10, padx=10).grid(row=3, column=0)
Label(root, text="Phone Number", font=font, pady=10, padx=10).grid(row=4, column=0)
Label(root, text="Designation", font=font, pady=10, padx=10).grid(row=5, column=0)
Label(root, text="Department", font=font, pady=10, padx=10).grid(row=6, column=0)
Label(root, text="Email ID", font=font, pady=10, padx=10).grid(row=7, column=0)

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sims"
    )
    mycursor = mydb.cursor()
    sql = "select * from faculty where fid = %s"
    mycursor.execute(sql, (sys.argv[1], ))
    print(sys.argv[1])
    res = mycursor.fetchall()[0]
    print(res)
    mydb.close()

    facname = res[0]
    lacname = res[1]
    facphone = res[2]
    facdepart = res[3]
    facdesig = res[4]
    facemail = res[5]
    facid = res[6]

    Label(root, text=facname, font=font, pady=10, padx=10).grid(row=1, column=1)
    Label(root, text=lacname, font=font, pady=10, padx=10).grid(row=2, column=1)
    Label(root, text=facid, font=font, pady=10, padx=10).grid(row=3, column=1)
    Label(root, text=facphone, font=font, pady=10, padx=10).grid(row=4, column=1)
    Label(root, text=facdesig, font=font, pady=10, padx=10).grid(row=5, column=1)
    Label(root, text=facdepart, font=font, pady=10, padx=10).grid(row=6, column=1)
    Label(root, text=facemail, font=font, pady=10, padx=10).grid(row=7, column=1)

except mysql.connector.Error as e:
    messagebox.showerror("Error", "Something went wrong !!")

Label(root, text="Enter Here New Details to Update/Change", font=font).grid(row=0, column=3)

Label(root, text="First Name", font=font, pady=10, padx=10).grid(row=1, column=3)
Label(root, text="Last Name", font=font, pady=10, padx=10).grid(row=2, column=3)
Label(root, text="Faculty ID", font=font, pady=10, padx=10).grid(row=3, column=3)
Label(root, text="Phone Number", font=font, pady=10, padx=10).grid(row=4, column=3)
Label(root, text="Designation", font=font, pady=10, padx=10).grid(row=5, column=3)
Label(root, text="Department", font=font, pady=10, padx=10).grid(row=6, column=3)
Label(root, text="Email ID", font=font, pady=10, padx=10).grid(row=7, column=3)

inpfacname = StringVar()
Entry(root, width=30, textvariable=inpfacname, font=font).grid(row=1, column=4, pady=10, padx=10)

inplacname = StringVar()
Entry(root, width=30, textvariable=inplacname, font=font).grid(row=2, column=4, pady=10, padx=10)

Label(root, text=facid, font=font, pady=10, padx=10).grid(row=3, column=4)

inpfacph = StringVar()
Entry(root, width=30, textvariable=inpfacph, font=font).grid(row=4, column=4, pady=10, padx=10)

optionDesig = ["Professor",
               "Head of Department",
               "Assistant Professor"]
clickedfacDesig = StringVar()
inputstdDesig = OptionMenu(root, clickedfacDesig, *optionDesig)
inputstdDesig.grid(row=5, column=4, pady=10, padx=10)
inputstdDesig.configure(font=font)

optionfacDepart = ["Information Technology",
                   "Computer Engineering",
                   "Electronics",
                   "Electronics and Telecommunications"]
clickedfacDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedfacDepart, *optionfacDepart)
inputstdDepart.grid(row=6, column=4, pady=10, padx=10)
inputstdDepart.configure(font=font)

# Label(root, width=30, text=facemail).grid(row=7, column=4)
inpfacem = StringVar()
Entry(root, width=30, textvariable=inpfacem, font=font).grid(row=7, column=4, pady=10, padx=10)


b = Button(root, width=30, text="Update Details", command=update_fac1, font=font, cursor='hand2')
b.grid(row=8, column=4, pady=10, padx=10)
b.configure(background='#a8a9ad')
b.bind("<Enter>", on_enter)
b.bind("<Leave>", on_leave)

root.mainloop()
