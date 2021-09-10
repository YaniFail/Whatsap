from pynput.keyboard import Key, Controller
import time
keyboard= Controller()
time.sleep(5)
while True:
    for letter in "Ups Autobot :D lol":
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)