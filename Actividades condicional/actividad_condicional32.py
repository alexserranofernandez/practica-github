#Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas
var_frase="A quién madruga Dios ayuda"
palabra=input("Introduce una palabra: ")
palabra1="A"
palabra2="quién"
palabra3="madruga"
palabra4="Dios"
palabra5="ayuda"
indice=var_frase.lower().index(palabra.lower())
if palabra == palabra1 or palabra2 or palabra3 or palabra4 or palabra5:
    print(f"La palabra está en la frase y está en el indice {indice}.")
else:
    print(f"La palabra no está en la frase")