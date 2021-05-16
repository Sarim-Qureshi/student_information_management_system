from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
import os
import sys


def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


def on_enterc(e):
    e.widget['background'] = '#bbb'
    e.widget['foreground'] = '#222'


def on_leavec(e):
    e.widget['background'] = '#222'
    e.widget['foreground'] = '#bbb'


def on_enter2(e):
    e.widget['background'] = '#033500'
    e.widget['foreground'] = 'white'


def on_leave2(e):
    e.widget['background'] = '#3cb043'
    e.widget['foreground'] = 'black'


# root = Tk()
# root.title("Login Page")
# root.geometry("400x400")

db = mysql.connector.connect(host="localhost", user="root", password="", database="SIMS")
cursor = db.cursor()



def change_pass():
    os.system('change_password.py')

def login():
    UserName = name.get()
    PassWord = password_var.get()

    if len(UserName.strip()) == 0 or len(PassWord.strip()) == 0:
        messagebox.showinfo('Empty credentials', 'Enter the credentials to login')
        return

    try:
        cursor.execute("select password from login where username = %s and role=%s", (UserName, sys.argv[1],))
        res = cursor.fetchall()

        if len(res) == 0:
            if sys.argv[1] == 'student':
                messagebox.showerror('Invalid username', 'Enter the correct username to login '
                                                     'or create an account if you do not have one')
            else:
                messagebox.showerror('Invalid username', 'Enter the correct username to login')
        else:
            db_pass = (res[0])[0]
            if db_pass != PassWord:
                messagebox.showerror('Invalid password', 'Enter the correct password to login')
            else:
                if sys.argv[1] == 'student':
                    cursor.execute("select * from register where username=%s", (UserName,))
                    res = cursor.fetchall()
                    fn = ((res[0])[0]).strip()
                    ln = ((res[0])[1]).strip()
                    ri = (str((res[0])[2])).strip()
                    os.system(f'student.py {fn} {ln} {ri}')
                else:
                    if sys.argv[1] == 'exam':
                        os.system('exam.py '+UserName)
                    elif sys.argv[1] == 'placement':
                        os.system('addremove_admin.py')
                    # os.system(sys.argv[1]+'.py '+UserName)
                    elif sys.argv[1] == 'faculty':
                        os.system('faculty.py')
    except mysql.connector.Error as e:
        messagebox.showerror('Error', 'An error occured. Try again after some time')

    finally:
        name.set("")
        password_var.set("")


def register():
    os.system("register.py student")


# ----------------------------------------------
root = Tk()
root.geometry("1000x670+0+0")
root.resizable(False, False)
root.configure(background='#222')
root.title('Student Information Management System')
head = Label(root, text='Login Page', font='consolas 30 bold')
head.pack(pady=(35, 0))
head.configure(background='#222', foreground='white')

f1 = Frame(root, width=800, height=500, borderwidth=10, relief='groove')
f1.configure(background='#999')
f1.pack(pady=(50, 20), padx=(60, 5), anchor='c')

username = Label(f1, text='Enter username:', font='consolas 18 bold')
username.grid(row=0, column=0, pady=(45, 20), padx=(70, 20))
username.configure(background='#999')

name = StringVar()
name_entry = Entry(f1, textvariable=name, font='consolas 17 bold')
name_entry.grid(row=0, column=1, pady=(45, 20), padx=(20, 70))

password = Label(f1, text='Enter password:', font='consolas 18 bold')
password.grid(row=1, column=0, pady=(20, 20), padx=(70, 20))
password.configure(background='#999')

password_var = StringVar()
password_entry = Entry(f1, textvariable=password_var, show='*', font='consolas 17 bold')
password_entry.grid(row=1, column=1, pady=(20, 20), padx=(20, 70))


b2 = Button(f1, text='Login', command=login, cursor='hand2', font='consolas 18 bold', pady=1, padx=10)
b2.bind("<Enter>", on_enter)
b2.bind("<Leave>", on_leave)
b2.grid(row=2, column=0, columnspan=2, pady=(20, 10), padx=(70, 70))
b2.configure(background='#0277bd')



if sys.argv[1] == 'student':
    b2 = Button(f1, text='Change password', command=change_pass, cursor='hand2', font='consolas 15 bold', pady=1,
                padx=10)
    b2.bind("<Enter>", on_enterc)
    b2.bind("<Leave>", on_leavec)
    b2.grid(row=3, column=0, columnspan=2, pady=(20, 10), padx=(70, 70))
    b2.configure(background='#222', foreground='#bbb')

    reg_label = Label(f1, text="Do not have an account?\nClick register button below to create one.",
                      font='consolas 17 bold')
    reg_label.configure(background='#999', foreground='#900d09')
    reg_label.grid(row=4, column=0, columnspan=2, pady=(10, 10), padx=(70, 70))

    b3 = Button(f1, text='Register', command=register, cursor='hand2', font='consolas 18 bold', pady=1, padx=10)
    b3.bind("<Enter>", on_enter2)
    b3.bind("<Leave>", on_leave2)
    b3.grid(row=5, column=0, columnspan=2, pady=(10, 20), padx=(70, 70))
    b3.configure(background='#3cb043')

root.mainloop()
# ----------------------------------------------


# Label(root, text="Login To Your Account").place(x=150, y=30)
#
# inpUserName = StringVar()
# userName = Label(root, text="User Name").place(x=20, y=70)
# inputusername = Entry(root, width=40, textvariable=inpUserName).place(x=100, y=70)
#
# inpPass = StringVar()
# passWord = Label(root, text="Password").place(x=20, y=100)
# inputpass = Entry(root, width=40, textvariable=inpPass).place(x=100, y=100)
#
# Button(root, text="Login", command=login).place(x=150, y=150)
#
# Label(root, text="If you Dont have an Account create one.\nTo Register click the below button").place(x=100, y=200)
# Button(root, text="Register Now", command=calverify).place(x=150, y=250)
