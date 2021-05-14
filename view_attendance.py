from tkinter import * 
from PIL import ImageTk,Image  
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
from tkinter import ttk
import tkinter as tk
import os
from tkcalendar import Calendar
from datetime import date




import matplotlib.pyplot as plt
import numpy as np


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="classroom"
)
mycursor=mydb.cursor()


def view_att():
	dat = cal.get_date()

	try:
		sql = ("select * from attendance where dateofattend = \"{}\"" .format(dat))
		#sql = ("select * from register where depart = \"Information Technology\"")
		mycursor.execute(sql)
		res = mycursor.fetchall()
		cnt = 0
		for row in res:
			res = row
			tree.insert("", tk.END, values=row)  
			status = True 
			cnt+=1
		
	except mysql.connector.Error as e:
		print(e)

	if cnt == 0:
		messagebox.showinfo("Message", "Not Available")
	
	

root = Tk()
root.geometry("1000x500")
root.resizable(False,False)
root.title("View Attendance")

Label(root, text = "Select the Date").place(x = 20, y = 30)

cal = Calendar(root, selectmode = 'day')
cal.place(x = 150, y = 30)

Button(root, text = "Show",command = view_att).place(x = 420, y = 30)


tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5","c6","c7","c8"), show='headings',selectmode ='browse')


tree.column("#1", anchor = tk.CENTER, width = 100)
tree.heading("#1", text="Name")

tree.column("#2", anchor=tk.CENTER, width = 100)
tree.heading("#2", text="Register Id")

tree.column("#3", anchor=tk.CENTER, width = 100)
tree.heading("#3", text="Year")

tree.column("#4", anchor=tk.CENTER, width = 100)
tree.heading("#4", text="Department")

tree.column("#5", anchor=tk.CENTER, width = 50)
tree.heading("#5", text="Faculty Id")

tree.column("#6", anchor=tk.CENTER, width = 150)
tree.heading("#6", text="Faculty Name")

tree.column("#7", anchor=tk.CENTER, width = 150)
tree.heading("#7", text="Date of Attendance")

tree.column("#8", anchor=tk.CENTER, width = 150)
tree.heading("#8", text="Subject")
#tree.bind('<ButtonRelease-1>', selectItem)


tree.place(x = 20 , y = 250 )






root.mainloop()