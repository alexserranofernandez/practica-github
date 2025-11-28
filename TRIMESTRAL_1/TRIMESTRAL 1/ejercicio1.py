concatenar=""
#Pido al usuario que introduzca variables e intervalo.
var_min=int(input("Introduce el número mínimo:"))
var_max=int(input("Introduce el número máximo:"))
var_intervalo=int(input("Introduce el intervalo:"))
#Asigno el rango en que se tiene que usar para mostrar el intervalo y su máximo y mínimo.
for i in range(var_min,var_max+1,var_intervalo):
#Hago la serie.
    concatenar=concatenar+str(i)+","
#Uso este formato para eliminar la última coma y muestro por pantalla.
concatenar=concatenar[:-1]
print(concatenar)