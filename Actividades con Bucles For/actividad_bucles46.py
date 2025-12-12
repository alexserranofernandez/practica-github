#A partir del programa anterior, soluciona el error que se produce en el test anterior con la 
#palabra Abrigo utilizando únicamente una instrucción.
vocal_palabra=""
var_vocales="aeiouáéíóú"
consonante_palabra=""
var_palabra=input("Introduce una palabra:")
var_palabra=var_palabra.lower()
for i in range(len(var_palabra)):
    if var_palabra[i] in var_vocales:
        vocal_palabra=str(vocal_palabra)+str(var_palabra[i])
    else:
        consonante_palabra=str(consonante_palabra)+str(var_palabra[i])
print(f"Las vocales de la palabra {var_palabra} son: {vocal_palabra}")
print(f"La consonantes de la palabra {var_palabra} son: {consonante_palabra}")