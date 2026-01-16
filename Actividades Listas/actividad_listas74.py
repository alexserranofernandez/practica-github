#A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de 
#entre las 2 listas.
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