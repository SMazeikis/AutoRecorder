import datetime, time, webbrowser, os

meeting_start  = (2,33)     # this is hh:mm local time.
meeting_length = 1*60  # (in seconds) this is 2 hours entirely.

rejoin_time=int(0.5*60) # (in sec) rejoin every 0.5 minute

meet_id="123123123123"
meet_pass="123123"

check_every=1*60 # Check for if there is meeting every 1 minutes(Must be less than pre-meet)
pre_meet= 5*60 # Time to start this process before actual start of meeting
post_meet=int(0.2*60) # Time to record after scheduled record end time

if check_every>pre_meet:
    check_every = pre_meet

def create_meetlink(meet_id, meet_pass=""):
    #Creates zoommtg link doesn't requires browser permission (more safe.Hope so!)
    if isinstance(meet_id,int) or (isinstance(meet_id,str) and meet_id.isdigit()):
        pass_param="&pwd={}".format(meet_pass) if (meet_pass) else ""
        meeting_link   = "zoommtg://zoom.us/join?action=join&confno={0}{1}".format(meet_id,pass_param)
        return meeting_link
    else:
        print("Invalid Meeting Id (Contains non numerals characters)")

def calculate_time_range(meeting_start,meeting_length,rejoin_time=0):
    # Calculate possible time range of meeting derived from rejoin time
    start_time = meeting_start[0]*60*60+meeting_start[1]*60
    
    end_time = start_time+meeting_length+post_meet

    then = start_time +rejoin_time
    t_range=[]
    
    if rejoin_time!=0:
        t_range.append((start_time - pre_meet ,
                 int(min(start_time+rejoin_time,end_time))))
        
        while then+rejoin_time<=end_time:
            t_range.append((then ,
                 then+rejoin_time))
            then +=rejoin_time
        
    if(then<end_time and rejoin_time!=0):
        t_range.append((then ,
             end_time))

    return t_range

def check_time(time_range,meet_link,check_every):
    while True:
        # set time for start of meeting hour here
        success=False
        for i in range(len(time_range)):
            print(time_range)
            now = datetime.datetime.now().time().hour*60*60+datetime.datetime.now().time().minute*60
            success=False
            if now in range(time_range[i][0],time_range[i][1]): 
                print("Launching Meeting.. ")
                webbrowser.open(meet_link)
                success=True
                return True
        if(not success):
            time.sleep(check_every)


def main():
    meet_link = create_meetlink(meet_id,meet_pass)
    time_range=calculate_time_range(meeting_start,meeting_length,rejoin_time)
    
    print("Starting Script.. ")
    print("Waiting for the meeting to start at time {0}:{1} LST .. ".format(meeting_start[0],meeting_start[1]))

    print("Launching Recording.. ")

    # launches recording for an hour and then kills the obs, saving the zoom recording
    bashCommand = 'start /d "C:/Program Files/obs-studio/bin/64bit" obs64.exe --startrecording --multi --scene "Zoom Meet"'
    os.system(bashCommand)

    print(f"Recording for {round(meeting_length/3600,2)} hours.. ")
    
    while True:
        check_time(time_range,meet_link,check_every)
        # set the length of meeting in seconds
        time.sleep(rejoin_time)
        
        # Bug if last interval less than rejoin time then record for more time
        now = datetime.datetime.now().time().hour*60*60+datetime.datetime.now().time().minute*60
        start_time = meeting_start[0]*60*60+meeting_start[1]*60
    
        end_time = start_time+meeting_length+post_meet
        print(now,start_time,end_time)
        if now>end_time:
            break
    os.system("taskkill /F /IM obs64.exe")

main()
