from tkinter import *
import sys
from PIL import Image, ImageTk
from mysql.connector import MySQLConnection

root = Tk()
root.geometry("1300x670+0+0")
root.resizable(False, False)
root.title('Student Information Management System')
root.configure(background='#222')


def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)


cnx = MySQLConnection(user='root', password='', host='localhost', database='sims')
cursor = cnx.cursor()
cursor.execute('select image from timetable where name=%s', (sys.argv[1], ))
photo = cursor.fetchone()[0]
# write blob data into a file
write_file(photo, 'new.jpg')
cursor.close()
cnx.close()

img = Image.open('new.jpg')
photo = ImageTk.PhotoImage(img)
lab = Label(image=photo)
lab.pack()
import os
if os.path.exists('new.jpg'):
    os.remove('new.jpg')
root.mainloop()

