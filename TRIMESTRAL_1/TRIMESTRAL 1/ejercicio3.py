#Inicio variable.
suma=0
#Pido al usuario qu introduzca variable.
cifras=int(input("Introduce el número de cifras:"))
numero=int(input("Introduce un número que respete las cifras introducidas:"))
#Mido longitud del número y lo convierto en un str.
longitud=len(str(numero))
#Aplico condición de que las cifras sean iguales a la longitud del número.
if cifras!=longitud:
    print("Error, no coincide el número de cifras")
else:
#Hago la suma con for i la variable i.
    for i in str(numero):
        suma=suma+int(i)
#Muestro resultado.
    print(f"Resultado: {suma}")