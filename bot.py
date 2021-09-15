# https://www.crazygames.com/game/magic-piano-tiles

from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(377, 482)[0] == 0:
        click(377, 482)
    if pyautogui.pixel(452, 482)[0] == 0:
        click(452, 482)
    if pyautogui.pixel(527, 482)[0] == 0:
        click(527, 482)
    if pyautogui.pixel(600, 482)[0] == 0:
        click(600, 482)
