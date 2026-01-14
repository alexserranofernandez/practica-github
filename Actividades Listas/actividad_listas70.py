#Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
#formato de entrada y salida tal y como se muestra en el testeo.
lista1=[]
lista2=[]
cantidad_palabras=int(input("Introduce un numero de palabras:"))
for i in range (cantidad_palabras):
    palabra=input("Introduce una palabra:")
    lista2.append(palabra)
lista2.sort()
lista1=lista2.copy()
lista1.reverse()
print(f"Lista1 contiene {lista2}")
print(f"Lista2 contiene {lista1}")