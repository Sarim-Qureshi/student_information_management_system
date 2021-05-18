from tkinter import Tk, Label, Button, Frame
import os


def add_examofficer():
    os.system('examcelladd_admin.py')


def change_details():
    os.system('examcell2_admin.py')


def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


root = Tk()
root.geometry("1000x500+0+0")
root.resizable(False, False)
root.title('Student Information Management System')
root.configure(background='#222')
head = Label(root, text='Modify Exam Section Staff', font='consolas 30 bold')
head.pack(pady=(35, 0))
head.configure(background='#222', foreground='white')

f1 = Frame(root, width=300, height=70, borderwidth=10, relief='groove')
f1.configure(background='#999')
f1.pack(pady=(50, 20), anchor='c')
b1 = Button(f1, text='Add Exam Officer', command=add_examofficer, cursor='hand2', font='consolas 14 bold', pady=1,
            padx=10)
b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)
b1.pack()
b1.configure(background='#0277bd')

f2 = Frame(root, width=300, height=70, borderwidth=10, relief='groove')
f2.configure(background='#999')
f2.pack(pady=(20, 20), anchor='c')
b2 = Button(f2, text='Remove/Update Details of Exam Officer', command=change_details, cursor='hand2',
            font='consolas 14 bold', pady=1, padx=10)
b2.bind("<Enter>", on_enter)
b2.bind("<Leave>", on_leave)
b2.pack()
b2.configure(background='#0277bd')

root.mainloop()
