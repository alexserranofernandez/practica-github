#Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
#repiten y cuales no
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
repetidas=[]
norepetidas=[]
for palabras in lista1:
    if palabras in lista2:
        repetidas.append(palabras)
    else:
        norepetidas.append(palabras)
for palabras in lista2:
    if not palabras in lista1:
        norepetidas.append(palabras)
print(f"Están repetidas:{repetidas}")
print(f"No están repetidas:{norepetidas}")