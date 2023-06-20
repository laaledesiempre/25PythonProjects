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
