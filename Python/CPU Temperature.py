import psutil
import tkinter as tk

def get_CPUTemp(temperature):

    temperature = psutil.sensors_temperatures()
    cpu_temp = temperature['coretemp'][0].current

    print(f"CPU temperature: {(cpu_temp * 1.8) + 32}°F")
    
def show_CPUTemp():


    # This is where we can start laying out the actual visual application
    win = tk.Tk()
    win.title("CPU Temp")  # The Window name or the application title
