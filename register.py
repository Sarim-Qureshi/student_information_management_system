from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import mysql.connector
import re
import yagmail
import random
import string


def on_enter2(e):
    e.widget['background'] = '#033500'
    e.widget['foreground'] = 'white'


def on_leave2(e):
    e.widget['background'] = '#3cb043'
    e.widget['foreground'] = 'black'


emailValidate = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def verify():

    firstName = inpFirstName.get().strip()
    lastName = inpLastName.get().strip()
    RegisterId = inpRegisterId.get().strip()
    PhoneNumber = inpPhoneNumber.get().strip()
    SelYear = clickedYear.get().strip()
    SelDepart = clickedDepart.get().strip()
    EmailId = inpEmailid.get().strip()
    Sem = clickedSem.get().strip()

    if len(firstName) == 0 or len(lastName) == 0 or len(RegisterId) == 0 or len(PhoneNumber) == 0 or len(
            SelYear) == 0 or len(SelDepart) == 0 or len(EmailId) == 0 or len(Sem) == 0:
        messagebox.showwarning("Empty fields", "Enter all the fields")
        return
    else:
        if re.search(emailValidate, EmailId) and re.search(r'^[789]\d{9}$', PhoneNumber):

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="SIMS"
            )

            mycursor = mydb.cursor()

            try:
                mycursor.execute('select has_account from register where email=%s', (EmailId,))
                res = mycursor.fetchall()
                ha = int((res[0])[0])
            except Exception as e:
                print(e)
                messagebox.showerror('Error', 'Your credentials are invalid')
            mydb.close()
            if ha==1:
                messagebox.showwarning("Account exists", "You already have an account. If you want to"
                                                   "change your credentials contact the office in the college or send a mail to"
                                                   " <office.sakec@sakec.ac.in>")
                return
            else:
                register(firstName, lastName, RegisterId, PhoneNumber, SelYear, SelDepart, EmailId, Sem)
        else:
            messagebox.showerror('Message', 'Ensure that phone number and email ID are valid')



def register(firstName, lastName, RegisterId, PhoneNumber, SelYear, SelDepart, EmailId, Sem):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="SIMS"
        )

        mycursor = mydb.cursor()
        sql = "select * from register where email=%s"
        mycursor.execute(sql, (EmailId, ))
        res = mycursor.fetchall()
        fn = (res[0])[0]
        ln = (res[0])[1]
        ri = str((res[0])[2])
        pn = str((res[0])[3])
        yr = (res[0])[4]
        dep = (res[0])[5]
        email = (res[0])[6]
        sem = str((res[0])[9])

        if firstName != fn or lastName != ln or RegisterId != ri or PhoneNumber != pn or SelYear != yr or SelDepart != dep or EmailId != email or Sem != sem:
            messagebox.showerror('Invalid credentials', 'Your credentials are invalid')
            return

        top = Tk()
        top.withdraw()

        reciever = inpEmailid.get()
        otp = random.randint(1000, 10000)
        message = "Dear Student,\nPlease verify your OTP {}".format(otp)

        sender = yagmail.SMTP(user='studentmanagement336@gmail.com', password='admin1234admin')
        sender.send(to=reciever, subject="Verification of Email ID", contents=message)

        verifycode = int(simpledialog.askstring(title="Verify",
                                                prompt="Enter the OPT received on your Email ID {}".format(EmailId)))
        if verifycode == otp:
            try:


                uname = str(firstName + str(RegisterId) + "@sakec")
                psd = ''.join((random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8)))

                reciever = inpEmailid.get()
                Usrpwd = "Congratulations {} {}!! You are verified. Your username and password are as follows:\nUsername: {}\nPassword: {}" \
                         "\nTo change your credentials, contact the office in the college or send a mail to <office.sakec@sakec.ac.in>\nThank You ".format(
                    firstName, lastName, uname, psd)
                messagebox.showinfo("Verified", "Kindly check your email for username and password")

                # Need to make New EMail id for this
                sender = yagmail.SMTP(user='studentmanagement336@gmail.com', password='admin1234admin')
                sender.send(to=reciever, subject="Verification of Email ID", contents=Usrpwd)


                sql1 = "insert into login values (%s, %s, %s)"
                val1 = (uname, psd, 'student', )
                mycursor.execute(sql1, val1)
                mydb.commit()

                mycursor.execute('update register set has_account=1, username=%s where email=%s', (uname, EmailId, ))
                mydb.commit()

                mydb.close()

                root.destroy()

            except mysql.connector.Error as e:
                messagebox.showerror('Error!', 'An error occurred!! Try again later')

            finally:
                inpFirstName.set("")
                inpLastName.set("")
                inpRegisterId.set("")
                inpPhoneNumber.set("")
                clickedYear.set("")
                clickedDepart.set("")
                inpEmailid.set("")
                clickedSem.set("")


        else:
            messagebox.showerror("Incorrect OTP", "Fatal!! Your OTP is not correct.")
            inpFirstName.set("")
            inpLastName.set("")
            inpRegisterId.set("")
            inpPhoneNumber.set("")
            clickedYear.set("")
            clickedDepart.set("")
            inpEmailid.set("")

        top.mainloop()


