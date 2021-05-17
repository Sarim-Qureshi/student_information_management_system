import os
from tkinter import messagebox
from  tkinter import *
import mysql.connector
import re
import sys
font = 'consolas 12 bold'


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="classroom"
# )
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sims"
)
mycursor=mydb.cursor()

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def on_enter(e):
    e.widget['background'] = '#b29700'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#a8a9ad'
    e.widget['foreground'] = 'black'


def update_stud1():
    firstname = inpfname.get().strip()
    lastname = inplname.get().strip()

    phno = inpph.get().strip()
    year = clickedYear.get()
    depart = clickedDepart.get()
    mail = inpemail.get().strip()
    sem = clickedSem.get()

    if inpfname.get().strip() == "" or inplname.get().strip() == "" or inpph.get().strip() == "" or clickedYear.get() == "" or clickedDepart.get() == "" or clickedSem.get=="":
        messagebox.showwarning("Empty fields", "Enter all the Details")

    else:
        if re.search(emailValidate, mail) and re.search(r'^[789]\d{9}$', phno):
            try:
                # sql = ("UPDATE register SET firstname = %s, lastname = %s, registerId = %s, phoneNumber = %s, year= %s,depart = %s WHERE registerId = {}".format(sys.argv[1]))
                sql=("UPDATE register SET firstname=%s,lastname=%s,registration_id=%s,phone_no=%s,year=%s,"
                     "department=%s, email=%s,"
                     " sem=%s WHERE registration_id = {}".format(sys.argv[1]))
                values = (firstname, lastname, rid, phno, year, depart, mail, sem)
                mycursor.execute(sql, values)
                mydb.commit()
                messagebox.showinfo("Message","Details Updated Sucessfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error","Some Error Occured")

            finally:
                root.destroy()
        else:
            messagebox.showerror('Message', 'Ensure that phone number and email ID are valid')




root = Tk()
root.geometry("1300x650+0+0")
root.title("Student Details")
root.resizable(False,False)

Label(root,text = "Old Details", font=font, pady=30, padx=10).grid(row = 0, column = 1)

Label(root,text = "First Name", font=font, pady=5, padx=10).grid(row = 1, column = 0)
Label(root,text = "Last Name", font=font, pady=5, padx=10).grid(row = 2, column = 0)
Label(root,text = "Registration Id", font=font, pady=5, padx=10).grid(row = 3, column = 0)
Label(root,text = "Phone Number", font=font, pady=5, padx=10).grid(row = 4, column = 0)
Label(root, text = "Year", font=font, pady=5, padx=10).grid(row = 5, column = 0)
Label(root, text = "Department", font=font, pady=5, padx=10).grid(row = 6, column = 0)
Label(root, text = "Email ID", font=font, pady=5, padx=10).grid(row = 7, column = 0)
Label(root, text = "Semester", font=font, pady=5, padx=10).grid(row = 8, column = 0)




try :
    
    sql = ("select * from register where registration_id = {} ".format(sys.argv[1]))
    mycursor.execute(sql)
    res = mycursor.fetchall()
    res=res[0]

    fname = res[0]
    lname = res[1]
    rid = res[2]
    phone = res[3]
    year = res[4]
    depart = res[5]
    email = res[6]
    sem = res[9]

    Label(root,text = fname, font=font, pady=5, padx=10).grid(row = 1, column = 1)
    Label(root,text = lname, font=font, pady=5, padx=10).grid(row = 2, column = 1)
    Label(root,text = rid, font=font, pady=5, padx=10).grid(row = 3, column = 1)
    Label(root,text = phone, font=font, pady=5, padx=10).grid(row = 4, column = 1)
    Label(root, text = year, font=font, pady=5, padx=10).grid(row = 5, column = 1)
    Label(root, text = depart, font=font, pady=5, padx=10).grid(row = 6, column = 1)
    Label(root, text = email, font=font, pady=5, padx=10).grid(row = 7, column = 1)
    Label(root, text = sem, font=font, pady=5, padx=10).grid(row = 8, column = 1)

except mysql.connector.Error as e:
    print(e)
    messagebox.showerror("Error", "Something went wrong !!")


Label(root, text = "Enter Here New Details to Update/Change", font=font, pady=30, padx=10).grid(row = 0 ,column = 3)

Label(root,text = "First Name", font=font, pady=5, padx=50).grid(row = 1, column = 3)
Label(root,text = "Last Name", font=font, pady=5, padx=50).grid(row = 2, column = 3)
Label(root,text = "Registration Id", font=font, pady=5, padx=50).grid(row = 3, column = 3)
Label(root,text = "Phone Number", font=font, pady=5, padx=50).grid(row = 4, column = 3)
Label(root, text = "Year", font=font, pady=5, padx=50).grid(row = 5, column = 3)
Label(root, text = "Department", font=font, pady=5, padx=50).grid(row = 6, column = 3)
Label(root, text = "Email ID", font=font, pady=5, padx=50).grid(row = 7, column = 3)
Label(root, text = "Semester", font=font, pady=5, padx=50).grid(row = 8, column = 3)


inpfname = StringVar()
Entry(root,width = 30,textvariable = inpfname, font=font).grid(row = 1, column = 4, pady=5, padx=10)

inplname = StringVar()
Entry(root,width = 30,textvariable = inplname, font=font).grid(row = 2, column = 4, pady=5, padx=10)

rid = sys.argv[1]
Label(root,text = rid, font=font).grid(row = 3,column = 4, pady=5, padx=10)

inpph = StringVar()
Entry(root,width = 30,textvariable = inpph, font=font).grid(row = 4, column = 4, pady=5, padx=10)


optionYear = ["FE", "SE", "TE", "BE"]
clickedYear = StringVar()
inputstdYear = OptionMenu(root, clickedYear, *optionYear,)
inputstdYear.grid(row = 5, column = 4, pady=5, padx=10)
inputstdYear.configure(font=font)


optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]
clickedDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedDepart, *optionDepart)
inputstdDepart.grid(row= 6, column = 4, pady=5, padx=10)
inputstdDepart.configure(font=font)

inpemail = StringVar()
Entry(root,width = 30,textvariable = inpemail, font=font).grid(row = 7, column = 4, pady=5, padx=10)
# Label(root,width = 30, text = email).grid(row = 16, column = 2)

# inpsem = StringVar()
# Entry(root,width = 30,textvariable = inpsem).grid(row = 17, column = 1)

optionSem = ["1", "2", "3", "4", "5", "6", "7", "8"]
# stdSem = Label(root, text="Semester", font='consolas 15 bold')
# stdSem.grid(row=5, column=0, pady=(15, 15), padx=(70, 20))
# stdSem.configure(background='#999')

clickedSem = StringVar()
inputstdSem = OptionMenu(root, clickedSem, *optionSem,)
inputstdSem.grid(row=8, column=4, pady=5, padx=10)
inputstdSem.configure(font=font)

b = Button(root, text = "Update Details",width = 30,command = update_stud1, font=font, cursor='hand2')
b.grid(row = 9, column = 4, pady=5, padx=10)
b.configure(background='#a8a9ad')
b.bind("<Enter>", on_enter)
b.bind("<Leave>", on_leave)

root.mainloop()