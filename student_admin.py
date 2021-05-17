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
root.title("Student Details")
root.resizable(False,False)


def update_stud():
    regid = inp.get().strip()
    if inp.get().strip() == "":
        messagebox.showerror("Error","Enter the Registration ID")
    else:
        show_dt()
        sleep(3)
        os.system(f'student2_admin.py {regid}')



def remove_stud():
    regid = inp.get().strip()
    if inp.get().strip() == "":
        messagebox.showerror("Error","Enter the Registration ID")
    else:
        show_dt()
        response = messagebox.askyesno("Warning","Do you confirm want to remove the student ?")
        if response == 1:
            try :
                sql = ("delete from register where registerId = {}".format(regid))
                mycursor.execute(sql)
                mydb.commit()
                messagebox.showinfo("Message Box","Student Removed")
            except mysql.connector.Error as e:
                messagebox.showinfo("Error","Student Not removed")
            finally:
                inp.set("")
               

def show_dt():
    regid = inp.get().strip()
    if inp.get().strip() == "":
        messagebox.showerror("Error","Enter the Registration ID")
    else:

        try :
            sql = ("select * from register where registerId = {} ".format(regid))
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
        
        
            

regId = Label(root, text = " Enter Register Id of Student ").grid(row=0, column=0, pady=10, padx=10)

inp = StringVar()
regIdinp = Entry(root, width = 30,textvariable = inp).grid(row = 0, column = 2)

showInfo =  Button(root,text = "Show Details",command = show_dt).grid(row = 0,column =3)


Label(root,text = "Name").grid(row = 1, column = 1)
Label(root,text = "Registration Id").grid(row = 2, column = 1)
Label(root,text = "Phone Number").grid(row = 3, column = 1)
Label(root, text = "Year").grid(row = 4, column = 1)
Label(root, text = "Department").grid(row = 5, column = 1)
Label(root, text = "Email ID").grid(row = 6, column =1)

updt = Button(root, text = "Update Details", command = update_stud).grid(row = 8, column = 1)
            
rm = Button(root, text = "Remove Student", command = remove_stud).grid(row = 8, column = 2)

root.mainloop()

