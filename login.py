#import register 
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
import os




root=Tk()
root.title("Login Page")
root.geometry("400x400")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="classroom"
)
mycursor=mydb.cursor()


def login():
	UserName = inpUserName.get()
	PassWord = inpPass.get()

	if len(UserName)==0 and len(PassWord)==0:
		print("Empty")


	try:
		sql = ("select password from login where username = \"{}\" ".format(str(UserName)))
		mycursor.execute(sql)
		res = mycursor.fetchall() 
		for row in res :
			pasd = row[0]

		if pasd == PassWord :
			print("Login Successful")
		else:
			print("Not Successful")

		print("Found")
	except mysql.connector.Error as e:
		print(e)
		print("Not found")

	finally:
		inpUserName.set("")
		inpPass.set("")



def calverify():
	os.system("register.py")




Label(root,text = "Login To Your Account").place(x = 150, y = 30)

inpUserName = StringVar()
userName = Label(root,text = "User Name").place(x = 20, y = 70)
inputusername = Entry(root, width=40, textvariable = inpUserName).place(x = 100, y = 70)

inpPass = StringVar()
passWord = Label(root,text = "Password").place(x = 20, y = 100)
inputpass = Entry(root, width = 40, textvariable = inpPass).place(x = 100, y = 100)

Button(root,text = "Login",command = login).place(x = 150, y = 150)


Label(root,text = "If you Dont have an Account create one.\nTo Register click the below button").place(x = 100, y = 200)
Button(root,text = "Register Now",command = calverify).place(x = 150, y = 250)






root.mainloop()