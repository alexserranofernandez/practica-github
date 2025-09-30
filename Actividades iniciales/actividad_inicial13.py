#Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el 
#área y para calcular el volumen utiliza el operador de exponente. 
var1=float(input("Introduce un lado del cubo"))
total_área=6*(var1**2)
total_volumen=var1**3
print("El área tiene un valor de", total_área,"cm2")
print("El volumen tiene un valor de", total_volumen,"cm3")