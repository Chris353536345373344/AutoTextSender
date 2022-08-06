from sqlite3 import Time
from pynput.keyboard import Controller, Key
import time
import random

keyboard = Controller()


print("After you press start there will be a five second countdown and it will start doing its thing")
Multiple = input("Multiple? True/False cap sensitive  ")

if (Multiple == "False"):
	text = ("(Python message) ") + input("What message ")

else:
	text1 = ("(Python message) ") + input("What message ")
	text2 = ("(Python message) ") + input("What message ")
	text3 = ("(Python message) ") + input("What message ")
	text4 = ("(Python message) ") + input("What message ")
	text5 = ("(Python message) ") + input("What message ")
	TextList = [text1, text2, text3, text4, text5]

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



if (Multiple == "False"):
	for x in range(Times):
		keyboard.type(text)
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		time.sleep(interval)


if (Multiple == "True"):
	for x in range(Times):
		whmessage = random.randint(0, 4)
		keyboard.type(TextList[whmessage])
		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
		time.sleep(interval)
		
	

time.sleep(0.2)
input("end of file")