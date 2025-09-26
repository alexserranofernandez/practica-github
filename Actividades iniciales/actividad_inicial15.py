#Conseguir área y volumen
#var1=radio
#var2=altura
var1=float(input("Introduce el radio del cilindro"))
var2=float(input("Introduce la altura del cilindro"))
import math
diametro=var1*2
total_área=2*math.pi*var1*(var1+var2)
total_área_redondeada=round(total_área,2)
total_volumen=math.pi*var1**2*var2
total_volumen_redondeado=round(total_volumen,2)
print("El área del cilindro es:", total_área_redondeada)
print("El volumen del cilindro es:", total_volumen_redondeado)