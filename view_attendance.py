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

def on_enter2(e):
    e.widget['background'] = '#033500'
    e.widget['foreground'] = 'white'


def on_leave2(e):
    e.widget['background'] = '#3cb043'
    e.widget['foreground'] = 'black'


import matplotlib.pyplot as plt
import numpy as np


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="classroom"
# )
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sims"
)
mycursor=mydb.cursor()


font = 'consolas 14 bold'
font2 = 'consolas 12 bold'

def view_att():
	dat = cal.get_date()

	try:
		# sql = ("select * from attendance where dateofattend = \"{}\"" .format(dat))
		#sql = ("select * from register where depart = \"Information Technology\"")
		import sys
		sid = sys.argv[1]
		# sid = 0
		mycursor.execute("select * from attendance where date = %s and registration_id = %s", (dat, sid,  ))
		res = mycursor.fetchall()
		print(res)
		cnt = 0
		for row in res:
			# res = row
			tree.insert("", tk.END, values=row)  
			status = True 
			cnt+=1
		if cnt == 0:
			messagebox.showinfo("Not available", "You do not have any attendance record for this day")
		
	except mysql.connector.Error as e:
		print(e)


	
	

root = Tk()
root.geometry("770x500")
root.resizable(False,False)
root.title("View Attendance")

Label(root, text = "Select the Date", font=font2).place(x = 20, y = 30)

cal = Calendar(root, selectmode = 'day')
cal.place(x = 200, y = 30)

b = Button(root, text = "Show",command = view_att, font=font2)
b.place(x = 500, y = 30)
b.bind("<Enter>", on_enter2)
b.bind("<Leave>", on_leave2)
b.configure(background='#3cb043')


tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', selectmode='browse')
style = ttk.Style()
style.configure("Treeview.Heading", font='consolas 11 bold')

tree.column("#1", anchor=tk.CENTER, width=110)
tree.heading("#1", text="Student ID")

tree.column("#2", anchor=tk.CENTER, width=110)
tree.heading("#2", text="Faculty ID")

tree.column("#3", anchor=tk.CENTER, width=110)
tree.heading("#3", text="Semester")

tree.column("#4", anchor=tk.CENTER, width=110)
tree.heading("#4", text="Department")

tree.column("#5", anchor=tk.CENTER, width=110)
tree.heading("#5", text="Subject")

tree.column("#6", anchor=tk.CENTER, width=110)
tree.heading("#6", text="Date")


# tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5","c6","c7","c8"), show='headings',selectmode ='browse')
#
#
# tree.column("#1", anchor = tk.CENTER, width = 100)
# tree.heading("#1", text="Name")
#
# tree.column("#2", anchor=tk.CENTER, width = 100)
# tree.heading("#2", text="Register Id")
#
# tree.column("#3", anchor=tk.CENTER, width = 100)
# tree.heading("#3", text="Year")
#
# tree.column("#4", anchor=tk.CENTER, width = 100)
# tree.heading("#4", text="Department")
#
# tree.column("#5", anchor=tk.CENTER, width = 50)
# tree.heading("#5", text="Faculty Id")
#
# tree.column("#6", anchor=tk.CENTER, width = 150)
# tree.heading("#6", text="Faculty Name")
#
# tree.column("#7", anchor=tk.CENTER, width = 150)
# tree.heading("#7", text="Date of Attendance")
#
# tree.column("#8", anchor=tk.CENTER, width = 150)
# tree.heading("#8", text="Subject")
#tree.bind('<ButtonRelease-1>', selectItem)


tree.place(x = 20 , y = 250 )






root.mainloop()