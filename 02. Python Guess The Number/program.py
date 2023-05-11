import random

PLAYER_GAMEMODE="player"

COMPUTER_GAMEMODE="computer"

class config:
    game_mode_selected= False
    game_mode=""
    game_loop=True
    game_number_selected=False

configuration = config()

while configuration.game_mode_selected==False:
    print("""Play as:
        a.guesser
        b.Let the computer guess""")
    game_mode= input()
    if game_mode == "a":
        configuration.game_mode_selected=True
        configuration.game_mode= PLAYER_GAMEMODE
    elif game_mode == "b":
        configuration.game_mode_selected=True
        configuration.game_mode= PLAYER_GAMEMODE
    else:
        print("?")
if configuration.game_mode==PLAYER_GAMEMODE:
    while configuration.game_loop==True:
        configuration.game_number_selected=False
        print("I'm the genius computer, i can guess the numbers in your mind, Please, tell me a number from 1 to 5")
        while configuration.game_number_selected==False:
            number_selected= input()
            if number_selected!="" and int(number_selected)<6 and int(number_selected)>0:
                configuration.game_number_selected=True
            else:
                print("That is not a valid Number")
        random_number= random.randrange(1,6)
        print(f"I say the number... {random_number}")
        print("")
        if str(random_number)==number_selected:
            print("I guessed, i'm awesome")
        else:
            print("oh, i failed, you win!")
        print("Press Enter to play again!")
        input()
elif configuration.game_mode==COMPUTER_GAMEMODE:
    "asd"
else:
    print("How did you get here? o.O")
