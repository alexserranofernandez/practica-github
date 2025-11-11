#Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes:
indice=0
var_vocales="aeiouAEIOUÁÉÍÓÚáéíóú"
var_palabra=input("Introduce una palabra:")
for i in range(len(var_palabra)):
    if var_palabra[indice] in var_vocales:
        vocal_palabra=vocal_palabra+str(var_palabra[indice])
        print(vocal_palabra)
        