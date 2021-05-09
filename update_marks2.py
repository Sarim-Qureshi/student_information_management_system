from tkinter import *
import mysql.connector
import sys


def on_enter0(e):
    e.widget['background'] = '#033500'
    e.widget['foreground'] = 'white'


def on_leave0(e):
    e.widget['background'] = '#3cb043'
    e.widget['foreground'] = 'black'


def update():
    try:
        rid = str(ls.get(ls.curselection())[2])
        fn = str(ls.get(ls.curselection())[0])
        ln = str(ls.get(ls.curselection())[1])
    except:
        return
    import os
    os.system(f'update_marks3.py {tablename} {rid} {fn} {ln} {dept}')


root = Tk()
root.geometry("1000x670+0+0")
root.resizable(False, False)
root.title('Student Information Management System')
root.configure(background='#222')
# if sys.argv[1] != 'student':
head = Label(root, text='Update marks', font='consolas 30 bold')
# else:
#     head = Label(root, text='View timetables', font='consolas 30 bold')
head.pack(pady=(20, 0))
head.configure(background='#222', foreground='white')
head2 = Label(root, text='Student names with registration id', font='consolas 25 bold')
head2.pack(pady=(10, 0))
head2.configure(background='#222', foreground='white')

f1 = Frame(root, width=600, height=300, borderwidth=10, relief='groove')
f1.configure(background='#999')
f1.pack(pady=(50, 20), padx=(60, 5), anchor='c')

sb = Scrollbar(f1)
sb.pack(side='right', fill='y')
ls = Listbox(f1, yscrollcommand=sb.set, width=40, height=10)
ls.config(font='comicsanms 18 bold')
ls.pack()
sb.config(command=ls.yview)
db = mysql.connector.connect(host='localhost', user='root', password='', database='sims')

tablename = sys.argv[1]
sem = tablename[-1]

i = 0
dept = ''
for x in sys.argv:
    if i > 1:
        dept += f'{x} '
    i += 1
dept = dept.strip()

c = db.cursor()
c.execute('select firstname, lastname, registration_id from register where sem=%s', (sem,))
result = c.fetchall()

for x in result:
    ls.insert(END, x)

db.close()

b0 = Button(root, text='Update marks', command=update, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
b0.bind("<Enter>", on_enter0)
b0.bind("<Leave>", on_leave0)
b0.pack()
b0.configure(background='#3cb043', font='consolas 17 bold')

root.mainloop()
