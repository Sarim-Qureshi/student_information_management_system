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


font = 'consolas 12 bold'
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

root = Tk()
root.geometry("860x440+0+0")
root.title("Modify Placement Officer Details")
root.resizable(False, False)


def update_place():
    plid = inp.get().strip()
    if inp.get().strip() == "":
        messagebox.showerror("Error", "Enter the Placement Officer ID")
    else:
        showplace_dt()
        sleep(3)
        os.system(f'placement3_admin.py {plid}')


def remove_place():
    regid = inp.get().strip()
    if inp.get().strip() == "":
        messagebox.showerror("Error", "Enter the Placement Officer ID")
    else:
        showplace_dt()
        response = messagebox.askyesno("Warning", "Confirm that you want to remove the Placement Officer")
        if response == 1:
            try:
                sql1 = ("delete from login where username=(select username from placementofficer where plid={})".format(regid))
                mycursor.execute(sql1)
                mydb.commit()
                sql = ("delete from placementofficer where plid = {}".format(regid))
                mycursor.execute(sql)
                mydb.commit()
                messagebox.showinfo("Message Box", "Placement Officer Removed")
            except mysql.connector.Error as e:
                messagebox.showinfo("Error", "Placement Officer Not removed")
            finally:
                inp.set("")


def showplace_dt():
    plid = inp.get().strip()

    if inp.get().strip() == "":
        messagebox.showerror("Error", "Enter the Placement Officer Id")
    else:
        try:
            sql = ("select * from placementofficer where plid = {} ".format(plid))
            mycursor.execute(sql)
            res = mycursor.fetchall()
            for row in res:
                res = row

                name = res[0] + " " + res[1]
                rid = res[2]
                phone = res[3]
                # year = res[4]
                depart = res[5]
                email = res[6]

            Label(root, text=name, font=font, pady=10, padx=10).grid(row=1, column=1)
            Label(root, text=rid, font=font, pady=10, padx=10).grid(row=2, column=1)
            Label(root, text=phone, font=font, pady=10, padx=10).grid(row=3, column=1)
            # yr = Label(root, text = year).grid(row = 4, column = 2)
            Label(root, text=depart, font=font, pady=10, padx=10).grid(row=4, column=1)
            Label(root, text=email, font=font, pady=10, padx=10).grid(row=5, column=1)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "Something Went Wrong !!")


regId = Label(root, text=" Enter Placement Officer Id", font=font, pady=10, padx=10).grid(row=0, column=0)
inp = StringVar()
regIdinp = Entry(root, width=30, textvariable=inp, font=font).grid(row=0, column=1, pady=10, padx=10)

showInfo = Button(root, text="Show Details", command=showplace_dt, font=font, cursor='hand2')
showInfo.grid(row=0, column=2, pady=10, padx=10)
showInfo.bind("<Enter>", on_enterv)
showInfo.bind("<Leave>", on_leavev)
showInfo.configure(background='#fee227')

Label(root, text="Name", font=font, pady=10, padx=10).grid(row=1, column=0)
Label(root, text="Phone Number", font=font, pady=10, padx=10).grid(row=2, column=0)
Label(root, text="Department", font=font, pady=10, padx=10).grid(row=3, column=0)
Label(root, text="Email Id", font=font, pady=10, padx=10).grid(row=4, column=0)
Label(root, text="Placement Officer Id", font=font, pady=10, padx=10).grid(row=5, column=0)

rm = Button(root, text="Remove Placement Officer", width=30, command=remove_place, font=font, cursor='hand2')
rm.grid(row=6, column=1, pady=10, padx=10)
rm.bind("<Enter>", on_enter_del)
rm.bind("<Leave>", on_leave_del)
rm.configure(background='#ea3c53')

updt = Button(root, text="Update Details", width=30, command=update_place, font=font, cursor='hand2')
updt.grid(row=6, column=0, pady=10, padx=10)
updt.bind("<Enter>", on_enter)
updt.bind("<Leave>", on_leave)
updt.configure(background='#9867c5')

root.mainloop()
