#Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
#la palabra
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
import random
palabra=random.choice(lista)
print(lista)
palabra_introducida=input("Introduce una de las palabras de la lista:")
while palabra_introducida!=palabra:
    print("SIGUE JUGANDO")
    palabra_introducida=input("Introduce una de las palabras de la lista:")
    break
else:
    print("ACERTASTE")