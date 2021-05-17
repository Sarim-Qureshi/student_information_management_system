import os
from tkinter import messagebox
from  tkinter import *
import mysql.connector
import re
from time import sleep
import random 
import yagmail
import string

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



def faculty_reg():
  tname = fname.get().strip()
  tlname = lname.get().strip()
  tphno = phno.get().strip()
  depart = clickedDepart.get()
  desig  = clickedDesig.get()
  tmail = mail.get().strip()
  tfid = fid.get().strip()

  if fname.get().strip() == "" or lname.get().strip() == "" or phno.get().strip() == "" or clickedDepart.get() == "" or clickedDesig.get() == "" or mail.get() == "" or fid.get().strip() == "":
    messagebox.showerror("Error","Enter all the Credentials")
  else:
    if  re.search(emailValidate, tmail) and re.search(r'^[789]\d{9}$', tphno):
      try :
        #registering the faculty
        sql = ("insert into faculty values(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        username = str(tname+str(tfid)+"@sakec")
        pswd = ''.join((random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8)))
        values = (tname,tlname,tphno,depart,desig,tmail,tfid,username,pswd)
        mycursor.execute(sql, values)
        #Giving role
        sql1= ("insert into login values(%s,%s,%s)")
        val = (username,pswd,"faculty")
        mycursor.execute(sql1,val)
        
        messagebox.showinfo("Sucess","Faculty Registered")
       
        # #Seding mail
        reciever = mail.get().strip()
        message="Congratulation, You are now Registered Faculty for SIMS !! \nKindly find your Username and password for Student Information Management System\n Username: {} \n Password: {} \n Change Your Password as soon as possible from the faculty Dashboard \n Thank You".format(username,pswd)
        sender = yagmail.SMTP('studentmanagement336@gmail.com','admin1234admin')
        sender.send(to = reciever,subject = "Username And Password for SIMS",contents=message)  
        messagebox.showinfo("Sucess","Username and Password Sent Sucessfully")

        #commiting the database
        mydb.commit()
        
      except mysql.connector.Error as  e:
        messagebox.showerror("Error", "Something went Wrong !! Try Again")
      finally:
        fname.get().set("")
        lname.get().set("")
        phno.get().set("")
        clickedDepart.set("")
        clickedDesig.set("")
        mail.get().set("")
        fid.get().set("")


    else:
      messagebox.showerror("Error","Check your email and Phone Number")



Label(root,text = "Register New Faculty").grid(row = 0, column = 2)
Label(root, text = "Enter First Name").grid(row = 1, column = 1)

fname = StringVar()
Entry(root, textvariable = fname,width = 30).grid(row = 1,column = 2)

Label(root, text = "Enter Last Name").grid(row = 2, column = 1)
lname = StringVar()
Entry(root,textvariable = lname,width = 30).grid(row = 2,column = 2)

Label(root, text = "Enter the Phone Number of Faculty").grid(row = 3, column = 1)
phno = StringVar()
Entry(root, textvariable = phno, width = 30).grid(row = 3,column = 2)

Label(root, text = "Select Department").grid(row = 4, column = 1)

optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]
clickedDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedDepart, *optionDepart)
inputstdDepart.grid(row= 4, column = 2)

Label(root, text = "Select the Designation").grid(row = 5,column = 1)
optionDesig = [ "Professor",
        "Head of Department",
          "Assistant Professor"]
clickedDesig = StringVar()
OptionMenu(root, clickedDesig, *optionDesig).grid(row = 5, column = 2)

Label(root, text = "Enter the Email ID").grid(row = 6, column = 1)

mail = StringVar()
Entry(root, textvariable = mail,width = 30).grid(row = 6, column = 2)

Label(root, text = "Enter the Id").grid(row = 7, column = 1)

fid = StringVar()
Entry(root,textvariable = fid,width = 30).grid(row = 7,column = 2)


Button(root, text = "Register", command = faculty_reg,width = 20).grid(row = 8, column = 2)

root.mainloop()