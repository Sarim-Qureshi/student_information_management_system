from tkinter import *


def on_enterv(e):
    e.widget['background'] = '#fda507'
    e.widget['foreground'] = 'white'


def on_leavev(e):
    e.widget['background'] = '#fee227'
    e.widget['foreground'] = 'black'


def view_subjects():
    try:
        name = str(ls.get(ls.curselection()))
    except:
        return
    import os
    os.system(f'course_info2.py {name}')


root = Tk()
root.geometry("1000x670+0+0")
root.wm_iconbitmap('zicon.ico')
root.resizable(False, False)
root.configure(background='#222')
root.title('Student Information Management System')
head = Label(root, text=f'Course Details', font='consolas 30 bold')
head.pack(pady=(35, 0))
head.configure(background='#222', foreground='white')

f1 = Frame(root, width=300, height=70, borderwidth=10, relief='groove')
f1.configure(background='#999')
f1.pack(pady=(50, 20), anchor='c')


sb = Scrollbar(f1)
sb.pack(side='right', fill='y')
ls = Listbox(f1, yscrollcommand=sb.set, width=40, height=10)
ls.config(font='comicsanms 18 bold')
ls.pack()
sb.config(command=ls.yview)

li = ["Information Technology",
                "Computer Engineering",
                "Electronics",
                "Electronics and Telecommunications"]
for x in range(1,9):
    for y in li:
        ls.insert(END, f'Sem {x} {y}')


f2 = Frame(root, width=600, height=300, borderwidth=10, relief='groove')
f2.configure(background='#999')
f2.pack(pady=(50, 20), padx=(60, 5), anchor='c')

bv = Button(f2, text='View subjects', command=view_subjects, cursor='hand2', font='consolas 14 bold', pady=1, padx=10)
bv.bind("<Enter>", on_enterv)
bv.bind("<Leave>", on_leavev)
bv.grid(row=0, column=1)
bv.configure(background='#fee227')
root.mainloop()
