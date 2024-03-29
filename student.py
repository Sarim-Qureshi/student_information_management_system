from tkinter import Tk, Label, Button, Frame
import os
import sys


def exam_details():
    os.system('update_timetable2.py student')


def placement_details():
    os.system(f'placement.py {sys.argv[4]}')


def college_info():
    os.system('enter_notification.py')


def course_info():
    os.system('course_info.py')


def marks():
    os.system(f'update_marks.py {sys.argv[3]}')


def attendance():
    os.system(f'view_attendance.py {sys.argv[3]}')


def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


root = Tk()
root.geometry("1000x690+0+0")
root.resizable(False, False)
root.configure(background='#222')
root.wm_iconbitmap('zicon.ico')
root.title('Student Information Management System')
head = Label(root, text=f'Welcome {sys.argv[1]} {sys.argv[2]}, what would you like to check?', font='consolas 24 bold')
head.pack(pady=(30, 0))
head.configure(background='#222', foreground='white')

f1 = Frame(root, width=300, height=70, borderwidth=10, relief='groove')
f1.configure(background='#999')
f1.pack(pady=(35, 20), anchor='c')
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

f5 = Frame(root, width=300, height=70, borderwidth=10, relief='groove')
f5.configure(background='#999')
f5.pack(pady=(20, 20), anchor='c')
b5 = Button(f5, text='Exam results', command=marks, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
b5.bind("<Enter>", on_enter)
b5.bind("<Leave>", on_leave)
b5.pack()
b5.configure(background='#0277bd')

f6 = Frame(root, width=300, height=70, borderwidth=10, relief='groove')
f6.configure(background='#999')
f6.pack(pady=(20, 20), anchor='c')
b6 = Button(f6, text='Check attendance', command=attendance, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
b6.bind("<Enter>", on_enter)
b6.bind("<Leave>", on_leave)
b6.pack()
b6.configure(background='#0277bd')

root.mainloop()