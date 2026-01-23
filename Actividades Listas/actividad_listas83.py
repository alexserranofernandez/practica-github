#Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
#que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente 
#manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así 
#sucesivamente.
#Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. 
#Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la 
#suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe 
#algún método que permita sumar el contenido de una lista?
import random
repeat_partidas="s"
intentos=8
puntos=[]
while repeat_partidas!="n":
    lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
    palabra=random.choice(lista)
    intentos=8
    print(lista)
    palabra_introducida=input("Introduce una de las palabras de la lista:")
    while not palabra_introducida==palabra:
        print("SIGUE JUGANDO")
        palabra_introducida=input("Introduce una de las palabras de la lista:")
        intentos=intentos-1
    else:
        print("ACERTASTE")
        puntos.append(intentos)
    repeat_partidas=input("¿Deseas seguir jugando?s/n:")
else:
    print(f"Puntuación: {puntos}")
    print(f"Tu puntuación ha sido de {sum(puntos)}")
media=(len(puntos)*8)/2
print(f"La media de las partidas realizadas es: {media}")
if sum(puntos)>media:
    print("Tienes buena suerte")
else:
    print("Mejor dedicate a jugar al FIFA")
