#Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.
numero_mayor=0
numero_menor=0
numero=int(input("Introduce un número:"))
while numero!=-99:
    if numero>numero_mayor:
        numero_mayor=numero
    if numero<numero_menor:
        numero_menor=numero
    numero=int(input("Introduce un número:"))
print("RESUMEN")
print(f"El número mayor es {numero_mayor}")
print(f"El número menor es {numero_menor}")