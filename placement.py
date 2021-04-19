from tkinter import * 
from PIL import ImageTk,Image  
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
from tkinter import ttk
import tkinter as tk
import re   
import yagmail
import random 
import string




root = Tk()
root.title("Student  Placement Zone")
root.geometry("700x500")

tabControl = ttk.Notebook(root)

tab1 = Frame(tabControl, height = 450 ,width = 690)
tab2 = Frame(tabControl, height = 450 ,width = 690)
tab3 = Frame(tabControl, height = 450 ,width = 690)
#tab3 = Frame(tabControl,  height = 650 ,width = 1270)

tabControl.add(tab1, text ='Notifications')
tabControl.add(tab2, text ='Placement At a Glance')
tabControl.add(tab3, text ='Recruiters')

tabControl.place(x = 5,y = 10)



#Tab 2



Label(tab2, text = "Placement at a Glance").place(x = 340, y = 20)
tree = ttk.Treeview(tab2, column=("c1", "c2", "c3","c4","c5","c6"), show='headings',selectmode ='browse')


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
#tree.bind('<ButtonRelease-1>', selectItem)
tree.place(x = 40, y = 50)





root.mainloop()