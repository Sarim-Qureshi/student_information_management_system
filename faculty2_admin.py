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
mycursor = mydb.cursor()

root = Tk()
root.geometry("650x650+0+0")
root.title("Modify Faculty Details")
root.resizable(False, False)


def update_fac():
    facid = inp.get().strip()
    if inp.get().strip() == "":
        messagebox.showinfo('Message', 'Enter Registration ID')
    else:
        showfac_dt()
        sleep(3)
        os.system(f'faculty3_admin.py {facid}')


def remove_fac():
    regid = inp.get().strip()
    if inp.get().strip() == "":
        messagebox.showinfo('Message', 'Enter Registration ID')
    else:
        showfac_dt()
        response = messagebox.askyesno("Warning", "Confirm that want to remove the faculty")
        if response == 1:
            try:

                sql1 = ("delete from login where username=(select userid from faculty where fid={})".format(regid))
                mycursor.execute(sql1)
                mydb.commit()

                sql = ("delete from faculty where fid = {}".format(regid))
                mycursor.execute(sql)
                mydb.commit()


                messagebox.showinfo("Message Box", "Faculty Removed")
            except mysql.connector.Error as e:
                messagebox.showinfo("Error", "Faculty Not removed")
            finally:
                inp.set("")


def showfac_dt():
    facid = inp.get().strip()

    if inp.get().strip() == "":
        messagebox.showinfo('Message', 'Enter Registration ID')
    else:
        try:
            sql = ("select * from faculty where fid = {} ".format(facid))
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

            res = res[0]
            name = res[0] + " " + res[1]
            rid = res[2]
            phone = res[3]
            year = res[4]
            depart = res[5]
            email = res[6]

            Label(root, text=name, font=font, pady=10, padx=10).grid(row=1, column=1)
            Label(root, text=rid, font=font, pady=10, padx=10).grid(row=2, column=1)
            Label(root, text=phone, font=font, pady=10, padx=10).grid(row=3, column=1)
            Label(root, text=year, font=font, pady=10, padx=10).grid(row=4, column=1)
            Label(root, text=depart, font=font, pady=10, padx=10).grid(row=5, column=1)
            Label(root, text=email, font=font, pady=10, padx=10).grid(row=6, column=1)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", "Something Went Wrong !!")


# Label(root, text="Remove Faculty").grid(row=0, column=2)
regId = Label(root, text=" Enter Faculty Id", font=font, pady=10, padx=10).grid(row=0, column=0)
inp = StringVar()
regIdinp = Entry(root, width=30, textvariable=inp, font=font).grid(row=0, column=1, pady=10, padx=10)

showInfo = Button(root, text="Show Details", command=showfac_dt, font=font, cursor='hand2')
showInfo.grid(row=0, column=2, pady=10, padx=10)
showInfo.bind("<Enter>", on_enterv)
showInfo.bind("<Leave>", on_leavev)
showInfo.configure(background='#fee227')

Label(root, text="Name", font=font, pady=10, padx=10).grid(row=1, column=0)
Label(root, text="Phone Number", font=font, pady=10, padx=10).grid(row=2, column=0)
Label(root, text="Department", font=font, pady=10, padx=10).grid(row=3, column=0)
Label(root, text="Designation", font=font, pady=10, padx=10).grid(row=4, column=0)
Label(root, text="Email Id", font=font, pady=10, padx=10).grid(row=5, column=0)
Label(root, text="Faculty Id", font=font, pady=10, padx=10).grid(row=6, column=0)

rm = Button(root, text="Remove Faculty", command=remove_fac, font=font, cursor='hand2')
rm.grid(row=7, column=1, pady=10, padx=10)
rm.bind("<Enter>", on_enter_del)
rm.bind("<Leave>", on_leave_del)
rm.configure(background='#ea3c53')

updt = Button(root, text="Update Details", command=update_fac, font=font, cursor='hand2')
updt.grid(row=7, column=0, pady=10, padx=10)
updt.bind("<Enter>", on_enter)
updt.bind("<Leave>", on_leave)
updt.configure(background='#9867c5')

root.mainloop()
