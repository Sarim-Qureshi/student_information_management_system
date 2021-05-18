from tkinter import Tk, Label, Button, Frame, filedialog, messagebox, StringVar, Entry, IntVar, Checkbutton
import mysql.connector
import os


def on_enter(e):
    e.widget['background'] = '#051094'
    e.widget['foreground'] = 'white'


def on_leave(e):
    e.widget['background'] = '#0277bd'
    e.widget['foreground'] = 'black'


def on_enter2(e):
    e.widget['background'] = '#033500'
    e.widget['foreground'] = 'white'


def on_leave2(e):
    e.widget['background'] = '#3cb043'
    e.widget['foreground'] = 'black'


def add_timetable():
    import re
    result = re.search(r'\w+', pdf_name.get())
    if cb0.get() == 0 and result is None:
        messagebox.showinfo('Enter the timetable name', 'Make sure to enter a sensible timetable name to proceed')
    else:
        filename = filedialog.askopenfilename(defaultextension='.pdf',
                                              filetypes=[('pdf file', '*.pdf'), ('All files', '*.*')])

        # print(os.path.splitext(os.path.basename(filename))[0])
        file = open('code.txt', 'wb')
        with open(filename, 'rb') as f:
            for line in f.readlines():
                file.write(line)
        file.close()
        with open('code.txt', 'rb') as f:
            data = f.read()
        if cb0.get() == 1:
            timetable_name = str(os.path.splitext(os.path.basename(filename))[0])
        else:
            timetable_name = pdf_name.get()
        db = mysql.connector.connect(host='localhost', user='root', password='', database='sims')
        c = db.cursor()
        print(len(data))
        try:
            c.execute('insert into timetable values(%s, %s, %s)', (timetable_name.strip(), data, cb.get()))
            db.commit()
        except:
            db.rollback()
        db.close()
        messagebox.showinfo('Success', 'Your timetable was added successfully')
        if os.path.exists("code.txt"):
            os.remove("code.txt")


def edit_timetable_list():
    os.system('update_timetable2.py exam')


root = Tk()
root.geometry("1000x670+0+0")
root.resizable(False, False)
root.title('Student Information Management System')
root.wm_iconbitmap('zicon.ico')
root.configure(background='#222')
head = Label(root, text='Add timetables', font='consolas 30 bold')
head.pack(pady=(35, 0))
head.configure(background='#222', foreground='white')


f1 = Frame(root, width=800, height=500, borderwidth=10, relief='groove')
f1.configure(background='#999')
f1.pack(pady=(50, 20), padx=(60, 5), anchor='c')


name = Label(f1, text='Enter timetable name:', font='consolas 18 bold')
name.grid(row=0, column=0, pady=(45, 40), padx=(70, 20))
name.configure(background='#999')

pdf_name = StringVar()
pdf_entry = Entry(f1, textvariable=pdf_name, font='consolas 17 bold')
pdf_entry.grid(row=0, column=1, pady=(45, 40), padx=(20, 70))

cb0 = IntVar()
use_pdf_name = Checkbutton(f1, text='Use filename as timetable name?', font='consolas 14 bold', variable=cb0)
use_pdf_name.grid(row=1, column=0, columnspan=2, pady=(7, 15), padx=(70, 70))
use_pdf_name.configure(background='#999')

cb = IntVar()
visible_to_student = Checkbutton(f1, text='Visible to students?', font='consolas 14 bold', variable=cb)
visible_to_student.grid(row=2, column=0, columnspan=2, pady=(7, 15), padx=(70, 70))
visible_to_student.configure(background='#999')

b2 = Button(f1, text='Click here to Upload pdf file', command=add_timetable, cursor='hand2', font='consolas 18 bold', pady=1, padx=10)
b2.bind("<Enter>", on_enter)
b2.bind("<Leave>", on_leave)
b2.grid(row=3, column=0, columnspan=2, pady=(20, 45), padx=(70, 70))
b2.configure(background='#0277bd')

f2 = Frame(root, width=800, height=500, borderwidth=10, relief='groove')
f2.configure(background='#999')
f2.pack(pady=(50, 20), padx=(60, 5), anchor='c')

b3 = Button(f2, text='Edit timetables list', command=edit_timetable_list ,cursor='hand2', font='consolas 18 bold', pady=1, padx=10)
b3.bind("<Enter>", on_enter2)
b3.bind("<Leave>", on_leave2)
b3.pack()
b3.configure(background='#3cb043')

root.mainloop()