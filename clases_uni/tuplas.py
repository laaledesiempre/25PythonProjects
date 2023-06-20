"""
letras= ("a","b","c","d","e","f")

print(letras)

print(letras[2:])

print(letras[:5])

print(letras[3:6])

print(tuple([x.upper() for x in list(letras)]))

print("Está tu letra" if ("a" in letras) else "No esta tu letra")

print(len(letras))

letras2= ("g","h","i")

letras3= letras+letras2

print(letras3)
print(letras2)
print(letras)
"""
"""
numeros=(7,5,2,3,4,8,6,9,2)

print(f"la lista numeros mide {len(numeros)} y su mayor numero es {max(numeros)} y esta en el indice {numeros.index(max(numeros))}")
"""

def calcular_siguiente(unidad,numero):
    meses_30=("04","06","09","11")
    meses_31=("01","03","05","07","08","10","12")
    result=""
    if unidad=="dia":
        dia=numero[:2]
        mes=numero[3:5]
        año=numero[6:]
        if mes in meses_30:
            if int(dia)>=30:
                if int(mes)>9:
                    result= f"01/{int(mes)+1}/{año}"
                else:
                    result= f"01/0{int(mes)+1}/{año}"
            else:
                if int(dia)>9:
                    result= f"{int(dia)+1}/{mes}/{año}"
                else:
                    result=f"0{int(dia)+1}/{mes}/{año}"
        elif mes in meses_31:
            if int(dia)>30:
                if int(mes)>11:
                    result= f"01/01/{int(año)+1}"
                else:
                    result=f"01/{int(mes)+1}/{año}"
            else:
                if int(dia)>9:
                    result= f"{int(dia)+1}/{mes}/{año}"
                else:
                    result=f"0{int(dia)+1}/{mes}/{año}"
        else:
            if int(dia)>=28:
                result=f"01/03/{año}"
            else:
                result=f"{int(dia)+1}/02/{año}"
    return result 
print(calcular_siguiente("dia","28/02/2019"))
