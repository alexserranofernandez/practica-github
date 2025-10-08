#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
#índice

var_frase="A quién madruga Dios ayuda"
palabra=input("Introduce una palabra: ")
palabra1="A"
palabra2="quién"
palabra3="madruga"
palabra4="Dios"
palabra5="ayuda"
indice=var_frase.index(palabra)
if palabra == palabra1 or palabra2 or palabra3 or palabra4 or palabra5:
    print(f"La palabra está en la frase y está en el indice {indice}.")
else:
    print(f"La palabra no está en la frase")