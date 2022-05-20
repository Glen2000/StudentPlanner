from tkinter import *
from tkinter import ttk
import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
calendar = outlook.GetDefaultFolder(9)
appointments = calendar.Items

new_lst = []

for appointment in appointments:
    new_lst.append(appointment.Location)

x = ('\n'.join(new_lst))

ws = Tk()
ws.title('Room Locations')
ws.attributes("-fullscreen", True)
ws.config(bg='white')
# IMAGE TAKEN FROM:
# https://www.pinterest.ie/pin/288934132345151288/visual-search/?x=16&y=16&w=538&h=537&cropSource=6&imageSignature=3e6e0fe48f1e97ad27c496f4b8100024
img = PhotoImage(file="room_number.PNG")
f = ("Times bold", 10)
m = ("Times", 12)

mylabel = Label(ws, text='', font="0")
mylabel.pack()
myscroll = Scrollbar(ws)
myscroll.pack(side=RIGHT, fill=Y)
mylist = Listbox(ws, yscrollcommand=myscroll.set)

for appointment in appointments:
    mylist.insert(END, str(appointment.Location))
mylist.pack(side = BOTTOM, fill = BOTH, padx=500, pady=100 )

def appointments():
    ws.destroy()
    import Appointments

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
    text="Inbox",
    font=f,
    bg='#7c1380',
    fg="white",
    command=Inbox
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
