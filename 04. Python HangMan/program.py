import random
#---------------------------------------------
#classes and objects

#states

class configuration_data:
    words=["horse","tatami","amigo","sunscreen","pizza","chocolate","python","dog","chile","eggplant","sunset","parasite","castle","summer","winter","palace","quinoa","camera"]
    letter_selected=False
    letters_on_load=""
    game_ended=False
    game_loop=True
config= configuration_data()

#display

class man_stages:
    failures=0
    current_head=""" """
    current_body="""   """
    current_legs="""   """
    def failure(self):
        self.failures+=1
        if self.failures==1:
            self.current_head="""0"""
        elif self.failures==2:
            self.current_body=""" | """
        elif self.failures==3:
            self.current_body="""/| """
        elif self.failures==4:
            self.current_body="""/|\\"""
        elif self.failures==5:
            self.current_legs="""/  """
        elif self.failures==6:
            self.current_legs="""/ \\"""
    def reset(self):
        current_head=""" """
        current_body="""   """
        current_legs="""   """
    def display(self):
        return f"""
   |
   |
  {self.current_head}
 {self.current_body}
 {self.current_legs}

 
"""
stickman= man_stages()
#---------------------------------------------
#methods

#Win checker

def winChecker(string1,string2):
    if string1==string2:
        print("you win, press enter to play again")
        config.letters_on_load=""
        stickman.reset()
        config.game_ended=True
    elif stickman.failures>=6:
        print("you lose, press enter to play again")
        config.letters_on_load=""
        stickman.reset()
        config.game_ended=True

#text trasnformation function
def showText(word):
    final_string=""
    for letterin in word:
        if letterin in config.letters_on_load:
            final_string+=letterin.upper()
        else:
            final_string+=" _ "
    winChecker(word,final_string.lower())#revisar
    return final_string
#end of text, function

def checker(letter,word):
    if len(letter)>1 and len(letter)<1:
        print("No valid, just one letter")
    elif letter in word:
        config.letters_on_load+=letter
        config.letter_selected=True
    else:
        stickman.failure()
        config.letter_selected=True

#---------------------------------------------
#game

while config.game_loop:
    print("Welcome to our game, press ENTER to start")
    input()
    word=random.choice(config.words)
    config.game_ended=False
    while not config.game_ended:
        print(stickman.display())
        print(showText(word))
        config.letter_selected=False
        while not config.letter_selected:
            letter=input()
            checker(letter,word)
