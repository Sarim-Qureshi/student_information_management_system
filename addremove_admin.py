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
font2 = 'consolas 13 bold'


def on_enterv(e):
    e.widget['background'] = '#fda507'
    e.widget['foreground'] = 'white'


def on_leavev(e):
    e.widget['background'] = '#fee227'
    e.widget['foreground'] = 'black'


def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'

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
root.geometry("700x500+20+20")

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

# Label(tab1, text = "Fill the Following Details to Add the Company").place(x = 250,y= 30)
Label(tab1, text = "Fill the Following Details to Add the Company", font=font2).grid(row=0, column=0, columnspan=2, pady=10, padx=10)


# Label(tab1,text = "Name of Company").place(x = 20 ,y = 80)
Label(tab1,text = "Name of Company", font=font).grid(row=1, column=0, pady=10, padx=10)

inpCompanyName = StringVar()
# Entry(tab1, width = 30, textvariable = inpCompanyName).place(x = 150, y = 80)
Entry(tab1, width = 30, textvariable = inpCompanyName, font=font).grid(row=1, column=1, pady=10, padx=10)


# Label(tab1 ,text = "Eligibility Marks").place(x = 30, y = 120)
Label(tab1 ,text = "Eligibility Marks", font=font).grid(row=2, column=0, pady=10, padx=10)

inpEligibleMarks = StringVar()
# Entry(tab1, width = 30, textvariable = inpEligibleMarks).place(x = 150, y = 120)
Entry(tab1, width = 30, textvariable = inpEligibleMarks, font=font).grid(row=2, column=1, pady=10, padx=10)


# Label(tab1, text = "Seats Offered").place(x = 40,y = 150)
Label(tab1, text = "Seats Offered", font=font).grid(row=3, column=0, pady=10, padx=10)

inpSeatsOffered = StringVar()
# Entry(tab1, width = 30, textvariable = inpSeatsOffered).place(x = 150, y = 150)
Entry(tab1, width = 30, textvariable = inpSeatsOffered, font=font).grid(row=3, column=1, pady=10, padx=10)


# Label(tab1, text = "Applied Students").place(x = 50,y = 180)
Label(tab1, text = "Applied Students", font=font).grid(row=4, column=0, pady=10, padx=10)

inpAppliedStud = StringVar()
# Entry(tab1, width = 30, textvariable = inpAppliedStud).place(x = 150, y = 180)
Entry(tab1, width = 30, textvariable = inpAppliedStud, font=font).grid(row=4, column=1, pady=10, padx=10)


# Button(tab1, text = "Add",width = 30, command = addcompany).place(x = 210, y = 200)
b1 = Button(tab1, text = "Add",width = 30, command = addcompany, font=font)
b1.grid(row=5, column=1, pady=10, padx=10)
b1.configure(background='#0277bd', font=font)
b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)



#Tab2----------------------------------------------------------------------
# Label(tab2, text = "Remove Company").place(x = 250,y= 30)
Label(tab2, text = "Remove Company", font=font2).grid(row=0, column=2, pady=10, padx=10)

try:
	sql = "(select company from applied)"
	mycursor.execute(sql)
	res = mycursor.fetchall()
	optionCompany1 = []
	for row in res:
	    optionCompany1 = res
		
except mysql.connector.Error as e:
	print(e)

# Label(tab2, text = "Select Company Name").place(x = 30, y = 50)
Label(tab2, text = "Select Company Name", font=font2).grid(row=0, column=0, pady=10, padx=10)


clickedCompany1 = StringVar()
# inputCompany = OptionMenu(tab2, clickedCompany1, *optionCompany1,).place(x = 150, y = 30)
inputCompany = OptionMenu(tab2, clickedCompany1, *optionCompany1,)
inputCompany.grid(row=0, column=1, pady=10, padx=10)
inputCompany.configure(font=font)



# Button(tab2, text = "Show",command = company_details).place(x = 350 , y = 50)
bv = Button(tab2, text = "Show",command = company_details, font=font)
bv.grid(row=1, column=1, pady=10, padx=10)
bv.bind("<Enter>", on_enterv)
bv.bind("<Leave>", on_leavev)



tree = ttk.Treeview(tab2, column=("c1", "c2", "c3","c4"), show='headings')

tree.column("#1", anchor = tk.CENTER, width = 130)
tree.heading("#1", text="Company Name")

tree.column("#2", anchor=tk.CENTER, width = 130)
tree.heading("#2", text="Eligibile Marks")

tree.column("#3", anchor=tk.CENTER, width = 130)
tree.heading("#3", text="Seats Offered")

tree.column("#4", anchor=tk.CENTER, width = 130)
tree.heading("#4", text="Applied Students")

tree.bind('<ButtonRelease-1>', company_remove)

# tree.place(x = 40, y = 100)
tree.grid(row=2, column=0, columnspan=4, pady=10, padx=10)




root.mainloop()