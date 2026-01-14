#Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.
milista=[]
sinduplicados=[]
decision="s"
while decision!="n":
    letra=input("Introduce una letra:")
    if letra.isnumeric():
        letra=input("Introduce una letra:")
    else:
        milista.append(letra)
        decision=input("¿Deseas repetir? s/n:")
sinduplicados=list(set(milista))
print(sinduplicados)
