import tkinter as tk
import win32com.client
from tkinter import *
from tkinter import ttk

root = tk.Tk()

canvas_1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas_1.pack()

label_1 = tk.Label(root, text='Select an outlook folder\n9-CALENDAR, 6-INBOX')
label_1.config(font=('helvetica', 13))
canvas_1.create_window(200, 25, window=label_1)

label_2 = tk.Label(root, text='Type your Number:')
label_2.config(font=('helvetica', 10))
canvas_1.create_window(200, 100, window=label_2)

entry_1 = tk.Entry(root)
canvas_1.create_window(200, 140, window=entry_1)



def getFolder():
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    x1 = entry_1.get()

    calendar = outlook.GetDefaultFolder(x1)
    appointments = calendar.Items
    new_lst = []

    if x1 == '9':
        for appointment in appointments:
            new_lst.append(appointment.Body)

    elif x1 == '6':
        for appointment in appointments:
            new_lst.append(appointment.Body)

    label3 = tk.Label(root, text='The folder has been selected', font=('helvetica', 10))
    canvas_1.create_window(200, 210, window=label3)

    label4 = tk.Label(root, text=new_lst, font=('helvetica', 10, 'bold'))
    canvas_1.create_window(200, 230, window=label4)


button1 = tk.Button(text='Get the folder', command=getFolder, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas_1.create_window(200, 180, window=button1)

root.mainloop()