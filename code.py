import pywhatkit as pw
import pyautogui as pt
from time import sleep
list = ['+91XXXXXXXXX','+91XXXXXXXXX']
msg = "Hello, This is User, Welcome to the world of Python" 
for i in list:
    pw.sendwhats_image(i,'C:/Users/HP/Documents/cnn.png',msg)
    pt.press("enter")
    sleep(1)
    