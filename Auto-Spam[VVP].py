import pyautogui, pyperclip, random, time
from http import server
from re import S
from this import d
from unicodedata import name
import keyboard
import smtplib

from threading import Semaphore, Timer

print("Spam Treo War Facebook / PC")
msg = input("[Auto-Spam] Nhap noi dung can spam dài dài càng tốt!: ").split(" ||")
n = int(input("[Auto-Spam] Nhap so lan spam thôi bé! "))
m = float(input("[Auto-Spam] nhap so time delay nữa bé!: "))

print("Chuẩn bị spam chết con đĩ mẹ nó thôi nào")
for i in range(5,0,-1):
    print(i,end="...",flush='True')
print('Bắt đầu chửi chết mẹ nó nè!')

for i in range(n):
	pyperclip.copy(random.choice(msg))
	pyautogui.hotkey("ctrl","v")
	pyautogui.press("enter")
	time.sleep(m) #Delay
