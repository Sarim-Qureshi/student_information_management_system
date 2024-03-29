import os
from tkinter import messagebox
from  tkinter import *
import mysql.connector


root = Tk()
root.geometry("1100x600+0+0")
root.title("Admin Section")
root.resizable(False,False)
root.wm_iconbitmap('zicon.ico')
root.configure(background='#222')


def handle_radio():
    if var.get() == 'NA':
        return
    else:
        if var.get() == 'student':
            os.system('student_admin.py')
        elif var.get() == 'exam':
            os.system('examcell_admin.py')
        elif var.get() == 'placement':
            os.system('placement_admin.py ')
        elif var.get() == 'faculty':
            os.system('faculty_admin.py')


def on_enter(e):
    b['background'] = '#033500'
    b['foreground'] = 'white'


def on_leave(e):
    b['background'] = '#3cb043'
    b['foreground'] = 'black'

head = Label(root, text='Welcome ADMIN, Choose the role to Edit', font='consolas 30 bold')
head.pack(pady=(35, 0))
head.configure(background='#222', foreground='white')

f = Frame(root, width=300, height=100, borderwidth=30, relief='groove')
f.configure(background='#999')
f.pack(pady=50)

# l = Label(f, text='Choose your role', font='consolas 22 bold', padx=15)
# l.pack(pady=(20, 15))
# l.configure(background='#999', foreground='#111')
var = StringVar()
var.set('NA')
r1 = Radiobutton(f, text='Student', variable=var, value='student', padx=30, font='consolas 14 bold')
r1.pack(pady=5, anchor='w')
r1.configure(background='#999', foreground='#111')
r2 = Radiobutton(f, text='Faculty', variable=var, value='faculty', padx=30, font='consolas 14 bold')
r2.pack(pady=5, anchor='w')
r2.configure(background='#999', foreground='#111')
r3 = Radiobutton(f, text='Exam section', variable=var, value='exam', padx=30, font='consolas 14 bold')
r3.pack(pady=5, anchor='w')
r3.configure(background='#999', foreground='#111')
r4 = Radiobutton(f, text='Placement Cell', variable=var, value='placement', padx=30, font='consolas 14 bold')
r4.pack(pady=5, anchor='w')
r4.configure(background='#999', foreground='#111')




b = Button(f, text='Next', command=handle_radio, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
b.bind("<Enter>", on_enter)
b.bind("<Leave>", on_leave)
b.pack(pady=(10, 20))
b.configure(background='#3cb043')



root.mainloop()
