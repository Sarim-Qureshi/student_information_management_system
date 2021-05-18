from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
import os
import sys


def on_enter(e):
    e.widget['background'] = '#710193'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#9867c5'
    e.widget['foreground'] = 'black'





def change_password():
    UserName = name.get()
    old_PassWord = password_var_old.get()
    new_PassWord = password_var_new.get()
    newc_PassWord = password_var_new_confirm.get()


    if len(UserName.strip()) == 0 or len(old_PassWord.strip()) == 0 or len(new_PassWord.strip()) == 0 or len(newc_PassWord.strip()) == 0:
        messagebox.showinfo('Empty credentials', 'Enter the credentials to change password')
        return
    if sys.argv[1] == 'student':
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="SIMS")
            cursor = db.cursor()
            cursor.execute("select * from login where username = %s and password = %s", (UserName, old_PassWord,))
            res = cursor.fetchall()

            if len(res) == 0:
                messagebox.showerror('Invalid credentials', 'Enter the correct username and password')
                return
            if not new_PassWord == newc_PassWord:
                messagebox.showerror('Error', 'The new passwords do not match')
                return
            cursor.execute("update login set password = %s where username = %s and password = %s", (new_PassWord, UserName, old_PassWord,))
            db.commit()
            db.close()
            messagebox.showinfo('Password changed', f'{UserName}, your password was changed')
            name.set("")
            password_var_old.set("")
            password_var_new.set("")
            password_var_new_confirm.set("")

        except mysql.connector.Error as e:
            messagebox.showerror('Error', 'Your password could not be changed')

    elif sys.argv[1] == 'faculty':
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="SIMS")
            cursor = db.cursor()
            cursor.execute("select * from login where username = %s and password = %s", (UserName, old_PassWord,))
            res = cursor.fetchall()

            if len(res) == 0:
                messagebox.showerror('Invalid credentials', 'Enter the correct username and password')
                return
            if not new_PassWord == newc_PassWord:
                messagebox.showerror('Error', 'The new passwords do not match')
                return
            q1 = "update login set password = %s where username = %s and password = %s"
            q2 = "update faculty set password = %s where userid = %s and password = %s"
            cursor.execute(q1, (new_PassWord, UserName, old_PassWord,))
            db.commit()
            cursor.execute(q2, (new_PassWord, UserName, old_PassWord,))
            db.commit()
            db.close()
            messagebox.showinfo('Password changed', f'{UserName}, your password was changed')
            name.set("")
            password_var_old.set("")
            password_var_new.set("")
            password_var_new_confirm.set("")

        except mysql.connector.Error as e:
            messagebox.showerror('Error', 'Your password could not be changed')

    elif sys.argv[1] == 'placement':
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="", database="SIMS")
            cursor = db.cursor()
            cursor.execute("select * from login where username = %s and password = %s", (UserName, old_PassWord,))
            res = cursor.fetchall()

            if len(res) == 0:
                messagebox.showerror('Invalid credentials', 'Enter the correct username and password')
                return
            if not new_PassWord == newc_PassWord:
                messagebox.showerror('Error', 'The new passwords do not match')
                return
            q1 = "update login set password = %s where username = %s and password = %s"
            q2 = "update placementofficer set password = %s where username = %s and password = %s"
            cursor.execute(q1, (new_PassWord, UserName, old_PassWord,))
            db.commit()
            cursor.execute(q2, (new_PassWord, UserName, old_PassWord,))
            db.commit()
            db.close()
            messagebox.showinfo('Password changed', f'{UserName}, your password was changed')
            name.set("")
            password_var_old.set("")
            password_var_new.set("")
            password_var_new_confirm.set("")

        except mysql.connector.Error as e:
            messagebox.showerror('Error', 'Your password could not be changed')


root = Tk()
root.geometry("1000x670+0+0")
root.resizable(False, False)
root.configure(background='#222')
root.title('Student Information Management System')
head = Label(root, text='Change password', font='consolas 30 bold')
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

opassword = Label(f1, text='Enter old password:', font='consolas 18 bold')
opassword.grid(row=1, column=0, pady=(20, 20), padx=(70, 20))
opassword.configure(background='#999')

password_var_old = StringVar()
password_entry_old = Entry(f1, textvariable=password_var_old, show='*', font='consolas 17 bold')
password_entry_old.grid(row=1, column=1, pady=(20, 20), padx=(20, 70))

npassword = Label(f1, text='Enter new password:', font='consolas 18 bold')
npassword.grid(row=2, column=0, pady=(20, 20), padx=(70, 20))
npassword.configure(background='#999')

password_var_new = StringVar()
password_entry_new = Entry(f1, textvariable=password_var_new, show='*', font='consolas 17 bold')
password_entry_new.grid(row=2, column=1, pady=(20, 20), padx=(20, 70))

ncpassword = Label(f1, text='Confirm new password:', font='consolas 18 bold')
ncpassword.grid(row=3, column=0, pady=(20, 20), padx=(70, 20))
ncpassword.configure(background='#999')

password_var_new_confirm = StringVar()
password_entry_new_confirm = Entry(f1, textvariable=password_var_new_confirm, show='*', font='consolas 17 bold')
password_entry_new_confirm.grid(row=3, column=1, pady=(20, 20), padx=(20, 70))


b2 = Button(f1, text='Change password', command=change_password, cursor='hand2', font='consolas 18 bold', pady=1, padx=10)
b2.bind("<Enter>", on_enter)
b2.bind("<Leave>", on_leave)
b2.grid(row=4, column=0, columnspan=2, pady=(20, 10), padx=(70, 70))
b2.configure(background='#9867c5')


root.mainloop()
