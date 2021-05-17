from tkinter import *
import sys
import os
import mysql.connector


def on_enter2(e):
    e.widget['background'] = '#033500'
    e.widget['foreground'] = 'white'


def on_leave2(e):
    e.widget['background'] = '#3cb043'
    e.widget['foreground'] = 'black'


def attendance():
    if len(clickedSem.get().strip()) == 0 or len(clickedDepart.get().strip()) == 0:
        return
    sem = clickedSem.get().strip()
    dept = clickedDepart.get().strip()

    import sys
    os.system(f'attendance.py {sys.argv[1]} {sem} {dept}')


    # if sys.argv[1] != 'faculty':
    #     db = mysql.connector.connect(host='localhost', user='root', password='', database='sims')
    #     c = db.cursor()
    #     c.execute('select firstname, lastname, department from register where registration_id=%s', (sys.argv[1],))
    #     result = c.fetchall()
    #     result = result[0]
    #     os.system(f'update_marks3.py {exam} {sys.argv[1]} {result[0]} {result[1]} {result[2]} 0')
    # else:
    #     if len(clickedSem.get().strip()) == 0 or len(clickedDepart.get().strip()) == 0:
    #         return
    #
    #     # if cb.get():
    #     #     exam += 'kt'
    #     os.system(f'update_marks2.py {exam} {dept}')


root = Tk()
root.geometry("1100x550+0+0")
root.resizable(False, False)
root.title('Student Information Management System')
root.configure(background='#222')
# if sys.argv[1] == 'faculty':
head = Label(root, text='Mark attendance', font='consolas 30 bold')
# else:
#     head = Label(root, text='Check attendance', font='consolas 30 bold')
head.pack(pady=(35, 0))
head.configure(background='#222', foreground='white')

f1 = Frame(root, width=600, height=300, borderwidth=10, relief='groove')
f1.configure(background='#999')
f1.pack(pady=(50, 20), padx=(60, 5), anchor='c')

# optionExam = ["Internal Assessment 1", "Internal Assessment 2"]
# stdExam = Label(f1, text="Exam", font='consolas 20 bold')
# stdExam.grid(row=1, column=0, pady=(15, 15), padx=(70, 20))
# stdExam.configure(background='#999')

# clickedExam = StringVar()
# inputstdExam = OptionMenu(f1, clickedExam, *optionExam, )
# inputstdExam.grid(row=1, column=1, pady=(15, 15), padx=(20, 70))
# inputstdExam.configure(background='#999', font='consolas 16 bold')

optionSem = ["1", "2", "3", "4", "5", "6", "7", "8"]
stdSem = Label(f1, text="Semester", font='consolas 20 bold')
stdSem.grid(row=2, column=0, pady=(15, 15), padx=(70, 20))
stdSem.configure(background='#999')

clickedSem = StringVar()
inputstdSem = OptionMenu(f1, clickedSem, *optionSem, )
inputstdSem.grid(row=2, column=1, pady=(15, 15), padx=(20, 70))
inputstdSem.configure(background='#999', font='consolas 16 bold')

optionDepart = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]

stdDepart = Label(f1, text="Department", font='consolas 20 bold')
stdDepart.grid(row=3, column=0, pady=(15, 15), padx=(70, 20))
stdDepart.configure(background='#999')

clickedDepart = StringVar()
inputstdDepart = OptionMenu(f1, clickedDepart, *optionDepart)
inputstdDepart.grid(row=3, column=1, pady=(15, 15), padx=(20, 70))
inputstdDepart.configure(background='#999', font='consolas 16 bold')

# if sys.argv[1] == 'faculty':
b3 = Button(f1, text="Mark", cursor='hand2', command=attendance, font='consolas 15 bold')
# else:
#     b3 = Button(f1, text="Check", cursor='hand2', command=update_marks, font='consolas 15 bold')
b3.grid(row=4, column=0, columnspan=2, pady=(15, 15), padx=(70, 70))
b3.bind("<Enter>", on_enter2)
b3.bind("<Leave>", on_leave2)
b3.configure(background='#3cb043', font='consolas 16 bold')

root.mainloop()
