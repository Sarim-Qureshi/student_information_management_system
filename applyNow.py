
import os 
import sys
from tkinter import * 
from PIL import ImageTk,Image  
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
from tkinter import ttk
import tkinter as tk



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="classroom"
)
mycursor=mydb.cursor()


emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 

def submit():
    name = inpName.get()
    email = inpEmail.get()
    year = clickedYear.get()
    depart = clickedDepart.get()
    phone = inpPhone.get()
    selCompany = sys.argv[1]
    print(selCompany)
    
    if inpName.get() == "":
        messagebox.showwarning("Warning", "Entr Name")
    elif inpEmail.get() == "":
        messagebox.showwarning("warning","Enter Email id")
    elif clickedYear.get() == "":
        messagebox.showwarning("Warning","Enter Year")
    elif clickedDepart.get() == "":
        messagebox.showwarning("Warning","Enter Department")
    elif inpPhone.get() == "" :
        messagebox.showwarning("Warning", "Enter Phone Number")
    else:
        try :
            #insert the values in applied table
            sql = "insert into applied values (%s, %s, %s ,%s, %s)"
            val = (name, email,year, depart, phone)
            mycursor.execute(sql,val)
            mydb.commit()

            #update the students applied column in the placement table
            sql2 = "select applied from placement where company = \"{}\"".format(selCompany)
            mycursor.execute(sql2)
            res = mycursor.fetchall()
            for row in res:
                studint = res[0][0]
            studint+=1

            #sql2 = "update placement set applied  = {}"
            sql3 = "update placement set applied = {} where company = \"{}\"".format(int(studint), selCompany)
            mycursor.execute(sql3)
            mydb.commit()



        except mysql.connector.Error as e :
            print(e)
        
        #print(name, email, year, depart, phone)
        messagebox.showinfo("Message", "Submitted")




top = Tk()
top.title("Apply Now")
top.geometry("500x500")


Label(top, text = "You are Applying for {}".format(sys.argv[1],)).place(x = 30, y = 0)



Label(top, text = "Enter your Name").place(x = 20, y = 20)

inpName = StringVar()
Entry(top, width = 30, textvariable = inpName).place(x = 80, y = 20 )

Label(top, text = "Enter your Email ID").place(x = 40, y = 50)

inpEmail = StringVar()
Entry(top,width = 30,textvariable = inpEmail).place(x = 80, y = 50)

#Label(top, text = "Enter Your Department").place(x = 60, y = 80)

optionYear = ["FE","SE","TE","BE"]
stdYear = Label(top, text = "Year").place(x = 20, y = 80)
clickedYear = StringVar()
inputstdYear = OptionMenu(top, clickedYear , *optionYear).place(x = 80, y = 80)

optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunincations"]
stdDepart = Label(top, text = "Department").place(x = 20, y = 110)
clickedDepart = StringVar()
inputstdDepart = OptionMenu(top, clickedDepart, *optionDepart).place(x = 80, y = 110)


Label(top, text = "Phone Number").place(x = 20, y = 140)

inpPhone = StringVar()
Entry(top, width = 30, textvariable = inpPhone).place(x = 80, y = 140)

Button(top, text = "Submit", width = 30, command = submit).place(x = 150, y = 200)


top.mainloop()