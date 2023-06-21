'''
s= {
    'fruta':'Peras',
    'cantidad':10,
    'precio':35.10
    }

print(s["cantidad"])

print(s["precio"])

s['precio']= 75

s['fecha']= "12/10/21"

for x in s.keys():
    print(x)

for x in s.items():
    print(x)

for x in s.values():
    print(x)

s= list(s)

print(s)

s.pop()

print(s)
'''
'''
dicc={
    'clave1':2,
    'clave2':True,
    'clave3':"Wewewe",
    'clave4':[1,2,3,4]
    }

print(type(dicc))

print(dicc["clave1"])
print(dicc["clave2"])
print(dicc["clave3"])
print(dicc["clave4"])

print(type(dicc["clave1"]))
print(type(dicc["clave2"]))
print(type(dicc["clave3"]))
print(type(dicc["clave4"]))

dicc["clave5"]=(1,2,3,4)

#comprobar=input("Ponga una clave: ")
#if comprobar in dicc:
#    print(dicc[comprobar])

dicc2=dicc

dicc2["clave1"]=0
print(dicc["clave1"])

for x in dicc.keys():
    dicc[x]=0

for x in dicc.items():
    print(x)
val_a_borrar=int(input("dato a borrar: "))
prueba=dicc.keys()
while val_a_borrar in dicc.values():
    for x in prueba:
        if dicc[x]==val_a_borrar:
            del dicc[x]
            break
print("valores")
for x in dicc.values():
    print(x)
'''
'''
notas={
    }
z=int(input("cantidad de elementos: "))
for x in range(z):
    notas[f"elemento{x+1}"]=x

for x in notas.items():
    print(x)

notS2=notas
print(id(notas))
print(id(notS2))
notas=None
print(id(notas))
print("valores")
for x in notS2.items():
    print(x)
'''
'''
notas= {
    'Pepito':(9,6,4),
    'Tamal':(9,10,11),
    'Josefa':(2,6,9)
    }
for x in notas.items():
    for y in x[1]:
        if y not in range(1,11):
            print(f"Error, nota erronea en {x}. nota fuera de rango")

for x in notas.items():
    print(f"{x[0]}: {max(x[1])}")

for x in notas.items():
    print(f"{x[0]}: {sum(x[1])/len(x[1])}")
'''
'''
lista1= input("Ingrese numeros, separados por coma: ").split(",")
lista2= input("Ingrese mas numeros, separados por coma: ").split(",")
object={
        'UNO':[],
        'DOS':[]
        }
for x in lista1:
    try:
        object['UNO'].append(int(x))
    except:
        print(f"Valor {x} invalido como numero entero, se ignorara")
for x in lista2:
    try:
        object['DOS'].append(int(x))
    except:
        print(f"Valor {x} invalido como numero entero, se ignorara")
for x in object.items():
    print(f"{x[0]}: {x[1]}")
'''
data={
        
    }
print("Bienvenido a la base de datos de los alumnos")
if len(data)==0:
    print("La base de datos se encuentra vacia.")
 
while True:
    print('''
          Elija una de las siguientes opciones escribiendo el simbolo indicado a la izquierda del parentesis:

          1) Cargar alumno y notas.
          2) Mostrar nombres y promedio.
          S) Salir
          ''')
    opcion= input('Seleccione una opcion: ')
    print()
    if opcion=="1":
        print("Ingrese el nombre del alumno")
        while True:
            added=False
            alumn=input("Nombre del alumno: ")
            if alumn in data.keys():
                print("Nombre presente en nuestra base de datos, porfavor utilice otro")
                continue
            else:
                print("Ingrese las notas del alumno separadas por coma (del 1 al 10)")
                while True:
                    notas=input("Notas del alumno: ").split(",")
                    notas_convertidas=[]
                    for x in notas:
                        try:
                            if 0 <= int(x) <10:
                                notas_convertidas.append(int(x))
                            else:
                                print("notas invalidas, porfavor reintentar")
                                notas_convertidas.clear()
                                break
                        except:
                            print("notas invalidas, porfavor reintentar")
                            notas_convertidas.clear()
                            break
                    if len(notas_convertidas)>0:
                        data[alumn]=notas_convertidas
                        added=True
                        break
            if added:
                break
            else:
                continue

                    
    elif opcion=="2":
        if len(data)==0:
            print("Base de datos vacia, no es posible ver la lista de promedios")
        else:
            print("Lista de promedios:")
            for x in data.items():
                print(f"{x[0]}: {sum(x[1])/len(x[1])}")
    elif opcion.upper()=="S":
            break
    else:
        print("Opcion invalida:")
        continue

