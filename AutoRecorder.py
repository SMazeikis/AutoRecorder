import datetime, time, webbrowser, os

meeting_start  = 10       # this is 10 am local time.
meeting_length = 5*60*60  # this is 5 hours.
meeting_link   = Link_Here


print("Starting Script.. ")
print(f"Waiting for the meeting to start at {meeting_start} .. ")


while True:
    # set time for start of meeting hour here
    if datetime.datetime.now().time().hour == meeting_start: 
        print("Launching Meeting.. ")
        webbrowser.open(meeting_link)
        break
    else:
        time.sleep(3600-time.time()%3600)


print("Launching Recording.. ")

# launches recording for an hour and then kills the obs, saving the zoom recording
bashCommand = 'start /d "C:/Program Files/obs-studio/bin/64bit" obs64.exe --startrecording'
os.system(bashCommand)


print(f"Recording for {meeting_length/3600} hours.. ")

# set the length of meeting in seconds
time.sleep(meeting_length)
os.system("taskkill /F /IM obs64.exe")
