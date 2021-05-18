import os
from tkinter import messagebox
from tkinter import *
import mysql.connector
import re
from time import sleep



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
font = 'consolas 12 bold'

root = Tk()
root.geometry("860x440+0+0")
root.title("Exam Officer Modify")
root.wm_iconbitmap('zicon.ico')
root.resizable(False, False)


def update_examcell():
    ecid = inp.get().strip()
    if inp.get().strip() == "":
        messagebox.showerror("Error", "Enter the Registration ID")
    else:
        showexamcell_dt()
        sleep(3)
        os.system(f'examcell3_admin.py {ecid}')


def remove_examcell():
    ecid = inp.get().strip()
    if inp.get().strip() == "":
        messagebox.showerror("Error", "Enter the Registration ID")
    else:
        showexamcell_dt()
        response = messagebox.askyesno("Warning", "Confirm that you want to remove the exam officer")
        if response == 1:
            try:
                sql1 = ("delete from login where username=(select username from examcell where ecid={})".format(ecid))
                mycursor.execute(sql1)
                mydb.commit()

                sql = ("delete from examcell where ecid = {}".format(ecid))
                mycursor.execute(sql)
                mydb.commit()

                messagebox.showinfo("Message Box", "Exam Officer Removed")
            except mysql.connector.Error as e:
                print(e)
                messagebox.showinfo("Error", "Exam Officer Not removed")
            finally:
                inp.set("")


def showexamcell_dt():
    ecid = inp.get().strip()

    if inp.get().strip() == "":
        messagebox.showerror("Error", "Enter the Exam Officer Id")
    else:
        try:
            sql = ("select * from examcell where ecid = {} ".format(ecid))
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
            depart = res[4]
            email = res[5]

            Label(root, text=name, font=font, pady=10, padx=10).grid(row=1, column=1)
            Label(root, text=rid, font=font, pady=10, padx=10).grid(row=2, column=1)
            Label(root, text=phone, font=font, pady=10, padx=10).grid(row=3, column=1)
            Label(root, text=depart, font=font, pady=10, padx=10).grid(row=4, column=1)
            Label(root, text=email, font=font, pady=10, padx=10).grid(row=5, column=1)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "Something Went Wrong !!")


regId = Label(root, text=" Enter Exam Officer Id", font=font, pady=10, padx=10).grid(row=0, column=0, pady=10, padx=10)
inp = StringVar()
regIdinp = Entry(root, width=30, textvariable=inp, font=font).grid(row=0, column=1, pady=10, padx=10)

showInfo = Button(root, text="Show Details", command=showexamcell_dt, font=font, cursor='hand2')
showInfo.grid(row=0, column=2, pady=10, padx=10)
showInfo.bind("<Enter>", on_enterv)
showInfo.bind("<Leave>", on_leavev)
showInfo.configure(background='#fee227')

Label(root, text="Name", font=font, pady=10, padx=10).grid(row=1, column=0)
Label(root, text="Phone Number", font=font, pady=10, padx=10).grid(row=2, column=0)
Label(root, text="Department", font=font, pady=10, padx=10).grid(row=3, column=0)
Label(root, text="Email Id", font=font, pady=10, padx=10).grid(row=4, column=0)
Label(root, text="Faculty Id", font=font, pady=10, padx=10).grid(row=5, column=0)

rm = Button(root, text="Remove Exam Officer", width=30, command=remove_examcell, font=font, cursor='hand2')
rm.grid(row=6, column=1, pady=10, padx=10)
rm.bind("<Enter>", on_enter_del)
rm.bind("<Leave>", on_leave_del)
rm.configure(background='#ea3c53')

updt = Button(root, text="Update Details", width=30, command=update_examcell, font=font, cursor='hand2')
updt.grid(row=6, column=0, pady=10, padx=10)
updt.bind("<Enter>", on_enter)
updt.bind("<Leave>", on_leave)
updt.configure(background='#9867c5')

root.mainloop()
