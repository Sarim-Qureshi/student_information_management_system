import tkinter as tk
import MySQLdb
from tkinter import messagebox
master = tk.Tk()

c=MySQLdb.connect('localhost','root','','python')
s=c.cursor()

master.title("RESULT")
 
master.geometry("600x400")
master.configure(background='#222')
master.resizable(False, False)

e1 = tk.Entry(master)
e2 = tk.Entry(master,width=20)




def inert():
    
    s1= e1.get()
    s2= e2.get()
    s.execute("""insert into message(msgno, notice) values (%s,%s)""",(s2,s1))
    c.commit()
    c.close()



e2.place(x=400,y=80)
e1.place(x=100,y=120,width=350,height=100)
tk.Label(master,text = "Notification", font ='Times 25 bold',fg ='red',bg='#222').place(x=200,y=30)
tk.Label(master,text = 'Enter New Notification',font='Times 12 bold',bg='#222',fg='white').place(x=10,y=80)
tk.Label(master,text = 'Notification number',font='Times 12 bold',bg='#222',fg='white').place(x=240,y=80)
#tk.Button(master,text = "Remove",width=15,height=2,bg='Red').place(x=200,y=320)
tk.Button(master,text = "Add",width=15,height=2,bg='blue',command=inert).place(x=200,y=250)


master.mainloop()
#Name of database is python
#create table(msgno int(7),notice varchar(2000))
