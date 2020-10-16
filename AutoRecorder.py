import datetime, time, webbrowser, os

while True:
    # set time for start of meeting hour here
    if datetime.datetime.now().time().hour == 3: 
        webbrowser.open("LINK OF MEETING")
        break
    else:
        time.sleep(3600-time.time()%3600)

# launches recording for an hour and then kills the obs, saving the zoom recording
bashCommand = 'start /d "C:/Program Files/obs-studio/bin/64bit" obs64.exe --startrecording'
os.system(bashCommand)

# set the length of meeting in seconds
time.sleep(30)
os.system("taskkill /F /IM obs64.exe")