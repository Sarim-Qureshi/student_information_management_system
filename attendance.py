from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
import re   
import yagmail
from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar
from datetime import date
today = date.today()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="classroom"
)
mycursor=mydb.cursor()



root = Tk()
root.geometry("700x600")
root.title("Attendance")


status = False

def addrecord():
	additem = inpRegisterID.get()

	
	try :
		sql = ("select * from register where registerId = {} ".format(additem))
		#sql = ("select * from register where depart = \"Information Technology\"")
		mycursor.execute(sql)
		res = mycursor.fetchall()
		for row in res:
			res = row
			tree.insert("", tk.END, values=row)  
			status = True 
		
	except mysql.connector.Error as e:
		print(e)
	finally :
		inpRegisterID.set(" ")

def markAttendance():
	takeAttend = inpRegisterID.get()
	dat = cal.get_date()
	print(dat)

	try :
		sql = "insert into attendance values (%s, %s, %s)"
		val = (takeAttend, 78965, dat)
		mycursor.execute(sql,val)
		mydb.commit()
		print("sucess")

	except mysql.connector.Error as e:
		print("not sucess")
		print(e)

def selectItem(a):
  
    curItem = tree.focus()
    additem = tree.item(curItem)['values'][2]
    subj = clickedSubj.get()


    dat = cal.get_date()
    
    if clickedSubj.get() == "":
    	messagebox.showinfo("messagebox", "Enter Subject")
    elif inpRegisterID.get() == "":
    	messagebox.showinfo("messagebox", "Enter Register ID")
    elif cal.get_date() == "":
    	messagebox.showinfo("messagebox", "Select Date")
    else :
    	try :
    		response=messagebox.askyesno("Message Box","Mark Attendance for {}".format(additem))
    		if response==1:
    			sql = "insert into attendance values (%s, %s, %s)"
    			val = (additem, 78965, subj)
    			mycursor.execute(sql,val)
    			mydb.commit()
    			messagebox.showinfo("Message Box","Attendance Marked")
    	
    	except mysql.connector.Error as e:
    		print("not sucess")
    		print(e)
    



Label(root, text = "Add Attendance").place(x = 300, y = 10)

Label(root, text = "Enter Register Id").place(x = 30, y= 50)

inpRegisterID = StringVar()
registerId = Entry(root, width = 30, textvariable = inpRegisterID).place(x = 150, y = 50)
Button(root, text = "Show",command = addrecord).place(x = 350 , y = 50)




optionSubj = ["EM-4",
				"OS",
				"COA",
				"CNND",
				"AT"]
stdSubj = Label(root, text = " Select Subject").place(x = 420, y = 50)
clickedSubj = StringVar()
inputSubj = OptionMenu(root, clickedSubj, *optionSubj).place(x = 550, y = 50)











cal = Calendar(root, selectmode = 'day')
  
cal.place(x = 80, y = 80)



tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5","c6"), show='headings',selectmode ='browse')


tree.column("#1", anchor = tk.CENTER, width = 100)
tree.heading("#1", text="First Name")

tree.column("#2", anchor=tk.CENTER, width = 100)
tree.heading("#2", text="Last Name")

tree.column("#3", anchor=tk.CENTER, width = 100)
tree.heading("#3", text="Register Id")

tree.column("#4", anchor=tk.CENTER, width = 100)
tree.heading("#4", text="Phone Number")

tree.column("#5", anchor=tk.CENTER, width = 50)
tree.heading("#5", text="Year")

tree.column("#6", anchor=tk.CENTER, width = 150)
tree.heading("#6", text="Department")
tree.bind('<ButtonRelease-1>', selectItem)


tree.place(x = 40, y = 280)

#Button(root, text = "Mark Attendance", command = markAttendance).place(x = 300 , y = 530)

root.mainloop()
