#Programa un código que permita contar el número de vocales de la siguiente frase: No 
#hay mal que dure cien años

var_frase="No hay mal que dure cien años"
var_frase=var_frase.lower()
vocales=["a","e","i","o","u"]
contador_vocales=0
for letra in var_frase:
    if letra in vocales:
        contador_vocales=contador_vocales+1
print(f"El número de vocales que encontramos en la frase {var_frase} es de {contador_vocales}")
