#Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.
intentos=0
import random
numero=random.randint(0, 1000)
numero_introducido=0
while numero!=numero_introducido:
    numero_introducido=int(input("Introduce un número:"))
    if numero<numero_introducido:
        print("El número es menor")
        intentos=intentos+1
    if numero>numero_introducido:
        print("El número es mayor")
        intentos=intentos+1
else:
    print(f"¡Acertaste! El número correcto era {numero} y has necesitado {intentos} intentos")