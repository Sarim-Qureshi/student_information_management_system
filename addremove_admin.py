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


def addcompany():
	compname = inpCompanyName.get()
	eligmarks = inpEligibleMarks.get()
	seatOffer = inpSeatsOffered.get()
	appliedStud = inpAppliedStud.get()
	if inpCompanyName.get() == "" or inpEligibleMarks.get() == "" or inpSeatsOffered.get() == "" or inpAppliedStud.get() == "":
		messagebox.showerror("Error","Enter the Fields")
	else:
		try:
			sql = "insert into placement values (%s,%s,%s,%s)"
			val = (compname,eligmarks, seatOffer,appliedStud)
			mycursor.execute(sql,val)
			mydb.commit()
			messagebox.showinfo("Successfull","Added company {}".format(compname))
		except mysql.connector.Error as e:
			print(e)
		finally:
			inpCompanyName.set("")
			inpEligibleMarks.set("")
			inpSeatsOffered.set("")
			inpAppliedStud.set("")

def company_details():
	company = clickedCompany1.get()
	bad_chars = [';', ':', '!', "*",")","(","\'",","]
	for i in bad_chars :
		company = company.replace(i, '')
	#print(company)
	try :
		sql = ("select * from placement where company = \"{}\" ".format(company))
		mycursor.execute(sql)
		res = mycursor.fetchall()
		for row in res:
			res = row
			tree.insert("",tk.END,values = row)

	except mysql.connector.Error as e:
		print(e)
	




def company_remove(a):
	curItem = tree.focus()
	removeitem = tree.item(curItem)['values'][0]

	try :
		response=messagebox.askyesno("Message Box","Remove Company {} ?".format(removeitem))
		if response==1:
			
			sql = ("delete from placement where company = \"{}\" ".format(removeitem))
			#val = (removeitem)
			mycursor.execute(sql)
			mydb.commit()
			messagebox.showinfo("Message Box","Company Removed")
	except mysql.connector.Error as e:
		print("not sucess")
		print(e)
	










root = Tk()
root.title("Officer Add and Remove Section")
root.geometry("700x500")

tabControl = ttk.Notebook(root)

tab1 = Frame(tabControl, height = 450 ,width = 690)
tab2 = Frame(tabControl, height = 450 ,width = 690)
#tab3 = Frame(tabControl, height = 450 ,width = 690)
#tab3 = Frame(tabControl,  height = 650 ,width = 1270)

tabControl.add(tab1, text ='Add Company')
#tabControl.add(tab2, text ='Students')
tabControl.add(tab2, text ='Remove Company')

tabControl.place(x = 5,y = 10)


#Tab1---------------------------------------------------------------------------------

Label(tab1, text = "Fill the Following Details to Add the Company").place(x = 250,y= 30)

Label(tab1,text = "Name of Company").place(x = 20 ,y = 80)

inpCompanyName = StringVar()
Entry(tab1, width = 30, textvariable = inpCompanyName).place(x = 150, y = 80)

Label(tab1 ,text = "Eligibility Marks").place(x = 30, y = 120)
inpEligibleMarks = StringVar()
Entry(tab1, width = 30, textvariable = inpEligibleMarks).place(x = 150, y = 120)

Label(tab1, text = "Seats Offered").place(x = 40,y = 150)
inpSeatsOffered = StringVar()
Entry(tab1, width = 30, textvariable = inpSeatsOffered).place(x = 150, y = 150)

Label(tab1, text = "Applied Students").place(x = 50,y = 180)
inpAppliedStud = StringVar()
Entry(tab1, width = 30, textvariable = inpAppliedStud).place(x = 150, y = 180)

Button(tab1, text = "Add",width = 30, command = addcompany).place(x = 210, y = 200)




#Tab2----------------------------------------------------------------------
Label(tab2, text = "Remove Company").place(x = 250,y= 30)

try:
	sql = "(select distinct(company) from applied)"
	mycursor.execute(sql)
	res = mycursor.fetchall()
	optionCompany1 = []
	for row in res:
		optionCompany1 = res
		
except mysql.connector.Error as e:
	print(e)

Label(tab2, text = "Select Company Name").place(x = 30, y = 50)
clickedCompany1 = StringVar()
inputCompany = OptionMenu(tab2, clickedCompany1, *optionCompany1,).place(x = 150, y = 30)


Button(tab2, text = "Show",command = company_details).place(x = 350 , y = 50)

tree = ttk.Treeview(tab2, column=("c1", "c2", "c3","c4"), show='headings')

tree.column("#1", anchor = tk.CENTER, width = 100)
tree.heading("#1", text="Company Name")

tree.column("#2", anchor=tk.CENTER, width = 100)
tree.heading("#2", text="Eligibile Marks")

tree.column("#3", anchor=tk.CENTER, width = 100)
tree.heading("#3", text="Seats Offered")

tree.column("#4", anchor=tk.CENTER, width = 100)
tree.heading("#4", text="Applied Students")

tree.bind('<ButtonRelease-1>', company_remove)

tree.place(x = 40, y = 100)




root.mainloop()