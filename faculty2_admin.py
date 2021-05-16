import os
from tkinter import messagebox
from  tkinter import *
import mysql.connector
import re
from time import sleep

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="classroom"
)
mycursor=mydb.cursor()

root = Tk()
root.geometry("650x650")
root.title("Faculty Remove")
root.resizable(False,False)

def update_fac():
  facid = inp.get().strip()
  if inp.get().strip() == "":
    messagebox.showerror("Error","Enter the Registration ID")
  else:
    showfac_dt()
    sleep(3)
    os.system(f'faculty3_admin.py {facid}')
  



def remove_fac():
  regid = inp.get().strip()
  if inp.get().strip() == "":
    messagebox.showerror("Error","Enter the Registration ID")
  else:
    showfac_dt()
    response = messagebox.askyesno("Warning","Do you confirm want to remove the student ?")
    if response == 1:
        try :
            sql = ("delete from faculty where fid = {}".format(regid))
            mycursor.execute(sql)

            sql1 = ("delete from login where roleid = {}".format(regid))
            mycursor.execute(sql1)
            mydb.commit()
            messagebox.showinfo("Message Box","Faculty Removed")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error","Faculty Not removed")
        finally:
            inp.set("")

def showfac_dt():
  facid = inp.get().strip()
  
  if inp.get().strip() == "":
        messagebox.showerror("Error","Enter the Faculty Id")
  else:
    try :
        sql = ("select * from faculty where fid = {} ".format(facid))
        mycursor.execute(sql)
        res = mycursor.fetchall()
        for row in res:
            res = row

            name = res[0]+" "+res[1]
            rid = res[2]
            phone = res[3]
            year = res[4]
            depart = res[5]
            email = res[6]

        name = Label(root,text = name).grid(row = 1, column = 2)
        rgid = Label(root,text = rid).grid(row = 2, column = 2)
        pho = Label(root,text = phone).grid(row = 3, column = 2)
        yr = Label(root, text = year).grid(row = 4, column = 2)
        dep = Label(root, text = depart).grid(row = 5, column = 2)
        mail = Label(root, text = email).grid(row = 6, column =2)
    except mysql.connector.Error as e:
        messagebox.showerror("Error","Something Went Wrong !!")



Label(root,text = "Remove Faculty").grid(row = 0, column = 2)
regId = Label(root, text = " Enter Faculty Id").grid(row=0, column=0, pady=10, padx=10)
inp = StringVar()
regIdinp = Entry(root, width = 30,textvariable = inp).grid(row = 0, column = 2)

showInfo =  Button(root,text = "Show Details",command = showfac_dt).grid(row = 0,column =3)

Label(root,text = "Name").grid(row = 1, column = 1)
Label(root,text = "Phone Number").grid(row = 2, column = 1)
Label(root,text = "Department").grid(row = 3, column = 1)
Label(root, text = "Designation").grid(row = 4, column = 1)
Label(root, text = "Email Id").grid(row = 5, column = 1)
Label(root, text = "Faculty Id").grid(row = 6, column = 1)


Button(root,text = "Remove Faculty",width = 30,command = remove_fac).grid(row = 7, column = 1)
Button(root,text = "Update Details",width = 30,command = update_fac).grid(row = 7, column =2)



root.mainloop()