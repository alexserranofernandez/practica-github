#Corrige los 4 errores o añade el código que necesites para que el siguiente programa se 
#ejecute correctamente
#inicializo valores a cada variable
var_numero=0
var_suma=0
var_numero=(input("Introduce un número"))
#obtengo su longitud
var_longitud=len(var_numero)
#sumo cada digito a partir del índice de cada posición
var_suma=var_longitud.index(1)+var_longitud.index(2)+var_longitud.index(3)+var_longitud.index(4)
#utilizo una condición y el operador aritmético // para saber si el resto da 0 y ver si es par
if var_suma // 2 == 0:
   print (f"el valor de {var_suma} es par")
else:
   print(f"El valor de {var_suma} es impar")
