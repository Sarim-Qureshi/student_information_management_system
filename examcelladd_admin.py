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
root.title("Exam Officer Details")
root.resizable(False,False)

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def examofficer_reg():
  tname = ecfname.get().strip()
  tlname = eclname.get().strip()
  tphno = ecphno.get().strip()
  depart = clickedecDepart.get()
  #desig  = clickedDesig.get()
  tmail = ecmail.get().strip()
  tfid = ecid.get().strip()

  if ecfname.get().strip() == "" or eclname.get().strip() == "" or ecphno.get().strip() == "" or clickedecDepart.get() == "" or ecmail.get() == "" or ecid.get().strip() == "":
    messagebox.showerror("Error","Enter all the Credentials")
  else:
    if  re.search(emailValidate, tmail) and re.search(r'^[789]\d{9}$', tphno):
      try:
        #registering the faculty
        sql = ("insert into examcell values(%s,%s,%s,%s,%s,%s,%s,%s)")
        username = str(tname+str(tfid)+"@sakec")
        pswd = ''.join((random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8)))
        values = (tname,tlname,tphno,depart,tmail,tfid,username,pswd)
        mycursor.execute(sql, values)

        #Giving role
        sql1= ("insert into login values(%s,%s,%s,%s)")
        val = (username,pswd,"examofficer",tfid)
        mycursor.execute(sql1,val)
       
        
        messagebox.showinfo("Sucess","Exam Officer Registered")
       
        # #Seding mail
        reciever = ecmail.get().strip()
        message="Congratulation, You are now Registered  for Exam Cell of SIMS !! \nKindly find your Username and password for Student Information Management System\n Username: {} \n Password: {} \n Change Your Password as soon as possible from the Exam Cell Dashboard \n Thank You".format(username,pswd)
        sender = yagmail.SMTP('studentmanagement336@gmail.com','admin1234admin')
        sender.send(to = reciever,subject = "Username And Password for SIMS",contents=message)  
        messagebox.showinfo("Sucess","Username and Password Sent Sucessfully")

        #commiting the database
        
        
        mydb.commit()
        
      except mysql.connector.Error as  e:
        messagebox.showerror("Error", "Something went Wrong !! Try Again")
      finally:
        ecfname.set("")
        eclname.set("")
        ecphno.set("")
        clickedecDepart.set("")
        #clickedDesig.set("")
        ecmail.set("")
        ecid.set("")
    else:
      messagebox.showerror("Error","Check your email and Phone Number")



Label(root,text = "Register New Exam Officer").grid(row = 0, column = 2)
Label(root, text = "Enter First Name").grid(row = 1, column = 1)
 
ecfname = StringVar()
Entry(root, textvariable = ecfname,width = 30).grid(row = 1,column = 2)

Label(root, text = "Enter Last Name").grid(row = 2, column = 1)
eclname = StringVar()
Entry(root,textvariable = eclname,width = 30).grid(row = 2,column = 2)

Label(root, text = "Enter the Phone Number of Faculty").grid(row = 3, column = 1)
ecphno = StringVar()
Entry(root, textvariable = ecphno, width = 30).grid(row = 3,column = 2)

Label(root, text = "Select Department").grid(row = 4, column = 1)

optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]
clickedecDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedecDepart, *optionDepart)
inputstdDepart.grid(row= 4, column = 2)

# Label(root, text = "Select the Designation").grid(row = 5,column = 1)
# optionDesig = [ "Professor",
#         "Head of Department",
#           "Assistant Professor"]
# clickedDesig = StringVar()
# OptionMenu(root, clickedDesig, *optionDesig).grid(row = 5, column = 2)

Label(root, text = "Enter the Email ID").grid(row = 5, column = 1)

ecmail = StringVar()
Entry(root, textvariable = ecmail,width = 30).grid(row = 5, column = 2)

Label(root, text = "Enter the Id").grid(row = 6, column = 1)

ecid = StringVar()
Entry(root,textvariable = ecid,width = 30).grid(row = 6,column = 2)


Button(root, text = "Register", command = examofficer_reg,width = 20).grid(row = 7, column = 2)

root.mainloop()