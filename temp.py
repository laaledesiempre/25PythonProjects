import random
print(sum([p[0] for p in [[20 if list_of_ocurrences ==[5] else 12 if list_of_ocurrences ==[4] else 9 if list_of_ocurrences ==[2,3] or list_of_ocurrences==[3,2] else 6 if list_of_ocurrences==[3] else 5 if list_of_ocurrences==[2,2] else 2 if list_of_ocurrences==[2] else 0] for list_of_ocurrences in [[list.count(i) for i in range(1,7) if list.count(i) > 1] for list in [[random.choice(range(1,7)) for j in range(5)] for h in range(5)]]]]))