import datetime, time, webbrowser, subprocess
from os import listdir
from os.path import isfile, join
import os

while True: 
    if datetime.datetime.now().time().hour == 20: 
        webbrowser.open("google.com")
        break
    else:
        time.sleep(3600-time.time()%3600)


# launches recording for an hour and then kills the obs, saving the zoom recording
# time.sleep(30)
bashCommand = 'start /d "C:/Program Files/obs-studio/bin/64bit" obs64.exe --startrecording'
os.system(bashCommand)

time.sleep(30)
os.system("taskkill /F /IM obs64.exe")