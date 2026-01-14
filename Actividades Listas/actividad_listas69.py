#Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor.
cantidad_numeros=int(input("Introduce una cantidad exacta de numeros:"))
milista=[]
for i in range (cantidad_numeros):
    numero=int(input("Introduce un numero:"))
    milista.append(numero)
milista.sort()
print(milista)