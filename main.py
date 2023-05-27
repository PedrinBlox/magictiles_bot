#Tile 1 | X: 830 Y: 589
#Tile 2 | X: 888 Y: 589
#Tile 3 | X: 937 Y: 589
#Tile 4 | X: 1058 Y: 589
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(832, 444)[0] == 0:
        click(832, 444)
    if pyautogui.pixel(913, 444)[0] == 0:
        click(913, 444)
    if pyautogui.pixel(1004, 444)[0] == 0:
        click(1004, 444)
    if pyautogui.pixel(1105, 444)[0] == 0:
        click(1105, 444)
