import os
import time
from tkinter import *
import threading

try:
    import pyautogui
    import pyperclip     
except ImportError:
    print("Trying to Install required module: requests\n")
    os.system('python -m pip install pyautogui')
    os.system('python -m pip install pyperclip')
    import pyautogui
    import pyperclip 

root = Tk()
root.minsize(200, 100)
root.resizable(width=False, height=False)
root.title("Color Picker")

isActive = False
hexa = "#40E0D0"



label =  Label(root, text=" Press (ctrl + Alt + c) to copy color code")
label.pack(pady=40)

# Change Color Function
def change_color():
    global hexa, isActive
    while isActive:
        positon =  pyautogui.position()
        im = pyautogui.screenshot()
        color = im.getpixel(positon)
        hexa = '#%02x%02x%02x' % color
        root.configure(bg=hexa)
        time.sleep(1)



# t1 =  threading.Thread(target=change_color)
# t1.start()


def focusIn(event):
    global isActive    
    print('focusIn')
    isActive = True
    t1 =  threading.Thread(target=change_color)
    t1.start()


def focusOut(event):
    global isActive
    print('focusOut')
    isActive = False

def copyFunction(event):
        global hexa
        pyperclip.copy(hexa)
        print("Success!")
# if window not minimized
root.bind('<Map>', focusIn)
# if winow minimized
root.bind('<Unmap>', focusOut)
# if window in focus 
root.bind('<FocusIn>', focusIn)
# if window focused out
root.bind('<FocusOut>', focusOut)
# if mouse enter the widget
root.bind('<Enter>', focusOut)
# when mouse out the widget
root.bind('<Leave>', focusIn)
root.bind('<Control-Alt-c>', copyFunction)


# Stop all loop after closing close button
def on_closing():
    global isActive
    isActive = False    
    root.destroy()


def on_closing_ctrl_C(event):
    global isActive
    isActive = False    
    root.destroy()
root.bind('<Control-c>', on_closing_ctrl_C)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()