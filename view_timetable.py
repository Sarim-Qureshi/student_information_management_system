from tkinter import *
import mysql.connector

root = Tk()
root.geometry("1300x670+0+0")
root.resizable(False, False)
root.wm_iconbitmap('zicon.ico')
root.title('Student Information Management System')
root.configure(background='#222')

import sys

tname = ''
for i, x in enumerate(sys.argv):
    if i > 0:
        tname += x + " "

tname = tname.strip()

db = mysql.connector.connect(host='localhost', user='root', password='', database='sims')
c = db.cursor()
c.execute('select pdf from timetable where name=%s', (tname,))
result = c.fetchall()
file = None
for row in result:
    file = row[0]
with open('new.pdf', 'wb') as pdf:
    pdf.write(file)

from tkPDFViewer import tkPDFViewer as pdf

v1 = pdf.ShowPdf()
v2 = v1.pdf_view(root, pdf_location='new.pdf', width=100, height=500)
v2.pack(anchor='c', side='top')

root.mainloop()


# --------------Old code for image------------------------

# from tkinter import *
# import sys
# from PIL import Image, ImageTk, ImageFile
# from mysql.connector import MySQLConnection
# ImageFile.LOAD_TRUNCATED_IMAGES = True
#
# root = Tk()
# root.geometry("1300x670+0+0")
# root.resizable(False, False)
# root.title('Student Information Management System')
# root.configure(background='#222')
#
# import sys
# tname = ''
# for i, x in enumerate(sys.argv):
#     if i>0:
#         tname += x+" "
#
# tname = tname.strip()
#
# def write_file(data, filename):
#     with open(filename, 'wb') as f:
#         f.write(data)
#
#
# cnx = MySQLConnection(user='root', password='', host='localhost', database='sims')
# cursor = cnx.cursor()
# cursor.execute('select image from timetable where name=%s', (tname, ))
#
# photo = cursor.fetchone()[0]
# # write blob data into a file
# print(len(photo))
# write_file(photo, 'new.jpg')
# cursor.close()
# cnx.close()
#
# img = Image.open('new.jpg').resize((750, 750), resample=0)
# photo = ImageTk.PhotoImage(img)
# lab = Label(image=photo)
# lab.pack()
# import os
# if os.path.exists('new.jpg'):
#     os.remove('new.jpg')
# root.mainloop()

