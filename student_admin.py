import os
from tkinter import messagebox
from tkinter import *
import mysql.connector
import re
from time import sleep

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="classroom"
# )
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sims"
)
mycursor = mydb.cursor()


def on_enter_del(e):
    e.widget['background'] = '#900d09'
    e.widget['foreground'] = 'white'


def on_leave_del(e):
    e.widget['background'] = '#ea3c53'
    e.widget['foreground'] = 'black'


def on_enterv(e):
    e.widget['background'] = '#fda507'
    e.widget['foreground'] = 'white'


def on_leavev(e):
    e.widget['background'] = '#fee227'
    e.widget['foreground'] = 'black'


def on_enter(e):
    e.widget['background'] = '#710193'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#9867c5'
    e.widget['foreground'] = 'black'



root = Tk()
root.geometry("860x650+0+0")
root.title("Student Details")
root.resizable(False, False)

font = 'consolas 12 bold'

def update_stud():
    regid = inp.get().strip()
    if inp.get().strip() == "":
        messagebox.showinfo('Message', 'Enter Registration ID')

    else:
        show_dt()
        sleep(3)
        os.system(f'student2_admin.py {regid}')


def remove_stud():
    regid = inp.get().strip()
    if inp.get().strip() == "":
        messagebox.showinfo('Message', 'Enter Registration ID')
    else:
        show_dt()
        response = messagebox.askyesno("Warning", "Confirm that you want to remove the student")
        if response == 1:
            try:
                sql = (
                    "delete from login where username = (select username from register where registration_id = {})".format(
                        regid))
                mycursor.execute(sql)
                mydb.commit()
                sql = ("delete from register where registration_id = {}".format(regid))
                mycursor.execute(sql)
                mydb.commit()
                messagebox.showinfo("Message Box", "Student Removed")
            except mysql.connector.Error as e:
                messagebox.showinfo("Error", "Student Not removed")
            finally:
                inp.set("")


def show_dt():
    regid = inp.get().strip()
    if inp.get().strip() == "":
        messagebox.showinfo('Message', 'Enter Registration ID')
    else:
        try:
            # sql = ("select * from register where registerId = {} ".format(regid))
            sql = ("select * from register where registration_Id = {} ".format(regid))
            mycursor.execute(sql)
            res = mycursor.fetchall()
            cnt = 0
            for row in res:
                res = row
                cnt += 1

            if cnt == 0:
                messagebox.showinfo('Not found', 'No details available.\n Make sure to enter a valid ID')
                inp.set('')
                return

            name = res[0] + " " + res[1]
            rid = res[2]
            phone = res[3]
            year = res[4]
            depart = res[5]
            email = res[6]
            sem = res[9]

            Label(root, text=name, font=font).grid(row=1, column=1)
            Label(root, text=rid, font=font).grid(row=2, column=1)
            Label(root, text=phone, font=font).grid(row=3, column=1)
            Label(root, text=year, font=font).grid(row=4, column=1)
            Label(root, text=depart, font=font).grid(row=5, column=1)
            Label(root, text=email, font=font).grid(row=6, column=1)
            Label(root, text=sem, font=font).grid(row=7, column=1)


        except mysql.connector.Error as e:
            messagebox.showerror("Error", "Something Went Wrong !!")


Label(root, text="Enter Registration Id of the student", font=font, pady=10, padx=10).grid(row=0, column=0, pady=10, padx=10)

inp = StringVar()
regIdinp = Entry(root, textvariable=inp, font=font).grid(row=0, column=1, pady=10, padx=10)

showInfo = Button(root, text="Show Details", command=show_dt, font=font, cursor='hand2')
showInfo.grid(row=0, column=2, padx=10, pady=10)
showInfo.bind("<Enter>", on_enterv)
showInfo.bind("<Leave>", on_leavev)
showInfo.configure(background='#fee227')

Label(root, text="Name", font=font).grid(row=1, column=0, pady=10)
Label(root, text="Registration Id", font=font).grid(row=2, column=0, pady=10)
Label(root, text="Phone Number", font=font).grid(row=3, column=0, pady=10)
Label(root, text="Year", font=font).grid(row=4, column=0, pady=10)
Label(root, text="Department", font=font).grid(row=5, column=0, pady=10)
Label(root, text="Email ID", font=font).grid(row=6, column=0, pady=10)
Label(root, text="Semester", font=font).grid(row=7, column=0, pady=10)

updt = Button(root, text="Update Details", command=update_stud, font=font, cursor='hand2')
updt.grid(row=9, column=0, pady=10, padx=10)
updt.bind("<Enter>", on_enter)
updt.bind("<Leave>", on_leave)
updt.configure(background='#9867c5')


rm = Button(root, text="Remove Student", command=remove_stud, font=font, cursor='hand2')
rm.grid(row=9, column=1, padx=10, pady=10)
rm.bind("<Enter>", on_enter_del)
rm.bind("<Leave>", on_leave_del)
rm.configure(background='#ea3c53')
root.mainloop()
