#var1=diametro del circulo
var1=float(input("Introduce el diametro del círculo"))
import math
total_perimetro=math.pi*var1
radio=var1/2
total_área=math.pi*radio**2
print("El perimetro es:", total_perimetro)
print("El área es:", total_área)