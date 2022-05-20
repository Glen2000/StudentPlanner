from tkinter import *
from tkinter import ttk



ws = Tk()
ws.title('Grades Page')
ws.attributes("-fullscreen", True)
ws.config(bg='white')
# IMAGE TAKEN FROM:
# https://www.shutterstock.com/search/grading
img = PhotoImage(file="grades.png")
f = ("Times bold", 10)
m = ("Times", 12)

mylabel = Label(ws, text='', font="0")
mylabel.pack()
myscroll = Scrollbar(ws)
myscroll.pack(side=RIGHT, fill=Y)
mylist = Listbox(ws, yscrollcommand=myscroll.set)




def nextPage():
    ws.destroy()
    import RoomLocations

def prevPage():
    ws.destroy()
    import Inbox

def weatherPage():
    ws.destroy()
    import weatherAPI

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
    text="Previous Page",
    font=f,
    command=prevPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Next Page",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Text Editor",
    font=f,
    command=weatherPage
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
