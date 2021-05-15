from tkinter import * 
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
from tkinter import ttk
import tkinter as tk
import os

font = 'consolas 11'
font2 = 'consolas 12 bold'


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="classroom"
)
mycursor=mydb.cursor()

def on_enter0(e):
    e.widget['background'] = '#033500'
    e.widget['foreground'] = 'white'


def on_leave0(e):
    e.widget['background'] = '#3cb043'
    e.widget['foreground'] = 'black'

def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


root = Tk()
root.title("Student  Placement Zone")
root.geometry("700x500")

tabControl = ttk.Notebook(root)

tab1 = Frame(tabControl, height = 450 ,width = 690)
tab2 = Frame(tabControl, height = 450 ,width = 690)
tab3 = Frame(tabControl, height = 450 ,width = 690)
#tab3 = Frame(tabControl,  height = 650 ,width = 1270)

#tabControl.add(tab1, text ='Notifications')
tabControl.add(tab2, text ='Placement At a Glance')
#tabControl.add(tab3, text ='Statics')

tabControl.place(x = 5,y = 10)

def applyNow():

	company = clickedCompany.get()
	bad_chars = [';', ':', '!', "*",")","(","\'",","]
	for i in bad_chars :
		company = company.replace(i, '')
	
	#print(company)

	os.system(f'applyNow.py {company}')
	

def display():
	company = clickedCompany.get()


	#name = clickedCompany.get()
	bad_chars = [';', ':', '!', "*",")","(","\'",","]
	for i in bad_chars :
		company = company.replace(i, '')

	# Label(tab2, text = company).place(x = 150,y = 80)
	Label(tab2, text = company, font=font).grid(row=1, column=1, pady=10, padx=10)

	try :
		sql = ("select eligibity,seats,applied from placement where company = \"{}\" ".format(company))
		mycursor.execute(sql)
		res = mycursor.fetchall()
		eligible = []
		print(res)
		# for row in res:
		eligible = res
		Label(tab2, text=eligible[0][0], font=font).grid(row=2, column=1, pady=10, padx=10)
		Label(tab2, text=eligible[0][1], font=font).grid(row=3, column=1, pady=10, padx=10)
		Label(tab2, text=eligible[0][2], font=font).grid(row=4, column=1, pady=10, padx=10)
		# Label(tab2, text = eligible[0][0]).place(x = 150,y = 120)
		# Label(tab2, text = eligible[0][1]).place(x = 150, y = 150)
		# Label(tab2, text = eligible[0][2]).place(x = 150, y = 180)

		#print(eligible)
	except mysql.connector.Error as e:
		print(e)


	if eligible[0][1] <= eligible[0][2]:
		# Label(tab2, text = "Seats Not Available \n Try next Time!!").place(x = 250, y = 200)
		Label(tab2, text = "Seats Not Available \n Try next Time!!", font=font).grid(row=5, column=2, pady=10, padx=10)

		#print("Seats Not Available")
	else:
		# Label(tab2 , text = " ").place(x = 250, y = 200)
		# Button(tab2, text = "Apply Now",command = applyNow).place(x = 250, y = 200)
		Label(tab2, text=" ").grid(row=5, column=1, pady=10, padx=10)
		b0 = Button(tab2, text="Apply Now", command=applyNow)
		b0.grid(row=5, column=1, pady=10, padx=10)
		b0.configure(background='#3cb043', font=font)
		b0.bind("<Enter>", on_enter0)
		b0.bind("<Leave>", on_leave0)


#print("Seats Available")

	



try:
	sql = "(select company from placement)"
	mycursor.execute(sql)
	res = mycursor.fetchall()
	optionCompany = []
	for row in res:
		optionCompany = res
		
except mysql.connector.Error as e:
	print(e)



# stdCompany = Label(tab2, text = " Select Company Name").place(x = 20, y = 30)
stdCompany = Label(tab2, text = " Select Company Name", font=font2).grid(row=0, column=0, pady=10, padx=10)

clickedCompany = StringVar()
# inputCompany = OptionMenu(tab2, clickedCompany, *optionCompany).place(x = 150, y = 30)
# Button(tab2, text = "Get Details",width = 30,command = display).place(x = 300,y= 30)
inputCompany = OptionMenu(tab2, clickedCompany, *optionCompany)
inputCompany.grid(row=0, column=1, pady=10, padx=10)
inputCompany.configure(font=font2)
b1 = Button(tab2, text = "Get Details",width = 30,command = display)
b1.grid(row=0, column=2, pady=10, padx=10)
b1.configure(background='#0277bd', font=font)
b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)


# Label(tab2,text = "Name of Company").place(x = 20 ,y = 80)
# Label(tab2 ,text = "Eligibility Marks").place(x = 30, y = 120)
# Label(tab2, text = "Seats Offered").place(x = 40,y = 150)
# Label(tab2, text = "Students Applied").place (x = 40, y = 180)

Label(tab2,text = "Name of Company", font=font).grid(row=1, column=0, pady=10, padx=10)
Label(tab2 ,text = "Eligibility Marks", font=font).grid(row=2, column=0, pady=10, padx=10)
Label(tab2, text = "Seats Offered", font=font).grid(row=3, column=0, pady=10, padx=10)
Label(tab2, text = "Students Applied", font=font).grid(row=4, column=0, pady=10, padx=10)




#Tab 3
root.mainloop()