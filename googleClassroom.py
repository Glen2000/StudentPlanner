from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

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

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly','https://www.googleapis.com/auth/classroom.announcements', 'https://www.googleapis.com/auth/classroom.courses.readonly']

#<------------------------------------------------------------------------------------------------------------>

root = Tk()
root.attributes("-fullscreen", True)
root.configure(bg='#474548')
# IMAGE TAKEN FROM:
# https://www.griswold.k12.ct.us/ghs/about/announcements-and-news
img = PhotoImage(file="accouncements.PNG")

canvas_1 = tk.Canvas(root, width=400, height=300,bg="#474548",highlightthickness=0, relief='raised')
canvas_1.pack()

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

label_1 = tk.Label(root, text='Google classroom Annoucements')
label_1.config(font=('helvetica', 30), fg = 'white', bg="#474548")
canvas_1.create_window(200, 25, window=label_1)
canvas_1.configure(bg='#474548')

#<------------------------------------------------------------------------------------------------------------>

# Dropdown menu options
options = [
    "COMP4604",
    "CMAP4002"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Module")

#<------------------------------------------------------------------------------------------------------------>

def main():
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('classroom', 'v1', credentials=creds)

        # Call the Classroom API
        results = service.courses().list(pageSize=10).execute()
        courses = results.get('courses', [])

        if not courses:
            print('No courses found.')
            return
        # Prints the names of the first 10 courses.
        print('Courses:')

        for course in courses:
            print(course['name'], course['alternateLink']), course['id']

        get_data = service.courses()
        soup = get_data.list().execute()
        data = soup['courses']

        name_course = [name['name'] for name in data]  # name of the course
        course_id = [id['id'] for id in data]  # course ID
        course_id_1 = course_id[0]
        announcement = get_data.announcements()
        announcement_data_COMP4604 = announcement.list(courseId=course_id[0]).execute()
        announcement_data_CMAP4002 = announcement.list(courseId=course_id[1]).execute()

        if (clicked.get() == 'COMP4604'):
            result_2 = str(announcement_data_COMP4604)
            spltData_2 = result_2.split(",")
            annoucement_2 = (spltData_2[2])
            creationTime_2 = (spltData_2[5])

            cleanedCreationTime_2 = creationTime_2.replace("'creationTime': '", '')
            cleanedAnnoucement_2 = annoucement_2.replace("'text': '",'')

            lbl.config(text="\n\n"+cleanedCreationTime_2.replace("'", '') + "\n" + cleanedAnnoucement_2.replace("\\xa0'", ''))
            lbl.configure(fg="white", bg='#474548')

        elif (clicked.get() == 'CMAP4002'):
            result_1 = str(announcement_data_CMAP4002)
            spltData_1 = result_1.split(",")
            annoucement_1 = (spltData_1[2])
            creationTime_1 = (spltData_1[5])

            cleanedCreationTime_1 = creationTime_1.replace("'creationTime': '", '')
            cleanedAnnoucement_1 = annoucement_1.replace("'text': '",'')

            lbl.config(text="\n\n"+cleanedCreationTime_1.replace("'", '') + "\n" + cleanedAnnoucement_1.replace("\\xa0'", ''))
            lbl.configure(fg="white",bg='#474548')

        else:
            lbl.config(text="\n\nPlease select a module from the drop down menu")
            lbl.configure(fg="white", bg='#474548')

    except HttpError as error:
        print('An error occurred: %s' % error)

button1 = tk.Button(text='Get announcements', command=main, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))

canvas_1.create_window(200, 270, window=button1)

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.pack()
canvas_1.create_window(200, 180, window=drop)

# Label Creation
lbl = tk.Label(root, text = "")
lbl.configure(fg="white",bg='#474548')
lbl.pack()

label_2 = tk.Label(root, text='Select a subject')
label_2.config(bg="#474548",fg="white",font=('helvetica', 18))
canvas_1.create_window(200, 100, window=label_2)
canvas_1.configure(bg='#474548')

#<------------------------------------------------------------------------------------------------------------>
Label(
    root,
    image=img,
    font=f,
    bg="#474548",
    fg="#474548"
).pack(expand=TRUE, fill=BOTH)

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
    text="Inbox",
    font=f,
    bg='#7c1380',
    fg="white",
    command=Inbox
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