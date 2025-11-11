#Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima 
#por pantalla cada letra
var_palabra=input("Introduce una palabra:")
for i in range(len(var_palabra)):
    print(f"En la posición {i} está la {var_palabra[i]}")