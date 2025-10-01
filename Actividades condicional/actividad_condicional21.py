#Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz 
#cuadrada no de un valor negativo
import math
var1=int(input("Introduce el valor a de la ecuación"))
var2=int(input("Introduce el valor b de la ecuación"))
var3=int(input("Introduce el valor c de la ecuación"))
número_para_raiz_cuadrada=var2**2-4*var1*var3
if número_para_raiz_cuadrada<0:
    print("La raíz no puede ser un valor negativo")
else:
    total_ecuación_positivo=(-var2 + math.sqrt(número_para_raiz_cuadrada))/2*var1
    total_ecuación_negativo=(-var2 - math.sqrt(número_para_raiz_cuadrada))/2*var1
    print("El valor de x1 es:", total_ecuación_positivo)
    print("El valor de x2 es:", total_ecuación_negativo)