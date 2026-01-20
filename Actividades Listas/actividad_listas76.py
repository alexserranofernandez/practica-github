#A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
#y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
#en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
lista_ascendente_letras=[]
lista_ascendente_numeros=[]
lista_descendente_letras=[]
lista_descendente_numeros=[]
numeros=""
letras=""
orden=int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente:"))
for i in lista1:
    if i.isnumeric():
        numeros=numeros+str(i)
    if i.isalpha():
        numeros=numeros+str(i)
lista_ascendente_numeros=sorted(numeros)
lista_ascendente_letras=sorted(letras)
print(lista_ascendente_numeros)
print(lista_ascendente_letras)