import pyautogui
import time

#while True:    
    #aa =pyautogui.position()
    #print(aa)
    #time.sleep(1)
time.sleep(10)
#x=280 y=260 checkbox 278 260 inbox position
#x=427 y=156 trashcan 429 159 inbox position
#x=279   y=239    checkbox         social inbox
#x= 531   y= 155   trashcan         social inbox
for i in range(10):
    
    for i in range(150):
            pyautogui.moveTo(280,260,duration=0.15)
            pyautogui.click(280,260)
            time.sleep(.1)
            pyautogui.moveTo(427,156,duration=0.15)
            time.sleep(.1)
            pyautogui.click(427,156)
