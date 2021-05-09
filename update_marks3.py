from tkinter import *
import sys
from tkinter import messagebox
import mysql.connector


def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


def update():
    try:
        db = mysql.connector.connect(host='localhost', user='root', password='', database='sims')
        c = db.cursor()
        c.execute(
            f'update {tablename} set subject1marks=%s, subject2marks=%s, subject3marks=%s, subject4marks=%s, subject5marks=%s where registration_id=%s',
            (str(s1.get()), str(s2.get()), str(s3.get()), str(s4.get()), str(s5.get()), rid,))
        db.commit()
        db.close()
        messagebox.showinfo('Marks Updated', f'Successfully updated marks for {sys.argv[3]} {sys.argv[4]}')

    except Exception as e:
        messagebox.showerror("Error", 'Cannot update marks')


root = Tk()
root.geometry("1000x670+0+0")
root.resizable(False, False)
root.title('Student Information Management System')
root.configure(background='#222')
if sys.argv[-1] != '0':
    head = Label(root, text=f'Update marks for {sys.argv[3]} {sys.argv[4]}', font='consolas 30 bold')
else:
    head = Label(root, text=f'{sys.argv[3]} {sys.argv[4]}, your marks are', font='consolas 30 bold')
head.pack(pady=(35, 0))
head.configure(background='#222', foreground='white')

f1 = Frame(root, width=600, height=300, borderwidth=10, relief='groove')
f1.configure(background='#999')
f1.pack(pady=(30, 20), padx=(60, 5), anchor='c')

tablename = sys.argv[1].strip()
rid = sys.argv[2].strip()
sem = tablename[-1]

try:
    i = 0
    dept = ''
    for x in sys.argv[:-1]:
        if i > 4:
            dept += f'{x} '
        i += 1
    dept=dept.strip()
    db = mysql.connector.connect(host='localhost', user='root', password='', database='sims')
    c = db.cursor()
    if sem == '1' or sem == '2':
        c.execute(f'select * from sem{sem}_subjects')
        o = 0
    else:
        c.execute(f'select * from subjects where department=%s and sem=%s', (dept, sem,))
        o = 2

    result = c.fetchall()
    result = result[0]
    if sem == '1' or sem == '2':
        c.execute(f'select * from {tablename} where registration_id={rid}')
        o2 = 0
    else:
        c.execute(f'select * from {tablename} where registration_id={rid} and department=\'{dept}\'')
        o2 = 1

    r2 = c.fetchall()
    r2=r2[0]

    db.close()

except Exception as e:
    if sys.argv[-1]!='0':
        messagebox.showerror('Error occurred', 'Cannot update marks')
    else:
        messagebox.showerror('Invalid credentials', 'Enter valid credentials')


l1 = Label(f1, text=result[0+o], font='consolas 18 bold')
l1.grid(row=0, column=0, pady=(20, 10), padx=(70, 20))
l1.configure(background='#999')
s1 = Scale(f1, from_=0, to=20, orient='horizontal', tickinterval=20)
s1.set(r2[1+o2])
s1.grid(row=0, column=1, pady=(10, 10), padx=(70, 20))
if sys.argv[-1] == '0':
    s1.configure(state='disabled')

l2 = Label(f1, text=result[1+o], font='consolas 18 bold')
l2.grid(row=1, column=0, pady=(10, 10), padx=(70, 20))
l2.configure(background='#999')
s2 = Scale(f1, from_=0, to=20, orient='horizontal', tickinterval=20)
s2.set(r2[2+o2])
s2.grid(row=1, column=1, pady=(10, 10), padx=(70, 20))
if sys.argv[-1] == '0':
    s2.configure(state='disabled')


l3 = Label(f1, text=result[2+o], font='consolas 18 bold')
l3.grid(row=2, column=0, pady=(10, 10), padx=(70, 20))
l3.configure(background='#999')
s3 = Scale(f1, from_=0, to=20, orient='horizontal', tickinterval=20)
s3.set(r2[3+o2])
s3.grid(row=2, column=1, pady=(10, 10), padx=(70, 20))
if sys.argv[-1] == '0':
    s3.configure(state='disabled')


l4 = Label(f1, text=result[3+o], font='consolas 18 bold')
l4.grid(row=3, column=0, pady=(10, 10), padx=(70, 20))
l4.configure(background='#999')
s4 = Scale(f1, from_=0, to=20, orient='horizontal', tickinterval=20)
s4.set(r2[4+o2])
s4.grid(row=3, column=1, pady=(10, 10), padx=(70, 20))
if sys.argv[-1] == '0':
    s4.configure(state='disabled')


l5 = Label(f1, text=result[4+o], font='consolas 18 bold')
l5.grid(row=4, column=0, pady=(10, 10), padx=(70, 20))
l5.configure(background='#999')
s5 = Scale(f1, from_=0, to=20, orient='horizontal', tickinterval=20)
s5.set(r2[5+o2])
s5.grid(row=4, column=1, pady=(10, 20), padx=(70, 20))
if sys.argv[-1] == '0':
    s5.configure(state='disabled')


b1 = Button(root, text='Update marks', command=update, cursor='hand2', font='consolas 17 bold', pady=1, padx=10)
b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)
if sys.argv[-1] != '0':
    b1.pack()
b1.configure(background='#0277bd')

db.close()
root.mainloop()
