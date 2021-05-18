from tkinter import *
import mysql.connector
import sys


def on_enterv(e):
    e.widget['background'] = '#fda507'
    e.widget['foreground'] = 'white'


def on_leavev(e):
    e.widget['background'] = '#fee227'
    e.widget['foreground'] = 'black'


def view_subjects():
    pass


st = ''
i = 0
for x in sys.argv:
    if i > 0:
        st += (x + " ")
    i += 1

root = Tk()
root.geometry("1000x600+0+0")
root.wm_iconbitmap('zicon.ico')
root.resizable(False, False)
root.configure(background='#222')
root.title('Student Information Management System')
head = Label(root, text=f'Subjects of {st}', font='consolas 25 bold')
head.pack(pady=(35, 0))
head.configure(background='#222', foreground='white')

f1 = Frame(root, width=300, height=70, borderwidth=10, relief='groove')
f1.configure(background='#999')
f1.pack(pady=(50, 20), anchor='c')

sb = Scrollbar(f1)
sb.pack(side='right', fill='y')
ls = Listbox(f1, yscrollcommand=sb.set, width=40, height=10)
ls.config(font='comicsanms 18 bold')
ls.pack()
sb.config(command=ls.yview)
db = mysql.connector.connect(host='localhost', user='root', password='', database='sims')
c = db.cursor()

if sys.argv[2] == '1' or sys.argv[2] == '2':
    if sys.argv[2] == '1':
        c.execute('select * from sem1_subjects')
        result = c.fetchall()
        print(result)
        for x in result[0]:
            ls.insert(END, x)
    if sys.argv[2] == '2':
        c.execute('select * from sem2_subjects')
        result = c.fetchall()
        print(result)
        for x in result[0]:
            ls.insert(END, x)
else:
    st = ""
    i = 0
    for x in sys.argv:
        if i > 2:
            st += (x + ' ')
        i += 1
    st = st.strip()
    c.execute('select * from subjects where sem=%s and department=%s', (sys.argv[2], st))
    result = c.fetchall()
    c = 0
    for x in result[0]:
        if c > 1:
            ls.insert(END, x)
        c += 1


root.mainloop()
