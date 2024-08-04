# Aiden Rader
# 3/21/23

# Project Description: In this project, I will be creating a very simple application where it will ask
# which city you want to know the temperature, humidity, and the wind speed in.
# We will be using both the requests module and the Tkinter GUI framework to complete this task.

import tkinter as tk
import requests

api_key = "2ed7693ad3523f1c32904ca87adfb008"

def get_weather(city):
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        print(response.text)

    else:
        data = response.json()
        temperature = data["current"]["temperature"]
        feelsLike = data["current"]["feelslike"]
        weather_icon = data["current"]["weather_icons"]
        weather_des = data["current"]["weather_descriptions"]
        humid = data["current"]["humidity"]
        wind = data["current"]["wind_speed"]
        
        tempInFahren = (temperature * 1.8) + 32 
        feelsLikeInFahren = (feelsLike * 1.8) + 32

    #TODO: Figure out why weather icon does not display correctly
    return f"[Temperature: {tempInFahren}°F]\n[Feels Like: {feelsLikeInFahren}°F]\n{weather_icon}\n{weather_des}\n[Humidity: {humid}%]\n[Wind Speed: {wind} mph]"

def show_weather():
    city = city_entry.get()
    weather = get_weather(city)
    weather_label.config(text = weather)

# This is where we can start laying out the actual visual application 
win = tk.Tk()
win.title("Weather Channel") # The Window name or the application title

city_label = tk.Label(win, text = "Enter city:") #Text box to insert the name of the desired city
city_label.pack()

city_entry = tk.Entry(win) #User input inside the city_label textbox
city_entry.pack()

get_weather_button = tk.Button(win, text="Get Weather", command = show_weather)
get_weather_button.pack()

weather_label = tk.Label(win)
weather_label.pack()

win.mainloop() 
