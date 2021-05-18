import os
from tkinter import *
import sys
from tkinter import messagebox, filedialog

# from PIL import pdf, pdfTk
from mysql.connector import MySQLConnection
import mysql.connector
import sys
tname = ''
for i, x in enumerate(sys.argv):
    if i>0:
        tname += x+" "

tname = tname.strip()
print(tname)

def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


def on_enter2(e):
    e.widget['background'] = '#fda507'
    e.widget['foreground'] = 'white'


def on_leave2(e):
    e.widget['background'] = '#fee227'
    e.widget['foreground'] = 'black'


def edit_timetable():
    import re
    result = re.search(r'\w+', pdf_name.get())
    if result is None:
        messagebox.showinfo('Enter the timetable name', 'Make sure to enter a sensible timetable name to proceed')
    else:
        filename = filedialog.askopenfilename(defaultextension='.pdf',
                                              filetypes=[('pdf file', '*.pdf'), ('All files', '*.*')])

        # print(os.path.splitext(os.path.basename(filename))[0])
        file = open('code.txt', 'wb')
        with open(filename, 'rb') as f:
            for line in f.readlines():
                file.write(line)
        file.close()
        with open('code.txt', 'rb') as f:
            data = f.read()
        db = mysql.connector.connect(host='localhost', user='root', password='', database='sims')
        c = db.cursor()
        c.execute('select * from timetable where name=%s', (pdf_name.get(), ))
        c.fetchall()
        if c.rowcount >= 1 and tname != pdf_name.get():
            messagebox.showerror('Error!', 'Timetable with same name  already exists. Enter a different name')
            return
        else:
            timetable_name = pdf_name.get()
            try:
                c.execute('update timetable set name=%s, pdf=%s, student_visibility=%s where name=%s', (timetable_name, data, cb.get(), tname))
                db.commit()
                messagebox.showinfo('Success', 'Your timetable was edited successfully')
            except:
                db.rollback()
                messagebox.showerror('Error!', 'Timetable was not updated.')
        db.close()
        if os.path.exists("code.txt"):
            os.remove("code.txt")


def edit_timetable_simple():
    import re
    result = re.search(r'\w+', pdf_name.get())
    if result is None:
        messagebox.showinfo('Enter the timetable name', 'Make sure to enter a sensible timetable name to proceed')
    else:
        db = mysql.connector.connect(host='localhost', user='root', password='', database='sims')
        c = db.cursor()
        c.execute('select * from timetable where name=%s', (pdf_name.get(), ))
        c.fetchall()
        print(c.rowcount)
        if c.rowcount >= 1 and tname != pdf_name.get():
            messagebox.showerror('Error!', 'Timetable with same name  already exists. Enter a different name')
            return
        else:
            timetable_name = pdf_name.get()
            try:
                c.execute('update timetable set name=%s, student_visibility=%s where name=%s', (timetable_name, cb.get(), tname))
                db.commit()
                messagebox.showinfo('Success', 'Your timetable was edited successfully')
            except:
                db.rollback()
                messagebox.showerror('Error!', 'Timetable was not updated.')
        db.close()


root = Tk()
root.geometry("1000x670+0+0")
root.resizable(False, False)
root.configure(background='#222')
root.title('Student Information Management System')
head = Label(root, text='Update timetable', font='consolas 30 bold')
head.pack(pady=(35, 0))
head.configure(background='#222', foreground='white')

f1 = Frame(root, width=800, height=500, borderwidth=10, relief='groove')
f1.configure(background='#999')
f1.pack(pady=(50, 20), padx=(60, 5), anchor='c')

name = Label(f1, text='Edit timetable name:', font='consolas 18 bold')
name.grid(row=0, column=0, pady=(45, 40), padx=(70, 20))
name.configure(background='#999')

pdf_name = StringVar()
pdf_name.set(tname)
pdf_entry = Entry(f1, textvariable=pdf_name, font='consolas 17 bold')
pdf_entry.grid(row=0, column=1, pady=(45, 40), padx=(20, 70))

db = mysql.connector.connect(host='localhost', user='root', password='', database='sims')
c = db.cursor()
c.execute('select student_visibility from timetable where name=%s', (tname, ))
result=c.fetchall()
for x in result:
    flag = x
flag = int(flag[0])

cb = IntVar()
visible_to_student = Checkbutton(f1, text='Visible to students?', font='consolas 14 bold', variable=cb)
visible_to_student.grid(row=2, column=0, columnspan=2, pady=(7, 15), padx=(70, 70))
visible_to_student.configure(background='#999')
if flag == 1:
    visible_to_student.select()

b2 = Button(f1, text='Click here to change only name and visibility', command=edit_timetable_simple, cursor='hand2', font='consolas 18 bold', pady=1, padx=10)
b2.bind("<Enter>", on_enter2)
b2.bind("<Leave>", on_leave2)
b2.grid(row=3, column=0, columnspan=2, pady=(20, 45), padx=(70, 70))
b2.configure(background='#fee227')

b2 = Button(f1, text='Click here to Change pdf file', command=edit_timetable, cursor='hand2', font='consolas 18 bold', pady=1, padx=10)
b2.bind("<Enter>", on_enter)
b2.bind("<Leave>", on_leave)
b2.grid(row=4, column=0, columnspan=2, pady=(20, 45), padx=(70, 70))
b2.configure(background='#0277bd')


root.mainloop()