#Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
num1=int(input("Introduce un número:"))
num2=int(input("Introduce otro número:"))
concatenar_par=""
concatenar_impar=""
if num1>num2:
    for i in range(num2,num1+1):
        if i%2==0:
            concatenar_par=concatenar_par+str(i)+"-"
        elif i%2!=0:
            concatenar_impar=concatenar_impar+str(i)+"-"
    concatenar_par=concatenar_par[:-1]
    concatenar_impar=concatenar_impar[:-1]
    print(concatenar_par)
    print(concatenar_impar)
else:
    print("Valores no ordenados")