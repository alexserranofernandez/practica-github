#Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos
pares=0
impares=0
positivos=0
negativos=0
ceros=0
suma=0
numero=0
numero=int(input("Introduce un número:"))
while numero!=-99:
    if numero%2==0:
        pares=pares+1
    if numero%2!=0:
        impares=impares+1
    if numero>0:
        positivos=positivos+1
    if numero<0:
        negativos=negativos+1
    if numero==0:
        ceros=ceros+1
    suma=suma+numero
    if numero==-99:
        suma=suma+99
    numero=int(input("Introduce un número:"))
print("RESUMEN")
print(f"El número de números pares es {pares}")
print(f"El número de números impares es {impares}")
print(f"El número de números positivos es {positivos}")
print(f"El número de números negativos es {negativos}")
print(f"El número de ceros es {ceros}")
print(f"La suma de todos los números es {suma}")