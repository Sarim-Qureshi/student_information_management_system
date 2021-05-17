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
root.title("Exam Officer Details")
root.resizable(False,False)

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def update_examcell1():
    ecfirstname = inpecfname.get().strip()
    eclastname = inpeclname.get().strip()

    ecphno = inpecph.get().strip()
    #facdesig = clickedfacDesig.get()
    ecdepart = clickedecDepart.get()
    #facmail = inpfacmail.get().strip()

    if inpecfname.get().strip() == "" or inpeclname.get().strip() == "" or inpecph.get().strip() == "" or clickedecDepart.get() == "":
        messagebox.showerror("Error", "Enter all the Details")

    
    else:
        if re.search(r'^[789]\d{9}$', ecphno):
            try:
                sql = ("UPDATE examcell SET fname = %s, lname = %s, phone = %s, depart = %s WHERE ecid = {}".format(sys.argv[1]))
                values = (ecfirstname,eclastname,ecphno,ecdepart)
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
   
    sql = ("select * from examcell where ecid = {}".format(sys.argv[1]))
    mycursor.execute(sql)
    res = mycursor.fetchall()
    for row in res:
        
        res = row
        ecfname = res[0]
        eclname = res[1]
        ecphone = res[2]
        ecdepart = res[3]
        #facdesig = res[4]
        ecemail = res[4]
        ecid = res[5]

    Label(root,text = ecfname).grid(row = 1, column = 2)
    Label(root,text = eclname).grid(row = 2, column = 2)
    Label(root,text = ecphone).grid(row = 3, column = 2)
    Label(root,text = ecdepart).grid(row = 4, column = 2)
   # Label(root, text = pldesig).grid(row = 5, column = 2)
    Label(root, text = ecemail).grid(row = 6, column = 2)
    Label(root, text = ecid).grid(row = 7, column =2)

except mysql.connector.Error as e:
    messagebox.showerror("Error", "Something went wrong !!")


Label(root, text = "Enter Here New Details to Update/Change").grid(row = 9 ,column = 2)

Label(root,text = "First Name").grid(row = 10, column = 1)
Label(root,text = "Last Name").grid(row = 11, column = 1)
Label(root,text = "Exam Officer Id").grid(row = 12, column = 1)
Label(root,text = "Phone Number").grid(row = 13, column = 1)
#Label(root, text = "Designation").grid(row = 14, column = 1)
Label(root, text = "Department").grid(row = 15, column = 1)
Label(root, text = "Email Id").grid(row = 16, column = 1)


inpecfname = StringVar()
Entry(root,width = 30,textvariable = inpecfname).grid(row = 10, column = 2)

inpeclname = StringVar()
Entry(root,width = 30,textvariable = inpeclname).grid(row = 11, column = 2)


Label(root,text = ecid).grid(row = 12,column = 2)

inpecph = StringVar()
Entry(root,width = 30,textvariable = inpecph).grid(row = 13, column = 2)


# optionDesig = [ "Professor",
#         "Head of Department",
#           "Assistant Professor"]
# clickedfacDesig = StringVar()
# OptionMenu(root, clickedfacDesig, *optionDesig).grid(row = 14, column = 2)



optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]
clickedecDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedecDepart, *optionDepart)
inputstdDepart.grid(row= 15, column = 2)

Label(root,width = 30, text = ecemail).grid(row = 16, column = 2)

Button(root, text = "Update Details",width = 30,command = update_examcell1).grid(row = 18, column = 2)




root.mainloop()