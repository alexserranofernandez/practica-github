#Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While
var_numero1=int(input("Introduce un número:"))
var_numero2=int(input("Introduce otro número:"))
var_suma=var_numero1+var_numero2
print(f"El resultado de la suma es {var_suma}")
repetición=input("Desea repetir la operación s/n")
while repetición!="n":
    var_numero1=int(input("Introduce un número:"))
    var_numero2=int(input("Introduce otro número:"))
    var_suma=var_numero1+var_numero2
    print(f"El resultado de la suma es {var_suma}")
    repetición=input("Desea repetir la operación s/n")
else:
    print("Fin del programa")
    