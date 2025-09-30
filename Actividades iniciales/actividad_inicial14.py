#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área 
#y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el 
#resultado a un decimal.
#var1=diametro del circulo
var1=float(input("Introduce el diametro del círculo"))
import math
total_perimetro=math.pi*var1
total_perimetro_redondeado=round(total_perimetro,1)
radio=var1/2
total_área=math.pi*radio**2
total_área_redondeada=round(total_área,1)
print("El perimetro es:", total_perimetro_redondeado)
print("El área es:", total_área_redondeada)