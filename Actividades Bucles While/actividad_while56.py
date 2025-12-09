#Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.
print("MENÚ")
print("1. Bocadillo de calamares - 9€")
print("2. Bocadillo de chistorra - 4.5€")
print("3. Bikini de jamón - 2.5€")
print("")
print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5€")
print("2. Patatas gruesas - 1.75")
print("3. Patatas rústicas - 2€")
print("")
print("BEBIDAS")
print("1. Coca cola - 2€")
print("2. Acuarius - 1.5€")
print("3. Agua - 1€")
precio_normal=0
precio_descuento5=0
precio_descuento15=0
precio_iva=0
porcentaje_iva=0
pedidos=0
porcentaje_descuento5=0
porcentaje_descuento15=0
repeat="s"
while repeat=="s":
    menu=int(input("Introduce el menú (1,2,3):"))
    acompañamiento=int(input("Introduce el acompañamiento (1,2,3):"))
    bebida=int(input("Introduce la bebida (1,2,3):"))
    if menu==1:
        precio_normal=precio_normal+9
    if menu==2:
        precio_normal=precio_normal+4.5
    if menu==3:
        precio_normal=precio_normal+2.5
    if acompañamiento==1:
        precio_normal=precio_normal+1.5
    if acompañamiento==2:
        precio_normal=precio_normal+1.75
    if acompañamiento==3:
        precio_normal=precio_normal+2
    if bebida==1:
        precio_normal=precio_normal+2
    if bebida==2:
        precio_normal=precio_normal+1.5
    if bebida==3:
        precio_normal=precio_normal+1
    pedidos=pedidos+1
    repeat=input("¿Quieres otro pedido más?(s/n)")
porcentaje_iva=precio_normal*10/100
precio_iva=precio_normal+porcentaje_iva
if precio_iva<=30 and precio_iva>=20:
    porcentaje_descuento5=precio_iva*5/100
    precio_descuento5=precio_iva-porcentaje_descuento5
    precio_descuento5=round(precio_descuento5,1)
    print("RESUMEN")
    print(f"Número de pedidos:{pedidos}")
    print(f"Total a pagar:{precio_normal}")
    print(f"Total con iva:{precio_iva}")
    print(f"Precio total con descuento del 5%:{precio_descuento5}")  
if precio_iva>30:
    porcentaje_descuento15=precio_iva*15/100
    precio_descuento15=precio_iva-precio_descuento15
    precio_descuento15=round(precio_descuento15,2)
    print("RESUMEN")
    print(f"Número de pedidos:{pedidos}")
    print(f"Total a pagar:{precio_normal}")
    print(f"Total con iva:{precio_iva}")
    print(f"Precio total con descuento del 15%:{precio_descuento15}")  
        
