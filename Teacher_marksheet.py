import tkinter as tk
import MySQLdb
from tkinter import messagebox
master = tk.Tk()

c=MySQLdb.connect('localhost','root','','classroom')
s=c.cursor()

master.title("RESULT")
 
master.geometry("500x350")

master.resizable(False, False)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)
e8 = tk.Entry(master)
 
 

def display():
     
 
    tot=0
    gp=0

    if int(e4.get()) in range(70,81):
         

        tk.Label(master, text ="A").grid(row=5, column=4)
        tot += int(e4.get())
        gp +=10         

    if int(e4.get()) in range(60,70):
        tk.Label(master, text ="B").grid(row=5, column=4)
        tot += int(e4.get())
        gp +=9  

    if int(e4.get()) in range(50,60):
        tk.Label(master, text ="C").grid(row=5, column=4)
        tot += int(e4.get())
        gp +=8 
 
    if int(e4.get()) in range(40,50):
        tk.Label(master, text ="D").grid(row=5, column=4)
        tot += int(e4.get())
        gp +=7


 
    if int(e4.get()) in range(32,40):
        tk.Label(master, text ="E").grid(row=5, column=4)
        tot += int(e4.get())
        gp +=6
         
  
    if int(e4.get()) in range(32):
        tk.Label(master, text ="F").grid(row=5, column=4)
        tot += int(e4.get())
        gp +=0
  
  

    if int(e5.get()) in range(70,81):
        tk.Label(master, text ="A").grid(row=6, column=4)
        tot += int(e5.get())
        gp +=10
    if int(e5.get()) in range(60,70):
        tk.Label(master, text ="B").grid(row=6, column=4)
        tot += int(e5.get())
        gp +=9 
    if int(e5.get()) in range(50,60):
        tk.Label(master, text ="C").grid(row=6, column=4)
        tot += int(e5.get())
        gp +=8
    if int(e5.get()) in range(40,50):
        tk.Label(master, text ="D").grid(row=6, column=4)
        tot += int(e5.get())
        gp +=7
    if int(e5.get()) in range(32,40):
        tk.Label(master, text ="E").grid(row=6, column=4)
        tot += int(e5.get())
        gp +=6
    if int(e5.get()) in range(32):
        tk.Label(master, text ="F").grid(row=6, column=4)
        tot += int(e5.get())
        gp +=0
      



    if int(e6.get()) in range(70,81):
        tk.Label(master, text ="A").grid(row=7, column=4)
        tot += int(e6.get())
        gp +=10  
    if int(e6.get()) in range(60,70):
        tk.Label(master, text ="B").grid(row=7, column=4)
        tot += int(e6.get())
        gp +=9
    if int(e6.get()) in range(50,60):
        tk.Label(master, text ="C").grid(row=7, column=4)
        tot += int(e6.get())
        gp +=8
    if int(e6.get()) in range(40,50):
        tk.Label(master, text ="D").grid(row=7, column=4)
        tot += int(e6.get())
        gp +=7
    if int(e6.get()) in range(32,40):
        tk.Label(master, text ="E").grid(row=7, column=4)
        tot += int(e6.get())
        gp +=6
    if int(e6.get()) in range(32):
        tk.Label(master, text ="F").grid(row=7, column=4)
        tot += int(e6.get())
        gp +=0
  
  
  
  
  
    if int(e7.get()) in range(70,81):
        tk.Label(master, text ="A").grid(row=8, column=4)
        tot += int(e7.get())
        gp +=10  
    if int(e7.get()) in range(60,70):
        tk.Label(master, text ="B").grid(row=8, column=4)
        tot += int(e7.get())
        gp +=9
    if int(e7.get()) in range(50,60):
        tk.Label(master, text ="C").grid(row=8, column=4)
        tot += int(e7.get())
        gp +=8
    if int(e7.get()) in range(40,50):
        tk.Label(master, text ="D").grid(row=8, column=4)
        tot += int(e7.get())
        gp +=7
    if int(e7.get()) in range(32,40):
        tk.Label(master, text ="E").grid(row=8, column=4)
        tot += int(e7.get())
        gp +=6
    if int(e7.get()) in range(32):
        tk.Label(master, text ="F").grid(row=8, column=4)
        tot += int(e7.get())
        gp +=0






    if int(e8.get()) in range(70,81):
        tk.Label(master, text ="A").grid(row=9, column=4)
        tot += int(e8.get())
        gp +=10  
    if int(e8.get()) in range(60,70):
        tk.Label(master, text ="B").grid(row=9, column=4)
        tot += int(e8.get())
        gp +=9
    if int(e8.get()) in range(50,60):
        tk.Label(master, text ="C").grid(row=9, column=4)
        tot += int(e8.get())
        gp +=8
    if int(e8.get()) in range(40,50):
        tk.Label(master, text ="D").grid(row=9, column=4)
        tot += int(e8.get())
        gp +=7
    if int(e8.get()) in range(32,40):
        tk.Label(master, text ="E").grid(row=9, column=4)
        tot += int(e8.get())
        gp +=6
    if int(e8.get()) in range(32):
        tk.Label(master, text ="F").grid(row=9, column=4)
        tot += int(e8.get())
        gp +=0
  
  

    tk.Label(master, text=str(tot)).grid(row=17, column=4)
     

    tk.Label(master, text=str(gp/5)).grid(row=17, column=2)
    name=e1.get()
    reg=e2.get()
    
    m1=e4.get()
    m2=e5.get()
    m3=e6.get()
    m4=e7.get()
    m5=e8.get()
    sg= gp/5
    if sg > 6:
        tk.Label(master, text='Successful', foreground='Green').grid(row=19,column=4)
        m="Successful"
    else:
        tk.Label(master, text='Unsuccessful', foreground='RED').grid(row=19,column=4)
        m="Unsuccessful"

    s.execute("""insert into marks (regno, Name, Maths, OS, AT, COA, CNND, Total, SGPA, Ordinanca) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (reg,name,m1,m2,m3,m4,m5,tot,sg,m))
    c.commit()
    c.close()



 


    



f=('Times',12,'bold')
f1=('Courier',11)

tk.Label(master, text="Name",font=f).grid(row=0, column=1)
 

tk.Label(master, text="Reg.No",font=f).grid(row=1, column=1)
 

tk.Label(master, text="").grid(row=2, column=1)
 

tk.Label(master, text="Srl.No",font=f1).grid(row=4, column=0)
tk.Label(master, text="1").grid(row=5, column=0)
tk.Label(master, text="2").grid(row=6, column=0)
tk.Label(master, text="3").grid(row=7, column=0)
tk.Label(master, text="4").grid(row=8, column=0)
tk.Label(master, text="5").grid(row=9, column=0)
 

tk.Label(master, text="Sub",font=f1).grid(row=4, column=1)
tk.Label(master, text="Maths-4").grid(row=5, column=1)
tk.Label(master, text="OS").grid(row=6, column=1)
tk.Label(master, text="AT").grid(row=7, column=1)
tk.Label(master, text="COA").grid(row=8, column=1)
tk.Label(master, text='CNND').grid(row=9, column=1)
  
     

tk.Label(master, text="Marks",font=f1).grid(row=4, column=2)
e4.grid(row=5, column=2)
e5.grid(row=6, column=2)
e6.grid(row=7, column=2)
e7.grid(row=8, column=2)
e8.grid(row=9, column=2)  
 


  
tk.Label(master, text="Grade",font=f1).grid(row=4, column=4)
  

e1=tk.Entry(master)
e2=tk.Entry(master)
e3=tk.Entry(master)
  

e1.grid(row=0, column=2)
e2.grid(row=1, column=2)

  


button2=tk.Button(master, text='Calculate & Insert the Record', bg='Red',command=display)
button2.grid(row=21, column=2)  
 
tk.Label(master, text="").grid(row=16,column=0)
tk.Label(master, text="").grid(row=18,column=0)
tk.Label(master, text="").grid(row=19,column=0)
tk.Label(master, text="").grid(row=20,column=0) 
tk.Label(master, text="SGPA", font= f).grid(row=17, column=1)
tk.Label(master, text="Total Marks", font=f).grid(row=17, column=3)
tk.Label(master, text="Ordinance", font=f).grid(row=19, column=3)


 

    
master.mainloop()
#Database Table Code
#create table marks(regno int(6),rollno int(6), Name varchar(20),Maths int(4),OS int(4),AT int(4),CNND int(4),COA int(4), CNND int(4), Total int(6), SGPA float(8), Ordinanca varchar(15));

