import os
import pyautogui
import time
time.sleep(5)


for i in range(2, 11):
    pyautogui.typewrite(f"msrewardstest{i}@hi2.in")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)