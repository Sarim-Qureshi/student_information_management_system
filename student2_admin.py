import os
from tkinter import messagebox
from  tkinter import *
import mysql.connector
import re
import sys


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="classroom"
)
mycursor=mydb.cursor()

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def update_stud1():
    firstname = inpfname.get().strip()
    lastname = inplname.get().strip()

    phno = inpph.get().strip()
    year = clickedYear.get()
    depart = clickedDepart.get()
    #mail = inpmail.get().strip()

    if inpfname.get().strip() == "" or inplname.get().strip() == "" or inpph.get().strip() == "" or clickedYear.get() == "" or clickedDepart.get() == "" :
        messagebox.showerror("Error", "Enter all the Details")

    
    else:
        if re.search(r'^[789]\d{9}$', phno):
            try:
                sql = ("UPDATE register SET firstname = %s, lastname = %s, registerId = %s, phoneNumber = %s, year= %s,depart = %s WHERE registerId = {}".format(sys.argv[1]))
                values = (firstname,lastname,rid,phno, year, depart)
                mycursor.execute(sql,values)
                mydb.commit()
                messagebox.showinfo("Message","Details Updated Sucessfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error","Some Error Occured")

            finally:
                root.destroy()
        else:
            messagebox.showerror('Invalid Email or Phone Number', 'Ensure that email id or phone number is valid')




root = Tk()
root.geometry("650x650")
root.title("Student Details")
root.resizable(False,False)

Label(root,text = "Old Details").grid(row = 0, column = 2)

Label(root,text = "First Name").grid(row = 1, column = 1)
Label(root,text = "Last Name").grid(row = 2, column = 1)
Label(root,text = "Registration Id").grid(row = 3, column = 1)
Label(root,text = "Phone Number").grid(row = 4, column = 1)
Label(root, text = "Year").grid(row = 5, column = 1)
Label(root, text = "Department").grid(row = 6, column = 1)
Label(root, text = "Email ID").grid(row = 7, column = 1)




try :
    
    sql = ("select * from register where registerId = {} ".format(sys.argv[1]))
    mycursor.execute(sql)
    res = mycursor.fetchall()
    for row in res:
        res = row
        fname = res[0]
        lname = res[1]
        rid = res[2]
        phone = res[3]
        year = res[4]
        depart = res[5]
        email = res[6]

    Label(root,text = fname).grid(row = 1, column = 2)
    Label(root,text = lname).grid(row = 2, column = 2)
    Label(root,text = rid).grid(row = 3, column = 2)
    Label(root,text = phone).grid(row = 4, column = 2)
    Label(root, text = year).grid(row = 5, column = 2)
    Label(root, text = depart).grid(row = 6, column = 2)
    Label(root, text = email).grid(row = 7, column =2)

except mysql.connector.Error as e:
    messagebox.showerror("Error", "Something went wrong !!")


Label(root, text = "Enter Here New Details to Update/Change").grid(row = 9 ,column = 2)

Label(root,text = "First Name").grid(row = 10, column = 1)
Label(root,text = "Last Name").grid(row = 11, column = 1)
Label(root,text = "Registration Id").grid(row = 12, column = 1)
Label(root,text = "Phone Number").grid(row = 13, column = 1)
Label(root, text = "Year").grid(row = 14, column = 1)
Label(root, text = "Department").grid(row = 15, column = 1)
Label(root, text = "Email ID").grid(row = 16, column = 1)


inpfname = StringVar()
Entry(root,width = 30,textvariable = inpfname).grid(row = 10, column = 2)

inplname = StringVar()
Entry(root,width = 30,textvariable = inplname).grid(row = 11, column = 2)


Label(root,text = rid).grid(row = 12,column = 2)

inpph = StringVar()
Entry(root,width = 30,textvariable = inpph).grid(row = 13, column = 2)


optionYear = ["FE", "SE", "TE", "BE"]
clickedYear = StringVar()
inputstdYear = OptionMenu(root, clickedYear, *optionYear,)
inputstdYear.grid(row = 14, column = 2)


optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]
clickedDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedDepart, *optionDepart)
inputstdDepart.grid(row= 15, column = 2)


Label(root,width = 30, text = email).grid(row = 16, column = 2)

Button(root, text = "Update Details",width = 30,command = update_stud1).grid(row = 18, column = 2)





root.mainloop()