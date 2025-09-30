#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan 
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por 
#teclado el número de menores y el número de adultos que asisten al cine. 
#Los adultos tienen un 10% de descuento y los menores de 18 años tienen un 50% de descuento
#var1=adultos
#var2=menores
print("Cines Paradiso ofrece descuentos por su décimo aniversario")
var1=int(input("Introduce cuantos adultos van a ir al cine"))
var2=int(input("Introduce cuantos menores van a ir al cine"))
total_precio_adultos=(var1*12*(100-10))/100
total_precio_menores=(var2*12*50)/100
total_precio=total_precio_adultos+total_precio_menores
print("El total que tendrán que pagar será de", total_precio,"euros.")
print("Los adultos", total_precio_adultos, "euros, y los menores", total_precio_menores,"euros.")