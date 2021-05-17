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

root = Tk()
root.geometry("650x650")
root.title("Placement Officer Details")
root.resizable(False,False)

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def update_place1():
    plfirstname = inpplfname.get().strip()
    pllastname = inppllname.get().strip()

    plphno = inpplph.get().strip()
    #facdesig = clickedfacDesig.get()
    pldepart = clickedplDepart.get()
    #facmail = inpfacmail.get().strip()

    if inpplfname.get().strip() == "" or inppllname.get().strip() == "" or inpplph.get().strip() == "" or clickedplDepart.get() == "":
        messagebox.showerror("Error", "Enter all the Details")

    
    else:
        if re.search(r'^[789]\d{9}$', plphno):
            try:
                sql = ("UPDATE placementofficer SET fname = %s, lname = %s, phone = %s, depart = %s WHERE plid = {}".format(sys.argv[1]))
                values = (plfirstname,pllastname,plphno,pldepart)
                mycursor.execute(sql,values)
                mydb.commit()
                messagebox.showinfo("Message","Details Updated Sucessfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error","Some Error Occured")

            finally:
                root.destroy()
        else:
            messagebox.showerror('Invalid  Phone Number', 'Ensure that  phone number is valid')



Label(root,text = "Old Details").grid(row = 0, column = 2)

Label(root,text = "First Name").grid(row = 1, column = 1)
Label(root,text = "Last Name").grid(row = 2, column = 1)
Label(root,text = "Phone Number").grid(row = 3, column = 1)
Label(root,text = "Department").grid(row = 4, column = 1)
#Label(root, text = "Designation").grid(row = 5, column = 1)
Label(root, text = "Email Id").grid(row = 6, column = 1)
Label(root, text = "Faculty ID").grid(row = 7, column = 1)



try :
   
    sql = ("select * from placementofficer where plid = {}".format(sys.argv[1]))
    mycursor.execute(sql)
    res = mycursor.fetchall()
    for row in res:
        
        res = row
        plfname = res[0]
        pllname = res[1]
        plphone = res[2]
        pldepart = res[3]
        #facdesig = res[4]
        plemail = res[5]
        plid = res[4]

    Label(root,text = plfname).grid(row = 1, column = 2)
    Label(root,text = pllname).grid(row = 2, column = 2)
    Label(root,text = plphone).grid(row = 3, column = 2)
    Label(root,text = pldepart).grid(row = 4, column = 2)
   # Label(root, text = pldesig).grid(row = 5, column = 2)
    Label(root, text = plemail).grid(row = 6, column = 2)
    Label(root, text = plid).grid(row = 7, column =2)

except mysql.connector.Error as e:
    messagebox.showerror("Error", "Something went wrong !!")


Label(root, text = "Enter Here New Details to Update/Change").grid(row = 9 ,column = 2)

Label(root,text = "First Name").grid(row = 10, column = 1)
Label(root,text = "Last Name").grid(row = 11, column = 1)
Label(root,text = "Placement Officer Id").grid(row = 12, column = 1)
Label(root,text = "Phone Number").grid(row = 13, column = 1)
#Label(root, text = "Designation").grid(row = 14, column = 1)
Label(root, text = "Department").grid(row = 15, column = 1)
Label(root, text = "Email Id").grid(row = 16, column = 1)


inpplfname = StringVar()
Entry(root,width = 30,textvariable = inpplfname).grid(row = 10, column = 2)

inppllname = StringVar()
Entry(root,width = 30,textvariable = inppllname).grid(row = 11, column = 2)


Label(root,text = plid).grid(row = 12,column = 2)

inpplph = StringVar()
Entry(root,width = 30,textvariable = inpplph).grid(row = 13, column = 2)


# optionDesig = [ "Professor",
#         "Head of Department",
#           "Assistant Professor"]
# clickedfacDesig = StringVar()
# OptionMenu(root, clickedfacDesig, *optionDesig).grid(row = 14, column = 2)



optionplDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]
clickedplDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedplDepart, *optionplDepart)
inputstdDepart.grid(row= 15, column = 2)

Label(root,width = 30, text = plemail).grid(row = 16, column = 2)

Button(root, text = "Update Details",width = 30,command = update_place1).grid(row = 18, column = 2)




root.mainloop()