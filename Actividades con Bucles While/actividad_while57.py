#Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
numero=random.randint(1, 5)
numero_introducido=0
while numero!=numero_introducido:
    numero_introducido=int(input("Introduce un número:"))
    if not 1<=numero_introducido<=5:
        print("Número erroneo")
        break
    if not numero==numero_introducido:
        print("Número no acertado")
else:
    print("Número acertado")