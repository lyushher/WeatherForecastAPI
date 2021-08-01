import tkinter as tk
from tkinter import*
import time
import requests

HEIGHT = 550
WIDTH = 650

def format_response(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]

        final_str = "City: %s \nConditions: %s \nTemperature(F): %s" % (name, desc, temp)
    except:
        final_str = "ERROR!"

    return final_str

def get_weather(city):
    weatherAPI_key = "bd8d3ed3b1734e5bbea29fce537ab589"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weatherAPI_key, "q": city, "units": "imperial"}
    response = requests.get(url, params=params)
    weather = response.json()
    label["text"] = format_response(weather)

root = tk.Tk()
root.title("Weather Forecast")

canvas = tk.Canvas(root, bg="#d0e9f0",height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="#c9c5e8", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=("PT Serif", 18))
entry.place(relx=0.27,relwidth=0.72, relheight=1)

search = tk.Button(frame, text="Search", fg="#5548b7", font=("PT Serif", 23), command=lambda: get_weather(entry.get()))
search.place(relx=0.01, relwidth=0.24, relheight=1)

lower_frame = tk.Frame(root, bg="#c9c5e8", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=("PT Serif", 28))
label.place(relwidth=1, relheight=1)


def clock_date():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")

    day = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day_name = time.strftime("%A")

    clock_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
    clock_label.after(1000, clock_date)

    date_label.config(text=day + "." + month + "." + year + " " + day_name)

date_label = Label(lower_frame, fg="#5548b7",font=("PT Serif", 20))
date_label.place(rely=0.03, relx=0.55)

clock_label = Label(lower_frame, fg="#25a01c", font=("PT Serif", 15))
clock_label.place( rely=0.13, relx=0.62)

clock_date()
root.mainloop()