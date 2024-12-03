import time
from datetime import datetime
import pygame

#intialize pygame mixer for sound playback
pygame.mixer.init()

#load the alarm sound (replace given alarm sound with your actual sound file)
pygame.mixer.music.load('alarm soundd.mp3')

def set_alarm(alarm_time):
    """this function waits until the current time match the alarm time"""
    print(f"alarm is set for {alarm_time} waiting")

    while True:
        #get the current time
        current_time = datetime.now().strftime("%H:%M:%S")

        #check if current time matches the alarm time  
        if current_time == alarm_time:
            print("time's up! alarm ringing...")
            pygame.mixer.music.play()

            #keep the alarm ringing until the user stops it
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break

        #sleep for 1 second to avoid continuous CPU usage
        time.sleep(1)

#get the alarm time from user in 24-hour format (Example: "14:30:00")
alarm_time = input("enter the alarm time (HH:MM:SS):")

#set the alarm
set_alarm(alarm_time)
