import sys
from tkinter import simpledialog

import sys

import matplotlib
import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import simpledialog
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, date
from tkinter import *
import tkinter as tk
import requests
import json
from datetime import datetime
from PIL import Image

#<------------------------------------------------------------------------------------------------------------>

root = tk.Tk()
root.attributes("-fullscreen", True)
# IMAGE TAKEN FROM:
# https://www.rte.ie/brainstorm/2020/0720/1154337-the-medieval-roots-of-modern-weather-forecasts/
img = PhotoImage(file="grades.PNG")
img2 = PhotoImage(file="grades_2.PNG")


canvas_1 = tk.Canvas(root, width=400, height=230, relief='raised')
canvas_1.pack()

canvas_2 = tk.Canvas(root, width=400, height=230, relief='raised')
canvas_2.pack()

canvas_3 = tk.Canvas(root, width=400, height=230, relief='raised')
canvas_3.pack()

canvas_4 = tk.Canvas(root, width=400, height=230, relief='raised')
canvas_4.pack()

f = ("Times bold", 10)

def RoomLocation():
    root.destroy()
    import RoomLocations

def Inbox():
    root.destroy()
    import Inbox

def weatherPage():
    root.destroy()
    import weatherAPI

def annoucements():
    root.destroy()
    import googleClassroom

def grades():
    root.destroy()
    import Grades

def textEdit():
    root.destroy()
    import textedit

def appointments():
    root.destroy()
    import Appointments

label_1 = tk.Label(root, text='Check your grades')
label_1.config(font=('helvetica', 30), fg = '#fc0505')
canvas_1.create_window(200, 25, window=label_1)

#<------------------------------------------------------------------------------------------------------------>

def getWeather():
    GUI_ = entry_1.get()
    Embedded_Systems_ = entry_2.get()
    mobile_apps_ = entry_3.get()
    ccna_ = entry_4.get()

    if GUI_.isdigit() and Embedded_Systems_.isdigit() and mobile_apps_.isdigit() and ccna_.isdigit():
        if int(GUI_) in range (-1,101) and int(Embedded_Systems_) in range (-1,101) and int(mobile_apps_) in range (-1,101) and int(ccna_) in range (-1,101):
            lbl.config(text="A pie-chart has been generated displaying your results")

            y = np.array([GUI_, Embedded_Systems_, mobile_apps_, ccna_])
            mylabels = ["GUI " + "(" + GUI_ + "%)",
                        "Embedded_Systems " + "(" + Embedded_Systems_ + "%)",
                        "mobile_apps " + "(" + mobile_apps_ + "%)",
                        "CCNA " + "(" + ccna_ + "%)"]

            plt.pie(y, labels=mylabels, startangle=90)
            today = date.today()
            hostname = ("Student" + "_" + "results" + "_" + str(today))
            plt.savefig(hostname + '.png')

            im = Image.open(r"C:\Users\gleno\PycharmProjects\changing_pages_test1\Student_results_" + str(today) + ".png")
            im.show()

        else:
            lbl.config(text="Please ensure all grades are between 0-100")

    else:
        lbl.config(text= "Please ensure all fields have been filled in and are numerical values")

button1 = tk.Button(text='Get the grade', command=getWeather, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))


canvas_1.create_window(200, 180, window=button1)
canvas_2.create_window(200, 180, window=button1)
canvas_3.create_window(200, 180, window=button1)
canvas_4.create_window(200, 180, window=button1)

# Label Creation
lbl = tk.Label(root, text = "")
lbl.pack()

label_2 = tk.Label(root, text='GUI GRADE:')
label_2.config(font=('helvetica', 18))
canvas_1.create_window(200, 100, window=label_2)

label_3 = tk.Label(root, text='EMBEDDED SYSTEMS GRADE:')
label_3.config(font=('helvetica', 18))
canvas_2.create_window(200, 100, window=label_3)

label_4 = tk.Label(root, text='MOBILE APPS GRADE:')
label_4.config(font=('helvetica', 18))
canvas_3.create_window(200, 100, window=label_4)

label_5 = tk.Label(root, text='CCNA GRADE:')
label_5.config(font=('helvetica', 18))
canvas_4.create_window(200, 100, window=label_5)

entry_1 = tk.Entry(root)
canvas_1.create_window(200, 140, window=entry_1)

entry_2 = tk.Entry(root)
canvas_2.create_window(200, 140, window=entry_2)

entry_3 = tk.Entry(root)
canvas_3.create_window(200, 140, window=entry_3)

entry_4 = tk.Entry(root)
canvas_4.create_window(200, 140, window=entry_4)
#<------------------------------------------------------------------------------------------------------------>
Label(
    root,
    #image=img,
    font=f
).pack(expand=TRUE, fill=BOTH)

label = Label(
    root,
    image=img2
)
label.place(x=0, y=170)

label = Label(
    root,
    image=img
)
label.place(x=1170, y=180)

Button(
    root,
    text="Room Locations",
    font=f,
    bg='#0a8a6a',
    fg="white",
    command=RoomLocation
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root,
    text="Appointments",
    font=f,
    bg='#c787a1',
    fg="white",
    command=appointments
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root,
    text="Inbox",
    font=f,
    bg='#7c1380',
    fg="white",
    command=Inbox
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root,
    text="Weather",
    font=f,
    bg='#d49b0b',
    fg="white",
    command=weatherPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root,
    text="Announcements",
    font=f,
    bg='#045912',
    fg="white",
    command=annoucements
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root,
    text="Grades",
    font=f,
    bg='#113c91',
    fg="white",
    command=grades
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root,
    text="Text Editor",
    font=f,
    bg='#7a5cdb',
    fg="white",
    command=textEdit
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    root,
    text="EXIT",
    font=f,
    bg='#e82305',
    fg="white",
    command=root.destroy
).pack(fill=X, expand=TRUE, side=LEFT)

root.mainloop()

#<------------------------------------------------------------------------------------------------------------>
