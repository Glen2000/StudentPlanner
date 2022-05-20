from tkinter import *
from tkinter import ttk
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
calendar = outlook.GetDefaultFolder(9)
appointments = calendar.Items

new_lst = []

for appointment in appointments:
    new_lst.append(appointment.Subject)

x = ('\n'.join(new_lst))

ws = Tk()
ws.title('Room Locations')
ws.attributes("-fullscreen", True)
ws.config(bg='white')
# IMAGE TAKEN FROM:
# https://www.istockphoto.com/photo/september-2021-calendar-on-yellow-background-gm1298563635-391399204
img = PhotoImage(file="calendar.png")
f = ("Times bold", 10)
m = ("Times", 12)

mylabel = Label(ws, text='', font="0")
mylabel.pack()
myscroll = Scrollbar(ws)
myscroll.pack(side=RIGHT, fill=Y)
mylist = Listbox(ws, yscrollcommand=myscroll.set)

for appointment in appointments:
    mylist.insert(END, str(appointment.Subject))
mylist.pack(side = BOTTOM, fill = BOTH, padx=500, pady=100 )


def RoomLocation():
    ws.destroy()
    import RoomLocations

def Inbox():
    ws.destroy()
    import Inbox

def weatherPage():
    ws.destroy()
    import weatherAPI

def annoucements():
    ws.destroy()
    import googleClassroom

def grades():
    ws.destroy()
    import Grades

def textEdit():
    ws.destroy()
    import textedit

def appointments():
    ws.destroy()
    import Appointments


Label(
    ws,
    image=img,
    padx=0,
    pady=0,
    bg='#bd580b',
    font=f
).pack(expand=True, fill=BOTH)

Label(
    ws,
    font=m,
    text=myscroll.config(command = mylist.yview) ,
    height=2,
    width=53
).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="Room Locations",
    font=f,
    bg='#0a8a6a',
    fg="white",
    command=RoomLocation
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Appointments",
    font=f,
    bg='#c787a1',
    fg="white",
    command=appointments
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Inbox",
    font=f,
    bg='#7c1380',
    fg="white",
    command=Inbox
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Weather",
    font=f,
    bg='#d49b0b',
    fg="white",
    command=weatherPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Announcements",
    font=f,
    bg='#045912',
    fg="white",
    command=annoucements
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Grades",
    font=f,
    bg='#113c91',
    fg="white",
    command=grades
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Text Editor",
    font=f,
    bg='#7a5cdb',
    fg="white",
    command=textEdit
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="EXIT",
    font=f,
    bg='#e82305',
    fg="white",
    command=ws.destroy
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
