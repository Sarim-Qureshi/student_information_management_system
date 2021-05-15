from tkinter import Tk, Label, Button, Frame, Scrollbar, Listbox, END, ACTIVE, filedialog, simpledialog, messagebox
import mysql.connector
import sys


def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


def on_enter_del(e):
    e.widget['background'] = '#900d09'
    e.widget['foreground'] = 'white'


def on_leave_del(e):
    e.widget['background'] = '#ea3c53'
    e.widget['foreground'] = 'black'


def on_enterv(e):
    e.widget['background'] = '#fda507'
    e.widget['foreground'] = 'white'


def on_leavev(e):
    e.widget['background'] = '#fee227'
    e.widget['foreground'] = 'black'


def on_enter0(e):
    e.widget['background'] = '#033500'
    e.widget['foreground'] = 'white'


def on_leave0(e):
    e.widget['background'] = '#3cb043'
    e.widget['foreground'] = 'black'


def delete_timetable():
    try:
        name = str(ls.get(ls.curselection()))
    except:
        return
    answer = messagebox.askyesno('Delete the timetable!', f'Are you sure you want to delete the timetable {name}?')
    if answer:
        db = mysql.connector.connect(host='localhost', user='root', password='', database='sims')
        c = db.cursor()
        try:
            c.execute('delete from timetable where name=%s', (name, ))
            messagebox.showinfo('Success', 'Timetable was deleted successfully')
            import os
            os.system('update_timetable2.py')
            root.destroy()
        except:
            messagebox.showerror('Error', 'Could not delete the timetable')


def view_timetable():
    try:
        name = str(ls.get(ls.curselection()))
    except:
        return
    import os
    os.system(f'view_timetable.py {name}')


def edit_timetable():
    try:
        name = str(ls.get(ls.curselection())[0])
    except:
        return
    import os
    os.system(f'edit_timetable.py {name}')
    root.destroy()


def add_timetable():
    root.destroy()


root = Tk()
root.geometry("1000x670+0+0")
root.resizable(False, False)
root.title('Student Information Management System')
root.configure(background='#222')
if sys.argv[1] != 'student':
    head = Label(root, text='Update timetables', font='consolas 30 bold')
else:
    head = Label(root, text='View timetables', font='consolas 30 bold')
head.pack(pady=(35, 0))
head.configure(background='#222', foreground='white')


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
c = db.cursor()
if sys.argv[1] != 'student':
    c.execute('select name from timetable')
else:
    c.execute('select name from timetable where student_visibility=1')
result=c.fetchall()
for x in result:
    ls.insert(END, x[0])

db.commit()
db.close()

# ls.bind('<<ListboxSelect>>', selected_timetable)

f2 = Frame(root, width=600, height=300, borderwidth=10, relief='groove')
f2.configure(background='#999')
f2.pack(pady=(50, 20), padx=(60, 5), anchor='c')

if sys.argv[1] != 'student':
    b0 = Button(f2, text='Add timetable', command=add_timetable, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
    b0.bind("<Enter>", on_enter0)
    b0.bind("<Leave>", on_leave0)
    b0.grid(row=0, column=0)
    b0.configure(background='#3cb043')

if sys.argv[1] != 'student':
    b1 = Button(f2, text='Edit timetable', command=edit_timetable, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
    b1.bind("<Enter>", on_enter)
    b1.bind("<Leave>", on_leave)
    b1.grid(row=0, column=1)
    b1.configure(background='#0277bd')

bv = Button(f2, text='View timetable', command=view_timetable, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
bv.bind("<Enter>", on_enterv)
bv.bind("<Leave>", on_leavev)
bv.grid(row=0, column=2)
bv.configure(background='#fee227')

if sys.argv[1] != 'student':
    bdel = Button(f2, text='Delete timetable', command=delete_timetable, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
    bdel.bind("<Enter>", on_enter_del)
    bdel.bind("<Leave>", on_leave_del)
    bdel.grid(row=0, column=3)
    bdel.configure(background='#ea3c53')




root.mainloop()