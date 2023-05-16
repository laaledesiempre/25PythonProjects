
import random

words=["caballo"]
letter_selected=False
global letters_on_load
letters_on_load=""
game_ended=False
game_loop=True

#Win checker
def winChecker(string1,string2):
    if string1==string2:
        print("you win")
        game_ended=True
    elif stickman.failures>=6:
        print("you lose")
        game_ended=True


#display
"""
   0
  /|\\
  / \\

"""
current_word=""
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
stickman= man_stages()
display=f"""
   |
   |
  {stickman.current_head}
 {stickman.current_body}
 {stickman.current_legs}

 
"""
#end of display
#text function
def showText(word):
    final_string=""
    for letterin in word:
        if letterin in letters_on_load:
            final_string+=letterin.upper()
        else:
            final_string+=" _ "
    winChecker(word,final_string)
    return final_string
#end of text, function
def checker(letter,word,lol):
    if len(letter)>1 and len(letter)<1:
        print("No valid, just one letter")
    elif letter in word:
        lol=lol+letter
        letter_selected=True
    else:
        stickman.failure()
        letter_selected=True



#game

while game_loop:
    print("Welcome to our game, press ENTER to start")
    input()
    word=random.choice(words)
    game_ended=False
    while not game_ended:
        print(display)
        print(showText(word))
        letter_selected=False
        while not letter_selected:
            letter=input()
            checker(letter,word,letters_on_load)
            print(letter_selected)
