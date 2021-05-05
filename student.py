from tkinter import Tk, Label, Button, Frame
import os
import sys


def exam_details():
    os.system('update_timetable2.py student')


def placement_details():
    pass


def college_info():
    pass


def course_info():
    os.system('course_info.py')


def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


root = Tk()
root.geometry("1000x600+0+0")
root.resizable(False, False)
root.configure(background='#222')
root.title('Student Information Management System')
head = Label(root, text=f'Welcome {sys.argv[1]} {sys.argv[2]}\nwhat would you like to check?', font='consolas 30 bold')
head.pack(pady=(35, 0))
head.configure(background='#222', foreground='white')

f1 = Frame(root, width=300, height=70, borderwidth=10, relief='groove')
f1.configure(background='#999')
f1.pack(pady=(50, 20), anchor='c')
b1 = Button(f1, text='Exam details', command=exam_details, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)
b1.pack()
b1.configure(background='#0277bd')

f2 = Frame(root, width=300, height=70, borderwidth=10, relief='groove')
f2.configure(background='#999')
f2.pack(pady=(20, 20), anchor='c')
b2 = Button(f2, text='Placement details', command=placement_details, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
b2.bind("<Enter>", on_enter)
b2.bind("<Leave>", on_leave)
b2.pack()
b2.configure(background='#0277bd')

f3 = Frame(root, width=300, height=70, borderwidth=10, relief='groove')
f3.configure(background='#999')
f3.pack(pady=(20, 20), anchor='c')
b3 = Button(f3, text='college notifications', command=college_info, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
b3.bind("<Enter>", on_enter)
b3.bind("<Leave>", on_leave)
b3.pack()
b3.configure(background='#0277bd')

f4 = Frame(root, width=300, height=70, borderwidth=10, relief='groove')
f4.configure(background='#999')
f4.pack(pady=(20, 20), anchor='c')
b4 = Button(f4, text='course details', command=course_info, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
b4.bind("<Enter>", on_enter)
b4.bind("<Leave>", on_leave)
b4.pack()
b4.configure(background='#0277bd')

root.mainloop()