listanumeros=[]
listanonumeros=[]
listatodo=[]
frase=input("Introduce valores separados por un guión:")
listatodo=frase.split("-")
for i in range (len(listatodo)):
    if listatodo[i].isnumeric():
        listanumeros.append(listatodo[i])
    else:
        listanonumeros.append(listatodo[i])
print(listanumeros)
print(listanonumeros)