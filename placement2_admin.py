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
root.title("Placement Officer Remove")
root.resizable(False,False)

def update_place():
  plid = inp.get().strip()
  if inp.get().strip() == "":
    messagebox.showerror("Error","Enter the Placement Officer ID")
  else:
    showplace_dt()
    sleep(3)
    os.system(f'placement3_admin.py {plid}')
  



def remove_place():
  regid = inp.get().strip()
  if inp.get().strip() == "":
    messagebox.showerror("Error","Enter the Placement Officer ID")
  else:
    showplace_dt()
    response = messagebox.askyesno("Warning","Do you confirm want to remove the Officer ?")
    if response == 1:
        try :
            sql = ("delete from placementofficer where plid = {}".format(regid))
            mycursor.execute(sql)

            sql1 = ("delete from login where roleid = {}".format(regid))
            mycursor.execute(sql1)
            mydb.commit()
            messagebox.showinfo("Message Box","Placement Officer Removed")
        except mysql.connector.Error as e:
            messagebox.showinfo("Error","Placement Officer Not removed")
        finally:
            inp.set("")

def showplace_dt():
  plid = inp.get().strip()
  
  if inp.get().strip() == "":
        messagebox.showerror("Error","Enter the Placement Officer Id")
  else:
    try :
        sql = ("select * from placementofficer where plid = {} ".format(plid))
        mycursor.execute(sql)
        res = mycursor.fetchall()
        for row in res:
            res = row

            name = res[0]+" "+res[1]
            rid = res[2]
            phone = res[3]
            #year = res[4]
            depart = res[5]
            email = res[6]

        name = Label(root,text = name).grid(row = 1, column = 2)
        rgid = Label(root,text = rid).grid(row = 2, column = 2)
        pho = Label(root,text = phone).grid(row = 3, column = 2)
        #yr = Label(root, text = year).grid(row = 4, column = 2)
        dep = Label(root, text = depart).grid(row = 5, column = 2)
        mail = Label(root, text = email).grid(row = 6, column =2)
    except mysql.connector.Error as e:
        messagebox.showerror("Error","Something Went Wrong !!")



Label(root,text = "Remove Placement Officer").grid(row = 0, column = 2)
regId = Label(root, text = " Enter Placement Officer Id").grid(row=0, column=0, pady=10, padx=10)
inp = StringVar()
regIdinp = Entry(root, width = 30,textvariable = inp).grid(row = 0, column = 2)

showInfo =  Button(root,text = "Show Details",command = showplace_dt).grid(row = 0,column =3)

Label(root,text = "Name").grid(row = 1, column = 1)
Label(root,text = "Phone Number").grid(row = 2, column = 1)
Label(root,text = "Department").grid(row = 3, column = 1)
#Label(root, text = "Designation").grid(row = 4, column = 1)
Label(root, text = "Email Id").grid(row = 5, column = 1)
Label(root, text = "Placement Officer Id").grid(row = 6, column = 1)


Button(root,text = "Remove Placement Officer",width = 30,command = remove_place).grid(row = 7, column = 1)
Button(root,text = "Update Details",width = 30,command = update_place).grid(row = 7, column =2)



root.mainloop()