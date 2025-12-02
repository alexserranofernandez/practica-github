#Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while
numero=int(input("Introduce un número:"))
multiplicacion=1
while multiplicacion<=10:
    producto_num=multiplicacion*numero
    multiplicacion=multiplicacion+1
    print(producto_num)