
import os 
import sys
from tkinter import * 
from PIL import ImageTk,Image  
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
from tkinter import ttk
#import phonenumbers
import tkinter as tk

font = 'consolas 11 bold'
font2 = 'consolas 14 bold'

def on_enter0(e):
    e.widget['background'] = '#033500'
    e.widget['foreground'] = 'white'


def on_leave0(e):
    e.widget['background'] = '#3cb043'
    e.widget['foreground'] = 'black'


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
    #print(selCompany)
    
    if inpName.get() == "" or inpEmail.get() == "" or clickedYear.get() == "" or clickedDepart.get() == "" or inpPhone.get() == "" :
        messagebox.showwarning("Warning", "Enter all the fields")
    else:
        import re
        if not re.search(emailValidate, email):
            messagebox.showerror('Invalid email', 'Enter a valid email')
            return
        import re
        matched = re.search(r'^[789]\d{9}$', inpPhone.get().strip())
        if matched is None:
            messagebox.showerror('Invalid number', 'Enter a valid phone number')
            return

        try :
            #insert the values in applied table
            sql = "insert into applied values (%s, %s, %s ,%s, %s, %s)"
            val = (name, email,year, depart, phone, selCompany)
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
            messagebox.showinfo("Message", "Submitted")
            top.destroy()


        except mysql.connector.Error as e :
            print(e)
            messagebox.showerror("Error", "Cannot apply. Make sure to enter your email id")

        finally:
            inpName.set("")
            inpEmail.set("")
            clickedYear.set("")
            clickedDepart.set("")
            inpPhone.set("")






top = Tk()
top.title("Student Information Management System")
top.geometry("500x500")
top.wm_iconbitmap('zicon.ico')



# Label(top, text = "You are Applying for {}".format(sys.argv[1],)).place(x = 30, y = 0)
Label(top, text = "You are Applying for {}".format(sys.argv[1],), font=font2).grid(row=0, column=1, pady=10, padx=10)



# Label(top, text = "Enter your Name").place(x = 20, y = 20)
Label(top, text = "Enter your Name", font=font).grid(row=1, column=0, pady=10, padx=10)

inpName = StringVar()
# Entry(top, width = 30, textvariable = inpName).place(x = 80, y = 20 )
Entry(top, width = 30, textvariable = inpName, font=font).grid(row=1, column=1, pady=10, padx=10)


# Label(top, text = "Enter your Email ID").place(x = 40, y = 50)
Label(top, text = "Enter your Email ID", font=font).grid(row=2, column=0, pady=10, padx=10)

inpEmail = StringVar()
# Entry(top,width = 30,textvariable = inpEmail).place(x = 80, y = 50)
Entry(top,width = 30,textvariable = inpEmail, font=font).grid(row=2, column=1, pady=10, padx=10)

#Label(top, text = "Enter Your Department").place(x = 60, y = 80)

# optionYear = ["FE","SE","TE","BE"]
optionYear = ["BE"]
# stdYear = Label(top, text = "Year").place(x = 20, y = 80)
stdYear = Label(top, text = "Year", font=font).grid(row=3, column=0, pady=10, padx=10)

clickedYear = StringVar()
# inputstdYear = OptionMenu(top, clickedYear , *optionYear).place(x = 80, y = 80)
inputstdYear = OptionMenu(top, clickedYear , *optionYear)
inputstdYear.grid(row=3, column=1, pady=10, padx=10)
inputstdYear.configure(font=font)

optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunincations"]
# stdDepart = Label(top, text = "Department").place(x = 20, y = 110)
stdDepart = Label(top, text = "Department", font=font).grid(row=4, column=0, pady=10, padx=10)

clickedDepart = StringVar()
# inputstdDepart = OptionMenu(top, clickedDepart, *optionDepart).place(x = 80, y = 110)
inputstdDepart = OptionMenu(top, clickedDepart, *optionDepart)
inputstdDepart.grid(row=4, column=1, pady=10, padx=10)
inputstdDepart.configure(font=font)


# Label(top, text = "Phone Number").place(x = 20, y = 140)
Label(top, text = "Phone Number", font=font).grid(row=5, column=0, pady=10, padx=10)


inpPhone = StringVar()
# Entry(top, width = 30, textvariable = inpPhone).place(x = 80, y = 140)
Entry(top, width = 30, textvariable = inpPhone, font=font).grid(row=5, column=1, pady=10, padx=10)

# Button(top, text = "Submit", width = 30, command = submit).place(x = 150, y = 200)
b = Button(top, text = "Submit", width = 30, command = submit, font=font, cursor='hand2')
b.grid(row=6, column=1, pady=10, padx=10)
b.configure(background='#3cb043', font=font)
b.bind("<Enter>", on_enter0)
b.bind("<Leave>", on_leave0)


top.mainloop()