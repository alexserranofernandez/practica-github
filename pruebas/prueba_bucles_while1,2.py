intentos=3
import random
numero_secreto=random.randint(1,20)
numero_introducido=int(input("Introduce un número del 1 al 20:"))
if intentos<=0:
    print(f"Te has quedado sin intentos, el número secreto era {numero_secreto}")
while intentos!=0:
    while numero_introducido<numero_secreto:
        print("Es más alto")
        intentos=intentos-1
        print(f"Te quedan {intentos} intentos")
        numero_introducido=int(input("Introduce otro número:"))
    while numero_introducido>numero_secreto:
        print("Es más bajo")
        intentos=intentos-1
        print(f"Te quedan {intentos} intentos")
        numero_introducido=int(input("Introduce otro número:"))
        print(f"Acertaste, te han sobrado {intentos-1} intentos")
        break

