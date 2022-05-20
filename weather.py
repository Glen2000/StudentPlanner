import sys
import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import simpledialog

import tkinter as tk

root = tk.Tk()

canvas_1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas_1.pack()

label_1 = tk.Label(root, text='Check the weather')
label_1.config(font=('helvetica', 14))
canvas_1.create_window(200, 25, window=label_1)

label_2 = tk.Label(root, text='Type your county:')
label_2.config(font=('helvetica', 10))
canvas_1.create_window(200, 100, window=label_2)

entry_1 = tk.Entry(root)
canvas_1.create_window(200, 140, window=entry_1)


def getWeather():
    location = entry_1.get()

    if location == "Antrim" or location == "antrim":
        URL = "https://www.rte.ie/weather/100002-antrim/"

    elif location == "Armagh" or location == "armagh":
        URL = "https://www.rte.ie/weather/100009-armagh/"

    elif location == "Carlow" or location == "carlow":
        URL = "https://www.rte.ie/weather/10466-carlow/"

    elif location == "Cavan" or location == "cavan":
        URL = "https://www.rte.ie/weather/12291-cavan/"

    elif location == "Clare" or location == "clare":
        URL = "https://www.rte.ie/weather/12544-clare/"

    elif location == "Cork" or location == "cork":
        URL = "https://www.rte.ie/weather/16366-cork/"

    elif location == "Derry" or location == "derry":
        URL = "https://www.rte.ie/weather/19430-derry/"

    elif location == "Donegal" or location == "donegal":
        URL = "https://www.rte.ie/weather/20235-donegal/"

    elif location == "Down" or location == "down":
        URL = "https://www.rte.ie/weather/20597-down/"

    elif location == "Dublin" or location == "dublin":
        URL = "https://www.rte.ie/weather/22259-dublin/"

    elif location == "Galway" or location == "galway":
        URL = "https://www.rte.ie/weather/24237-galway/"

    elif location == "Kerry" or location == "kerry":
        URL = "https://www.rte.ie/weather/28730-kerries%20east/"

    elif location == "Kildare" or location == "kildare":
        URL = "https://www.rte.ie/weather/29305-kildare/"

    elif location == "Kilkenny" or location == "kilkenny":
        URL = "https://www.rte.ie/weather/29569-kilkenny/"

    elif location == "Leitrim" or location == "leitrim":
        URL = "https://www.rte.ie/weather/34115-leitrim/"

    elif location == "Limerick" or location == "limerick":
        URL = "https://www.rte.ie/weather/34382-limerick/"

    elif location == "Longford" or location == "longford":
        URL = "https://www.rte.ie/weather/35523-longford/"

    elif location == "Louth" or location == "louth":
        URL = "https://www.rte.ie/weather/35837-louth/"

    elif location == "Mayo" or location == "mayo":
        URL = "https://www.rte.ie/weather/36627-mayo/"

    elif location == "Meath" or location == "meath":
        URL = "https://www.rte.ie/weather/36649-meath%20hill/"

    elif location == "Monaghan" or location == "monaghan":
        URL = "https://www.rte.ie/weather/37360-monaghan/"

    elif location == "Offaly" or location == "offaly":
        URL = "https://www.rte.ie/weather/22660-edenderry/"

    elif location == "Roscommon" or location == "roscommon":
        URL = "https://www.rte.ie/weather/42315-roscommon/"

    elif location == "Sligo" or location == "sligo":
        URL = "https://www.rte.ie/weather/44092-sligo/"

    elif location == "Tipperary" or location == "tipperary":
        URL = "https://www.rte.ie/weather/45602-tipperary/"

    elif location == "Tyrone" or location == "tyrone":
        URL = "https://www.rte.ie/weather/47165-tyrone/"

    elif location == "Waterford" or location == "waterford":
        URL = "https://www.rte.ie/weather/47396-waterford/"

    elif location == "Wexford" or location == "wexford":
        URL = "https://www.rte.ie/weather/47452-wexford/"

    elif location == "Wicklow" or location == "wicklow":
        URL = "https://www.rte.ie/weather/47557-wicklow/"

    else:
        sys.exit("Please try again with a correct county")

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='compact-nav')
    s = (str(soup))
    match = re.search(r'<span class="temperature">\d{1,5}', s)
    if match:
        x = (match.group(0))

    match2 = re.search(r'\d{1,5}', x)
    temp = (match2.group(0))

    label3 = tk.Label(root, text='The temperature of ' + location + ' is:', font=('helvetica', 10))
    canvas_1.create_window(200, 210, window=label3)

    label4 = tk.Label(root, text=temp + "°C", font=('helvetica', 10, 'bold'))
    canvas_1.create_window(200, 230, window=label4)


button1 = tk.Button(text='Get the temp', command=getWeather, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas_1.create_window(200, 180, window=button1)

root.mainloop()




#print("Temp =", temp + "°C")