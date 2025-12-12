#A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
#superior o igual a 40.
numero=int(input("Introduce un número:"))
multiplicacion=1
while multiplicacion<=10:
    producto_num=multiplicacion*numero
    multiplicacion=multiplicacion+1
    print(producto_num)
    if producto_num>=40:
        print("Fin del programa")
        break