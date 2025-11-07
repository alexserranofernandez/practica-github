#Programa que sume los n primeros números naturales. n Lo introduce el usuario.
var_n=int(input("Introduce un número natural:"))
var_suma=0
for i in range(1,1+var_n):
    var_suma=var_suma+i
print(f"La suma de los números naturales es de {var_suma}")