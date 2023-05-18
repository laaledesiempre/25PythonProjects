import time
class configuration:
    main_loop=True
    timer_runner=True
    minutes_selected=False
    seconds_selected=False
    minutes=0
    seconds=0
config=configuration()


while config.main_loop:
    config.minutes_selected=False
    config.seconds_selected=False
    print("This is a timer! press ENTER to create a new timer")
    input()
    while not config.minutes_selected:
        print("how many minutes? you can put a number between 60 and 0 included")
        minutes_input=input()
        try:
            minutes_input=int(minutes_input)
        except:
            print("this is not valid")
            continue
        if minutes_input<=60 and minutes_input>=0:
            config.minutes=minutes_input
            config.minutes_selected=True
        else:
            print("this is not valid")
    while not config.seconds_selected:
        print("how many seconds? you can put a number between 59 and 1 included")
        seconds_input=input()
        try:
            seconds_input=int(seconds_input)
        except:
            print("this is not valid")
            continue
        if  seconds_input<=59 and  seconds_input>=1:
            config.seconds= seconds_input
            config.seconds_selected=True
        else:
            print("this is not valid")
    print(config.minutes,":",config.seconds)
    config.timer_runner=True
    while config.timer_runner:
        time.sleep(1)
        if config.seconds==0:
            if not config.minutes==0:
                config.minutes-=1
                config.seconds=59
            else:
                print("is time")
                config.timer_runner=False
        else:
            config.seconds-=1
        print(config.minutes,":",config.seconds)
