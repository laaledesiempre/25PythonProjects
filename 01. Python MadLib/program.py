import random

config={
  "lenguage_selected":False,
  "current_lenguage":"",
  "game_loop_excecuting": True,
}

spanish_texts={
  "intro_text": """Bienvenido a Python Madlibs, el juego es muy simple, voy a pedirte unas palabras y...
Generare una frase con las mismas, entretenido no? que cosas raras y aleatorias saldran? eso esta por verse...""",
  "sustantive_question":"Primero necesito que me digas un interesante sustantivo",
  "adjetive_question":"Oh y ahora un amable Adjetivo",
  "verb_question":"Ahora asi como corre el ciervo, dime un verbo",
  "random_word_question":"Y ahora quiera o no quiera, digame una palabra cualquiera!",
  "presentation_phrase":"""
  Vamos a ver, vamos a ver que vamos a ver...

  acá está el resultado:
  """,
  "enter_to_continue":"Presiona enter para continuar",
  "amable_end":"Espero te haya gustado!",
  "phrases":[
    ["Esta un ",", El cual estaba muy ",", Por eso se puso a ", ", Porque nadie sabe cuando va a aparecer "],
    ["Cuando aparece ",", Todo el mundo se pone ",", Por supuesto, ya que dan ganas de ",", Cuando se siente eso en "]
  ]
}
english_texts={
  "intro_text": """Welcome to Python Madlibs, this game is simple, i'm going to ask you some for some words and...
i 'll make a phrase with it!, funny isn't it? what a random and strange things are going to be? let's see...""",
  "sustantive_question":"Primero necesito que me digas un interesante sustantivo",
  "adjetive_question":"Oh y ahora un amable Adjetivo",
  "verb_question":"Ahora asi como corre el ciervo, dime un verbo",
  "random_word_question":"Y ahora quiera o no quiera, digame una palabra cualquiera!",
  "presentation_phrase":"""
Vamos a ver, vamos a ver que vamos a ver...

  acá está el resultado:

  """,
  "enter_to_continue":"Press Enter to Continue",
  "amable_end":"Hope you liked",
  "phrases":[
    ["It was a ",", Who was very ",", Because of that it started ", ", Because no one knows when "],
    ["When "," appears, Everybody ",", Of course, Because makes you want to ",", When you feel it in "]
  ]
}


current_lenguage= config["current_lenguage"]

def random_phrase_generator(array,sustantive,adjetive,verb,random_word):
  phrase= array[0]+sustantive+array[1]+adjetive+array[2]+verb+array[3]+random_word
  return phrase
  #f"{array[0]}{sustantive}{array[1]}{adjetive}{array[2]}{verb}{array[3]}{random_word}"

while config["lenguage_selected"] == False:
  print("""a. Español
b. English""")
  lenguage_selection=input()
  if lenguage_selection=="a":
    current_lenguage= spanish_texts
    config["lenguage_selected"]=True
  elif lenguage_selection=="b":
    current_lenguage= english_texts
    config["lenguage_selected"]=True
  else:
    print("?")

def GameLoop():
  print(current_lenguage["intro_text"])
  print(current_lenguage["enter_to_continue"])
  input()
  print(current_lenguage["sustantive_question"])
  sustantive= input()
  print(current_lenguage["adjetive_question"])
  adjetive= input()
  print(current_lenguage["verb_question"])
  verb= input()
  print(current_lenguage["random_word_question"])
  random_word= input()
  print(current_lenguage["presentation_phrase"])
  print(random_phrase_generator(random.choice(current_lenguage["phrases"]),sustantive,adjetive,verb,random_word))
  print("")
  print(current_lenguage["amable_end"])
  print(current_lenguage["enter_to_continue"])
  input()

while config["game_loop_excecuting"]==True:
  GameLoop()