root = Tk()
root.geometry("1300x670+0+0")
root.resizable(False, False)
root.title('Student Information Management System')
root.configure(background='#222')

head = Label(root, text='Create an account', font='consolas 30 bold')
head.pack(pady=(5, 0))
head.configure(background='#222', foreground='white')

f1 = Frame(root, width=800, height=500, borderwidth=10, relief='groove')
f1.configure(background='#999')
f1.pack(pady=(10, 10), padx=(60, 5), anchor='c')

inpFirstName = StringVar()
firstname = Label(f1, text="First Name", font='consolas 15 bold')
firstname.grid(row=0, column=0, pady=(15, 15), padx=(70, 20))
firstname.configure(background='#999')

inputfirstname = Entry(f1, width=20, textvariable=inpFirstName, font='consolas 15 bold')
inputfirstname.grid(row=0, column=1, pady=(15, 15), padx=(20, 70))
# inputfirstname.configure(background='#999')

inpLastName = StringVar()
lastname = Label(f1, text="Last Name", font='consolas 15 bold')
lastname.grid(row=1, column=0, pady=(15, 15), padx=(70, 20))
lastname.configure(background='#999')

inputlastname = Entry(f1, width=20, textvariable=inpLastName, font='consolas 15 bold')
inputlastname.grid(row=1, column=1, pady=(15, 15), padx=(20, 70))
# inputlastname.configure(background='#999')

inpRegisterId = StringVar()
registerId = Label(f1, text="Registration ID", font='consolas 15 bold')
registerId.grid(row=2, column=0, pady=(15, 15), padx=(70, 20))
registerId.configure(background='#999')

inputregisterId = Entry(f1, width=20, textvariable=inpRegisterId, font='consolas 15 bold')
inputregisterId.grid(row=2, column=1, pady=(15, 15), padx=(20, 70))
# inputregisterId.configure(background='#999')

inpPhoneNumber = StringVar()
phoneNumber = Label(f1, text="Phone Number", font='consolas 15 bold')
phoneNumber.grid(row=3, column=0, pady=(15, 15), padx=(70, 20))
phoneNumber.configure(background='#999')

inputphoneNumber = Entry(f1, width=20, textvariable=inpPhoneNumber, font='consolas 15 bold')
inputphoneNumber.grid(row=3, column=1, pady=(15, 15), padx=(20, 70))
# inputphoneNumber.configure(background='#999')

optionYear = ["FE", "SE", "TE", "BE"]
stdYear = Label(f1, text="Year", font='consolas 15 bold')
stdYear.grid(row=4, column=0, pady=(15, 15), padx=(70, 20))
stdYear.configure(background='#999')

clickedYear = StringVar()
inputstdYear = OptionMenu(f1, clickedYear, *optionYear,)
inputstdYear.grid(row=4, column=1, pady=(15, 15), padx=(20, 70))
inputstdYear.configure(background='#999', font='consolas 12 bold')

optionSem = ["1", "2", "3", "4", "5", "6", "7", "8"]
stdSem = Label(f1, text="Semester", font='consolas 15 bold')
stdSem.grid(row=5, column=0, pady=(15, 15), padx=(70, 20))
stdSem.configure(background='#999')

clickedSem = StringVar()
inputstdSem = OptionMenu(f1, clickedSem, *optionSem,)
inputstdSem.grid(row=5, column=1, pady=(15, 15), padx=(20, 70))
inputstdSem.configure(background='#999', font='consolas 12 bold')

optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]

stdDepart = Label(f1, text="Department", font='consolas 15 bold')
stdDepart.grid(row=6, column=0, pady=(15, 15), padx=(70, 20))
stdDepart.configure(background='#999')

clickedDepart = StringVar()
inputstdDepart = OptionMenu(f1, clickedDepart, *optionDepart)
inputstdDepart.grid(row=6, column=1, pady=(15, 15), padx=(20, 70))
inputstdDepart.configure(background='#999', font='consolas 12 bold')

inpEmailid = StringVar()
emailId = Label(f1, text="Email ID", font='consolas 15 bold')
emailId.grid(row=7, column=0, pady=(15, 15), padx=(70, 20))
emailId.configure(background='#999')

inputemailId = Entry(f1, width=20, textvariable=inpEmailid, font='consolas 15 bold')
inputemailId.grid(row=7, column=1, pady=(15, 15), padx=(20, 70))
# inputemailId.configure(background='#999')

b3 = Button(f1, text="Register", cursor='hand2', command=verify, font='consolas 15 bold')
b3.grid(row=8, column=0, columnspan=2, pady=(15, 15), padx=(70, 70))
b3.bind("<Enter>", on_enter2)
b3.bind("<Leave>", on_leave2)
b3.configure(background='#3cb043')

root.mainloop()
