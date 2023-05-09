config={
  "lenguage_selected":False,
  "current_lenguage":"",
}

spanish_texts={
  "intro_text": """Bienvenido a Python Madlibs, el juego es muy simple, voy a pedirte unas palabras y...
Generare una frase con las mismas, entretenido no? que cosas raras y aleatorias saldran? eso esta por verse...""",
  "sustantive_question":6,
  "adjetive_question":6,
  "verb_question":6,
  "random_word_question":6,
}
english_texts={
  "intro_text": """Welcome to Python Madlibs, this game is simple, i'm going to ask you some for some words and...
i 'll make a phrase with it!, funny isn't it? what a random and strange things are going to be? let's see...""",
  "sustantive_question":6,
  "adjetive_question":6,
  "verb_question":6,
  "random_word_question":6,
}
current_lenguage= config["current_lenguage"]

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
print(current_lenguage["intro_text"])