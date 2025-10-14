print("Programa que calcula ep volumen de un cilindro")
radio=float(input("Introduce el radio"))
altura=float(input("Introduce la altura"))
formato=input("Quieres el resultado en mayusculas M o minusculas m")
import math
volumen= round(math.pi*radio**2*altura,3)
if formato=="M":
    print(f"EL VOLUMEN DEL CILINDRO ES DE {volumen} CM3")
elif formato=="m":
    print(f"el volumen del cilindro es de {volumen} cm3")
else:
    print("error")