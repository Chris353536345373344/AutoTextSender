from sqlite3 import Time
from pynput.keyboard import Controller, Key
import time

keyboard = Controller()


print("After you press start there will be a five second countdown and it will start doing its thing")
text = input("What message ")
interval = int(input("How long between messages (seconds) "))
Times = int(input("how many times "))


input("Start? (press enter)")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")




for x in range(Times):
    keyboard.type(text)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(interval)


time.sleep(10)
input("end of file")