#Modifica el programa anterior para que tengas 3 intentos. Utiliza while
intentos=3
import random
numero=random.randint(1, 5)
numero_introducido=0
while numero!=numero_introducido:
    numero_introducido=int(input("Introduce un número:"))
    if not 1<=numero_introducido<=5:
        print("Número erroneo")
        break
    if not numero==numero_introducido:
        intentos=intentos-1
        print(f"Número no acertado, vuelve ha intentarlo, te quedan {intentos} intentos")
    if intentos<=0:
        print("No te quedan intentos")
        break
else:
    print("Número acertado")