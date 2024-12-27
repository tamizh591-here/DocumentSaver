import pyautogui
import docx
import os
import keyboard

doc = docx.Document()
index = 0

def take_screenshot():
    global index
    screenshot = pyautogui.screenshot()
    screenshot_path = f'screenshot_{index}.png'
    screenshot.save(screenshot_path)
    doc.add_picture(screenshot_path)
    os.remove(screenshot_path)
    index += 1

print("Press 's' key to take screenshot or Press 'q' to exit and save document")

while True:
    if keyboard.is_pressed('s'):
        take_screenshot()
        print(f"Screenshot taken: {index}")
        while keyboard.is_pressed('s'):  
            pass

    if keyboard.is_pressed('q'):
        output_filename = input("Enter the document name with extension: ")
        doc.save(output_filename)
        print("File Saved Successfully !!")
        break
