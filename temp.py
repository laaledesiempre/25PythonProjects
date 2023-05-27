
import random
#def rolldice():
#    return random.choice(range(1,7))
#for i in range(5):
#    print(rolldice())
    
#[print(dices) for dices in [random.choice(range(1,7)) for i in range(5)]]
#list=[random.choice(range(1,7)) for i in range(5)]
#print(list)


print(sum([p[0] for p in [[20 if list_of_ocurrences ==[5] else 12 if list_of_ocurrences ==[4] else 9 if list_of_ocurrences ==[2,3] or list_of_ocurrences==[3,2] else 6 if list_of_ocurrences==[3] else 5 if list_of_ocurrences==[2,2] else 2 if list_of_ocurrences==[2] else 0] for list_of_ocurrences in [[list.count(i) for i in range(1,7) if list.count(i) > 1] for list in [[random.choice(range(1,7)) for j in range(5)] for h in range(5)]]]]))






"""   La puntuación es:
     - 5 dados iguales                  : 20 pts.
     - 4 dados iguales                  : 12 pts.
     - 3 dados iguales y otros 2 iguales:  9 pts.
     - 3 dados iguales                  :  6 pts.
     - 2 dados iguales y otros 2 iguales:  5 pts.
     - 2 dados iguales                  :  2 pts.
"""

#(list.count(i) for i in range(1,7) if list.count(i) > 1)

#ocurrences=[]
#for i in range(1,7):
#    if list.count(i) > 1:
#        ocurrences.append(list.count(i))
#print(ocurrences)

    



#list= ['papa','casa','mesa','libro','torco','meno' ]
#[print(palabra) for palabra in list if 'o' in palabra]