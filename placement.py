from tkinter import * 
from PIL import ImageTk,Image  
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
from tkinter import ttk
import tkinter as tk
import os


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="classroom"
)
mycursor=mydb.cursor()




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
tabControl.add(tab3, text ='Statics')

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

	Label(tab2, text = company).place(x = 150,y = 80)
	
	try :
		sql = ("select eligibity,seats,applied from placement where company = \"{}\" ".format(company))
		mycursor.execute(sql)
		res = mycursor.fetchall()
		eligible = []
		for row in res:
			eligible = res
			Label(tab2, text = eligible[0][0]).place(x = 150,y = 120)
			Label(tab2, text = eligible[0][1]).place(x = 150, y = 150)
			Label(tab2, text = eligible[0][2]).place(x = 150, y = 180)
		#print(eligible)
	except mysql.connector.Error as e:
		print(e)

	


	if eligible[0][1] <= eligible[0][2]:
		Label(tab2, text = "Seats Not Available \n Try next Time!!").place(x = 250, y = 200)
		#print("Seats Not Available")
	else:
		Label(tab2 , text = " ").place(x = 250, y = 200)
		Button(tab2, text = "Apply Now",command = applyNow).place(x = 250, y = 200)
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



stdCompany = Label(tab2, text = " Select Company Name").place(x = 20, y = 30)

clickedCompany = StringVar()
inputCompany = OptionMenu(tab2, clickedCompany, *optionCompany).place(x = 150, y = 30)
Button(tab2, text = "Get Details",width = 30,command = display).place(x = 250,y= 30)


Label(tab2,text = "Name of Company").place(x = 20 ,y = 80)
Label(tab2 ,text = "Eligibility Marks").place(x = 30, y = 120)
Label(tab2, text = "Seats Offered").place(x = 40,y = 150)
Label(tab2, text = "Students Applied").place (x = 40, y = 180)




#Tab 3
root.mainloop()