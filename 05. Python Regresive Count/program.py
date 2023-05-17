import time
class configuration:
    timer_runner=True
    minutes_selected=False
    seconds_selected=False
    minutes=0
    seconds=0
config=configuration()
while not config.minutes_selected:
    print("how many minutes? you can put a number between 60 and 0 included")
    minutes_input=input()
    if minutes_input<=60 and minutes_input>=0:
        minutes=minutes_input
        config.minutes_selected=True
    else:
        print("this is not valid")
while not config.seconds_selected:
    print("how many seconds? you can put a number between 59 and 1 included")
    seconds_input=input()
    if  seconds_input<=59 and  seconds_input>=1:
        seconds= seconds_input
        config.seconds_selected=True
    else:
        print("this is not valid")
while config.timer_runner:
    time.sleep(1)
    seconds+=1
    print(seconds)