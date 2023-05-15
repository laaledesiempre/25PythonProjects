import random

class GameConfig:
    player_choised=False
    game_loop=True

class Dialogs:
    rock_scisors="Rock brokes the Scisors"
    paper_rock="Paper wrap the Rock"
    scisors_paper="Scisors cut the Paper"

text= Dialogs()
config= GameConfig()
choices= ["rock","paper","scisors"]

while config.game_loop==True:
    print("Lets play rock, paper, scisors, what do you choose?")

    while config.player_choised==False:
        selection= input()
        if selection in choices:
            config.player_choised=True
        else:
            print("that is not paper, rock or scisors")

    computer_selection= random.choice(choices)
    print(f"computer choose {computer_selection}")
    if selection == computer_selection:
        print("it's a tie")
    elif selection=="scisors" and computer_selection=="paper":
        print(f"{text.scisors_paper}, player wins!")
    elif selection=="scisors" and computer_selection=="rock":
        print(f"{text.rock_scisors}, computer wins!")
    elif selection=="rock" and computer_selection=="paper":
        print(f"{text.paper_rock}, computer wins!")
    elif selection=="rock" and computer_selection=="scisors":
        print(f"{text.rock_scisors}, computer wins!")
    elif selection=="paper" and computer_selection=="scisors":
        print(f"{text.scisors_paper}, computer wins!")
    elif selection=="paper" and computer_selection=="rock":
        print(f"{text.paper_rock}, computer wins!")
    config.player_choised=False
    print("press enter to continue")
    input()
