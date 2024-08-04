import tkinter as tk

root = tk.Tk()
root.title('Light Switch App')

# Function defining what happens when the button is clicked
def onButtonPress(event):
    global buttonClicked
    buttonClicked = True
    root.iconbitmap(r'C:\Users\aiden\Downloads\pixil-frame-0 (2).ico')
    print(buttonClicked)

# Function defining what happens when the button is released
def onButtonRelease(event):
    global buttonClicked
    buttonClicked = False
    root.iconbitmap(r'C:\Users\aiden\Downloads\pixil-frame-0 (1).ico')
    print(buttonClicked)

buttonClicked = False

lightSwitch = tk.Button(root, text='On/Off', width=55)

# Bind the button press and release events to the corresponding functions
lightSwitch.bind("<ButtonPress-1>", onButtonPress)
lightSwitch.bind("<ButtonRelease-1>", onButtonRelease)

lightSwitch.pack()
root.mainloop()