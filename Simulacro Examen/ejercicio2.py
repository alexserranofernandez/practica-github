var_frase=input("Introduce una frase:")
número1=float(input("Introduce un número:"))
número2=float(input("Introduce un segundo número:"))
número3=float(input("Introduce un tercero número:"))
frase_minusculas=var_frase.lower()
var_suma=número1+número2+número3
var_media=round(var_suma/3,2)
var_producto=número1*número2*número3
print(f"La suma es {var_suma}, la media es {var_media} y el producto es{var_producto}")