from tkinter import *
import tkinter as tk
import requests
import json
from datetime import datetime

#<------------------------------------------------------------------------------------------------------------>

root = tk.Tk()
root.attributes("-fullscreen", True)
# IMAGE TAKEN FROM:
# https://www.rte.ie/brainstorm/2020/0720/1154337-the-medieval-roots-of-modern-weather-forecasts/
img = PhotoImage(file="weather.PNG")

canvas_1 = tk.Canvas(root, width=400, height=230, relief='raised')
canvas_1.pack()
f = ("Times bold", 10)

def appointments():
    root.destroy()
    import Appointments

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

def backupWeather():
    root.destroy()
    import weather

def textEdit():
    root.destroy()
    import textedit

label_1 = tk.Label(root, text='Check the weather')
label_1.config(font=('helvetica', 30), fg = '#fc0505')
canvas_1.create_window(200, 25, window=label_1)

#<------------------------------------------------------------------------------------------------------------>

def getWeather():
    location = entry_1.get()
    # Get the time from utc and timezone values provided
    # pass the value as utc + timezone (both are UTC timestamp)
    def time_from_utc_with_timezone(utc_with_tz):
        local_time = datetime.utcfromtimestamp(utc_with_tz)
        return local_time.time()

    # Enter your API key
    api_key = "d08c1e524b45c190eb3c055a94714dff"

    # Get city name from user
    city_name = location

    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key

    try:
        # Get the response from weather url
        response = requests.get(weather_url)

        # response will be in json format and we need to change it to pythonic format
        weather_data = response.json()




        if weather_data['cod'] == 200:
            kelvin = 273.15  # Temp is displayed in kelvin, this value will be used to convert to celsius
            temp_input = int(weather_data['main']['temp'] - kelvin)  # Ask user to enter city name
            temp = str(temp_input).upper()
            feels_like_temp = int(weather_data['main']['feels_like'] - kelvin)
            pressure = weather_data['main']['pressure']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed'] * 3.6
            sunrise = weather_data['sys']['sunrise']
            sunset = weather_data['sys']['sunset']
            timezone = weather_data['timezone']
            cloudy = weather_data['clouds']['all']
            description = weather_data['weather'][0]['description']

            sunrise_time = time_from_utc_with_timezone(sunrise + timezone)
            sunset_time = time_from_utc_with_timezone(sunset + timezone)

            cityName = (f"Weather Information for City: {city_name}")
            temperature = (f"Temperature (Celsius): {temp}")
            tempFeels = (f"Feels like in (Celsius): {feels_like_temp}")
            hpa = (f"Pressure: {pressure} hPa")
            humid = (f"Humidity: {humidity}%")
            windSpeed = ("Wind speed: {0:.2f} km/hr".format(wind_speed))
            timeOfSunset = (f"Sunrise at {sunrise_time} and Sunset at {sunset_time}")
            cloud = (f"Cloud: {cloudy}%")
            desc = (f"Info: {description}")
            lbl.config(text = str(cityName)+"\n"+str(temperature)+str(tempFeels)+"\n"+str(hpa)+"\n"+str(humid)+"\n"+str(windSpeed)+"\n"+str(timeOfSunset)+"\n"+str(cloud)+"\n"+str(desc))
        else:
            lbl.config(text = "City entered was not found, try again")
            print(f"City Name: {city_name} was not found!")

    except:
        lbl.config(text="Error has occurred, switching to backup weather program now")
        button1 = tk.Button(text='Get the temp', command=backupWeather, bg='brown', fg='white',
                            font=('helvetica', 9, 'bold'))
        canvas_1.create_window(200, 180, window=button1)

button1 = tk.Button(text='Get the temp', command=getWeather, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas_1.create_window(200, 180, window=button1)

# Label Creation
lbl = tk.Label(root, text = "")
lbl.pack()

label_2 = tk.Label(root, text='Type your county:')
label_2.config(font=('helvetica', 18))
canvas_1.create_window(200, 100, window=label_2)

entry_1 = tk.Entry(root)
canvas_1.create_window(200, 140, window=entry_1)
#<------------------------------------------------------------------------------------------------------------>
Label(
    root,
    image=img,
    font=f
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
