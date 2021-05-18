import tkinter as tk
import MySQLdb
from tkinter import messagebox, Scrollbar, Text, INSERT

master = tk.Tk()

master.title("Notifications")
 
master.geometry("640x400+50+50")
master.configure(background='#222')
master.resizable(False, False)

def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


import sys
isFaculty = False
for index, arg in enumerate(sys.argv):
    if index > 0:
        isFaculty = True




e1 = tk.Entry(master, font='consolas 14 bold')
e2 = tk.Entry(master,width=20, font='consolas 12 bold')


def inert():
    try:
        s1= e1.get()
        s2= e2.get()
        # c = MySQLdb.connect('localhost', 'root', '', 'python')
        c = MySQLdb.connect('localhost', 'root', '', 'sims')
        s = c.cursor()
        s.execute("""insert into message(msgno, notice) values (%s,%s)""",(s2,s1))
        c.commit()
        c.close()
        messagebox.showinfo('Success', 'Added notification')
    except Exception as e:
        messagebox.showerror('Error', 'Cannot add notification')



e2.place(x=434,y=80)
e1.place(x=100,y=120,width=350,height=100)
tk.Label(master,text = "Notification", font ='Times 30 bold',fg ='red',bg='#222').place(x=200,y=30)
if isFaculty:
    tk.Label(master,text = 'Enter New Notification',font='Times 13 bold',bg='#222',fg='white').place(x=10,y=80)
    tk.Label(master,text = 'Notification number',font='Times 13 bold',bg='#222',fg='white').place(x=260,y=80)
    b = tk.Button(master, text="Add notification", bg='blue', command=inert, font='consolas 14 bold', cursor='hand2', padx=4, pady=4)
    b.bind("<Enter>", on_enter)
    b.bind("<Leave>", on_leave)
    b.configure(background='#0277bd')
    b.place(x=200, y=250)
else:
    # c = MySQLdb.connect('localhost', 'root', '', 'python')
    c = MySQLdb.connect('localhost', 'root', '', 'sims')
    s = c.cursor()
    s.execute("""select * from message order by msgno""")
    result = s.fetchall()

    sb = Scrollbar(master)
    sb.pack(side='right', fill='y')
    t = Text(master, yscrollcommand=sb.set, fg='white', bg='black', font='consolas 15 bold')
    t.pack(fill='both')
    sb.config(command=t.yview)

    for row in result:
        t.insert(INSERT, f"({row[0]}) {row[1]}\n")
        print(row)

    t.configure(state='disabled')
    c.close()
    e1.configure(state='disabled', width=20)
    e2.destroy()

#tk.Button(master,text = "Remove",width=15,height=2,bg='Red').place(x=200,y=320)



master.mainloop()
#Name of database is python
#create table(msgno int(7),notice varchar(2000))
