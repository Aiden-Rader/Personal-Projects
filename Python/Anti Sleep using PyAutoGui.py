# Aiden Rader
# 2/13/23
# This was a test program which incorporates the pyautogui module in python, I wanted to see if moving a mouse cursor every 5-10 seconds
# would negate the "away" feature on Microsoft Teams/Skype, this works but I would'nt reccomend!  

import pyautogui
import keyboard
import random
import time

while True:
    x = random.randint(0, pyautogui.size()[0])
    y = random.randint(0, pyautogui.size()[1])
    pyautogui.moveTo(x, y)

    time.sleep(5)  

    if keyboard.is_pressed('x'):  # check if 'x' key is pressed
        break                     # exit the loop if 'x' key is pressed