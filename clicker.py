import mouse
import keyboard
import time
import pyautogui
from PIL import Image

#myScreenshot=pyautogui.screenshot()

#locationCookie=pyautogui.locateOnScreen('')







enter_pressed=False

while True:
    if(keyboard.is_pressed("enter") or enter_pressed==True):
        enter_pressed=True
        while True:
            if keyboard.is_pressed("space")==False:
                mouse.move(350, 650, absolute=True, duration=0)
                mouse.click('left')
                time.sleep(0.0001)
            if keyboard.is_pressed("shift+space"):
                enter_pressed=False
                break
            

        
    
