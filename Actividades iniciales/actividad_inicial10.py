var1=int(input("Introduce un número"))
var2=int(input("Introduce otro número"))
total_cociente=var1/var2
total_resto=var1%var2
print("El cociente es:", total_cociente)
print("El resto es:", total_resto)
if var1 % 2 == 0:
 print("El número es par")
else:
 print("El número es impar")