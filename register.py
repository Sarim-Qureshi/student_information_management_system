from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import mysql.connector
import re   
import yagmail
import random 
import string


root=Tk()
root.title("Registration Page")
root.geometry("500x500")


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="classroom"

)

mycursor=mydb.cursor()

emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  



def verify():
	firstName = inpFirstName.get()

	lastName = inpLastName.get()

	RegisterId = inpRegisterId.get()

	PhoneNumber = inpPhoneNumber.get()


	SelYear = clickedYear.get()

	SelDepart = clickedDepart.get()

	EmailId = inpEmailid.get()

	# if inpFirstName.get() == "":
	# 	msgbox = messagebox.showwarning("Enter the First Name","Warning")
	# elif inpLastName.get() == "":
	# 	msgbox = messagebox.showwarning("Enter the Last Name","Warning")
	# elif inpRegisterId.get() == "":
	# 	msgbox = messagebox.showwarning("Enter the Registration ID","Warning")
	# elif inpPhoneNumber.get() == "":
	# 	msgbox = messagebox.showwarning("Enter the Phone Number","Warning")
	# elif clickedYear.get() == "":
	# 	msgbox = messagebox.showwarning("Choose Your Year","Warning")
	# elif clickedDepart.get() == "":
	# 	msgbox = messagebox.showwarning("Enter the Department","Warning")
	# elif inpEmailid.get() == "":
	# 	msgbox = messagebox.showwarning("Enter the Email Id","Warning")
	# else:
	# 	msgbox = messagebox.showwarning("Sucess","Warning")





	if(re.search(emailValidate,EmailId)):
		
		top = Tk()
		top.withdraw()

		reciever = inpEmailid.get()
		otp = random.randint(1000, 10000)
		print(otp)
		message = "Dear Student,\nPlease verify you OTP {}".format(otp)
		sender = yagmail.SMTP('','')
		sender.send(to = reciever,subject = "Verification of Email ID",contents = message) 

		verifycode = int(simpledialog.askstring(title="Verify",prompt="Enter your OPT received on your Email ID {}".format(EmailId)))
		if verifycode == otp:
			try:
				sql = "insert into register values (%s, %s, %s, %s, %s, %s, %s)"
				val = (firstName, lastName, RegisterId, PhoneNumber, SelYear, SelDepart, EmailId)
				mycursor.execute(sql,val)
				mydb.commit()
				
				uname = str(firstName+str(RegisterId)+"@sakec")
				psd = ''.join((random.choice(string.ascii_lowercase) for x in range(10))) 
			
				reciever = inpEmailid.get()
				Usrpwd = " Congratulations !! You are verified. Your username and password is as follows:\n Username: {} \n Password: {} \n Kindly Change your Password as soon as possible.\n Thank You ".format(uname,psd)
				
				#Need to make New EMail id for this
				sender = yagmail.SMTP('','')
				sender.send(to = reciever,subject = "Verification of Email ID",contents = Usrpwd) 
				
				print(Usrpwd)
				print("Verified")

				sql1 = "insert into login values (%s, %s)"
				val1 = (uname, psd)
				mycursor.execute(sql1,val1)
				mydb.commit()


				print("Completed")

			except mysql.connector.Error as e:
				print("Not Sucess")

			finally:
				inpFirstName.set("")
				inpLastName.set("")
				inpRegisterId.set("")
				inpPhoneNumber.set("")
				clickedYear.set("")
				clickedDepart.set("")
				inpEmailid.set("")


		else:
			messagebox = messagebox.showwarning("Your OTP is not verified.Please Try again.")
			inpFirstName.set("")
			inpLastName.set("")
			inpRegisterId.set("")
			inpPhoneNumber.set("")
			clickedYear.set("")
			clickedDepart.set("")
			inpEmailid.set("")
			#print("Not verified")

		top.mainloop()
		#print("Valid Email")
	else:
		print("Invalid Email") 







inpFirstName = StringVar()
fistname = Label(root,text = "First Name").place(x = 20, y = 20)
inputfirstname = Entry(root, width=50, textvariable = inpFirstName).place(x = 100, y = 20)

inpLastName = StringVar()
lastname = Label(root,text = "Last Name").place(x = 20, y = 50)
inputlastname = Entry(root, width = 50, textvariable = inpLastName).place(x = 100, y = 50)

inpRegisterId = StringVar()
registerId = Label(root,text = "Registration ID").place(x = 20, y = 80)
inputregisterId = Entry(root, width = 50, textvariable = inpRegisterId).place(x = 100, y = 80)

inpPhoneNumber = StringVar()
phoneNumber = Label(root,text = "Phone Number").place(x = 20, y = 110)
inputphoneNumber = Entry(root, width = 50, textvariable = inpPhoneNumber).place(x = 100, y = 110)


optionYear = ["FE","SE","TE","BE"]
stdYear = Label(root, text = "Year").place(x = 20, y = 140)
clickedYear = StringVar()
inputstdYear = OptionMenu(root , clickedYear , *optionYear).place(x = 100, y = 140)

optionDepart = ["Information Technology",
				"Computer Engineering",
				"Electronics",
				"Electronics and Telecommunincations"]
stdDepart = Label(root, text = "Department").place(x = 20, y = 170)
clickedDepart = StringVar()
inputstdDepart = OptionMenu(root, clickedDepart, *optionDepart).place(x = 100, y = 170)

inpEmailid = StringVar()
emailId = Label(root,text = "Email ID").place(x = 20, y = 200)
inputemailId = Entry(root, width = 50, textvariable = inpEmailid).place(x = 100, y = 200)
 


submit = Button(root, text = "Submit", command = verify).place(x = 100,y = 240)


root.mainloop()