from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
import time

def controlMouse():
    mouse = MouseController()
    print("Moving mouse...")
    mouse.position = (500, 200)
    print(f"Mouse moved to {mouse.position}")

def controlKeyboard():
    keyboard = KeyboardController()
    print("Typing...")
    # Give a moment to switch focus if needed
    time.sleep(1) 
    keyboard.type("HELLOJJ")
    print("Typed 'HELLOJJ'")

if __name__ == "__main__":
    # You can run this script in a separate terminal while KeyLog.py is running
    controlMouse()
    controlKeyboard()
