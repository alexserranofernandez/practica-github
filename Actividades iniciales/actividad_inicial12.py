var1=float(input("Introduce el lado del trapecio"))
var2=float(input("Introduce la altura del trapecio"))
var3=float(input("Introduce la base pequeña del trapecio"))
var4=float(input("Introduce la base grande del trapecio"))
total_perimetro=var1*2+var3+var4
total_área=(var3*var4)*var2/2
print("El perimetro del trapecio es:", total_perimetro)
print("El área del trapecio es:", total_área)