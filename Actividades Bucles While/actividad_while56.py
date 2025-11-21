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
numero_pedidos=int(input("Introduce el número de pedidos que quieres:"))
numero=0
menu=0
acompanyamiento=0
bebidas=0
total_precio=0
descuento=0
while numero_pedidos>=numero:
    menu=int(input("Introduce el número del plato principal:"))
    acompanyamiento=int(input("Introduce el número del acompañamiento:"))
    bebidas=int(input("Introduce el número de la bebida:"))
    print("")
    print("SIGUIENTE PEDIDO:")
    numero=numero+1
    if menu==1:
        total_precio=float(total_precio+9)
    elif menu==2:
        total_precio=float(total_precio+4.5)
    elif menu==3:
        total_precio=float(total_precio+2.5)
    if acompanyamiento==1:
        total_precio=float(total_precio+1.5)
    elif acompanyamiento==2:
        total_precio=float(total_precio+1.75)
    elif acompanyamiento==3:
        total_precio=float(total_precio+2)
    if bebidas==1:
        total_precio=float(total_precio+2)
    elif bebidas==2:
        total_precio=float(total_precio+1.5)
    elif bebidas==3:
        total_precio=float(total_precio+1)

iva=total_precio*10/100
total_iva=total_precio-iva
if total_iva<30 and total_iva>20:
    descuento=total_iva*5/100
    precio_descuento=total_iva-descuento
    print("RESUMEN")
    print(f"Número de pedidos:{numero_pedidos}")
    print(f"Total a pagar:{total_precio}")
    print(f"Total con iva:{total_iva}")
    print(f"Precio total con descuento del 5%:{precio_descuento}")
elif total_iva>30:
    descuento=total_iva*15/100
    precio_descuento=total_iva-descuento
    print("RESUMEN")
    print(f"Número de pedidos:{numero_pedidos}")
    print(f"Total a pagar:{total_precio}")
    print(f"Total con iva:{total_iva}")
    print(f"Precio total con descuento del 15%:{precio_descuento}")