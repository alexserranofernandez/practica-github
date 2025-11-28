#Inicio variables.
positivos=0
negativos=0
#Asigno el rango de los números a introducir.
for i in range(6):
    numero=int(input("Introduce un número:"))
#Aplico con dición de si es positivo o negativo y hago suma.
    if numero>0:
        positivos=positivos+numero
    if numero<0:
        negativos=negativos+numero
#Muestro resultado por pantalla.
print(f"Suma de números positivos: {positivos}")
print(f"Suma de números negativos: {negativos}")