#Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor 
#y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro. 
var1=float(input("Introduce el lado del trapecio"))
var2=float(input("Introduce la altura del trapecio"))
var3=float(input("Introduce la base pequeña del trapecio"))
var4=float(input("Introduce la base grande del trapecio"))
total_perimetro=var1*2+var3+var4
total_área=(var3*var4)*var2/2
print("El perimetro del trapecio es:", total_perimetro)
print("El área del trapecio es:", total_área)