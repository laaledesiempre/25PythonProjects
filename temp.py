
import random
#def rolldice():
#    return random.choice(range(1,7))
#for i in range(5):
#    print(rolldice())
    
#[print(dices) for dices in [random.choice(range(1,7)) for i in range(5)]]
list=[random.choice(range(1,7)) for i in range(5)]
print(list)
[print(ocurrences) for ocurrences in ]
ocurrences=[]
for i in range(1,7):
    if list.count(i) > 1:
        ocurrences.append(list.count(i))
print(ocurrences)

    



#list= ['papa','casa','mesa','libro','torco','meno' ]
#[print(palabra) for palabra in list if 'o' in palabra]