
import pywhatkit as kit
import pyautogui
import time
import datetime
import os
import random


def send_image(image_path):
    pyautogui.click(x=800, y=950) 
    time.sleep(1)
    pyautogui.click(x=800, y=850)
    time.sleep(1)
    pyautogui.write(image_path)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=1350, y=950)

def list_images(folder_path):
    return [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]


image_folder_path = r'C:\Users\Binay\Downloads\images'  # Update this with your folder path
contact_path = r'C:\Users\Binay\Downloads\contacts.txt'


def list_images(folder_path):
    print(f"Checking folder path: {folder_path}")
    if os.path.exists(folder_path):
        return [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    else:
        print(f"The folder path '{folder_path}' does not exist.")
        return []


with open(contact_path, 'r') as file:
    contacts = file.read().splitlines()

message = "Binay Gupta,You Got Selected"

now = datetime.datetime.now()
hour = now.hour
minutes = now.minute + 1

for contact in contacts:
    images = list_images(image_folder_path)
    if not images:
        print("No images found in the folder.")
        continue

    random_image_path = os.path.join(image_folder_path, random.choice(images))

    kit.sendwhatmsg(contact, message, hour, minutes)
    
    print(f'Message scheduled to {contact} at {hour}:{minutes}')

    time.sleep(5) 

    send_image(random_image_path)  # Send the random image

    minutes += 2
    if minutes >= 60:
        minutes = 0
        hour += 1
