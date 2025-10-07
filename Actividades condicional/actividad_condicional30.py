#Realiza un programa que controle si la longitud de una frase introducida por teclado es
#igual, menor o mayor de 11 caracteres. Utiliza elif
var1=input("Introduce una frase: ")
if len(var1)<11:
    print(f"La longitud de la frase es de {len(var1)} caracteres y es menor a 11 caracteres.")
elif len(var1)==11:
    print(f"La longitud de la frase es igual a {len(var1)} caracteres.")
elif len(var1)>11:
    print(f"La longitud de la frase es de {len(var1)} caracteres y es mayor a 11 caracteres.")
    