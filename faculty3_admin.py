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
root.title("Faculty Details")
root.resizable(False,False)

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def update_fac1():
    facfirstname = inpfacname.get().strip()
    faclastname = inplacname.get().strip()

    facphno = inpfacph.get().strip()
    facdesig = clickedfacDesig.get()
    facdepart = clickedfacDepart.get()
    #facmail = inpfacmail.get().strip()

    if inpfacname.get().strip() == "" or inplacname.get().strip() == "" or inpfacph.get().strip() == "" or clickedfacDesig.get() == "" or clickedfacDepart.get() == "":
        messagebox.showerror("Error", "Enter all the Details")

    
    else:
        if re.search(r'^[789]\d{9}$', facphno):
            try:
                sql = ("UPDATE faculty SET fname = %s, lname = %s, phone = %s, depart = %s, desig = %s, fid = %s WHERE fid = {}".format(sys.argv[1]))
                values = (facfirstname,faclastname,facphno,facdepart,facdesig, facid)
                mycursor.execute(sql,values)
                mydb.commit()
                messagebox.showinfo("Message","Details Updated Sucessfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error","Some Error Occured")

            finally:
                root.destroy()
        else:
            messagebox.showerror('Invalid  Phone Number', 'Ensure that  phone number is valid')



    pass



Label(root,text = "Old Details").grid(row = 0, column = 2)

Label(root,text = "First Name").grid(row = 1, column = 1)
Label(root,text = "Last Name").grid(row = 2, column = 1)
Label(root,text = "Phone Number").grid(row = 3, column = 1)
Label(root,text = "Department").grid(row = 4, column = 1)
Label(root, text = "Designation").grid(row = 5, column = 1)
Label(root, text = "Email Id").grid(row = 6, column = 1)
Label(root, text = "Faculty ID").grid(row = 7, column = 1)



try :
   
    sql = ("select * from faculty where fid = {}".format(sys.argv[1]))
    mycursor.execute(sql)
    res = mycursor.fetchall()
    for row in res:
        
        res = row
        facname = res[0]
        lacname = res[1]
        facphone = res[2]
        facdepart = res[3]
        facdesig = res[4]
        facemail = res[5]
        facid = res[6]

    Label(root,text = facname).grid(row = 1, column = 2)
    Label(root,text = lacname).grid(row = 2, column = 2)
    Label(root,text = facphone).grid(row = 3, column = 2)
    Label(root,text = facdepart).grid(row = 4, column = 2)
    Label(root, text = facdesig).grid(row = 5, column = 2)
    Label(root, text = facemail).grid(row = 6, column = 2)
    Label(root, text = facid).grid(row = 7, column =2)

except mysql.connector.Error as e:
    messagebox.showerror("Error", "Something went wrong !!")


Label(root, text = "Enter Here New Details to Update/Change").grid(row = 9 ,column = 2)

Label(root,text = "First Name").grid(row = 10, column = 1)
Label(root,text = "Last Name").grid(row = 11, column = 1)
Label(root,text = "Faculty Id").grid(row = 12, column = 1)
Label(root,text = "Phone Number").grid(row = 13, column = 1)
Label(root, text = "Designation").grid(row = 14, column = 1)
Label(root, text = "Department").grid(row = 15, column = 1)
Label(root, text = "Email Id").grid(row = 16, column = 1)


inpfacname = StringVar()
Entry(root,width = 30,textvariable = inpfacname).grid(row = 10, column = 2)

inplacname = StringVar()
Entry(root,width = 30,textvariable = inplacname).grid(row = 11, column = 2)


Label(root,text = facid).grid(row = 12,column = 2)

inpfacph = StringVar()
Entry(root,width = 30,textvariable = inpfacph).grid(row = 13, column = 2)


optionDesig = [ "Professor",
        "Head of Department",
          "Assistant Professor"]
clickedfacDesig = StringVar()
OptionMenu(root, clickedfacDesig, *optionDesig).grid(row = 14, column = 2)



optionfacDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]
clickedfacDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedfacDepart, *optionfacDepart)
inputstdDepart.grid(row= 15, column = 2)

Label(root,width = 30, text = facemail).grid(row = 16, column = 2)

Button(root, text = "Update Details",width = 30,command = update_fac1).grid(row = 18, column = 2)




root.mainloop()