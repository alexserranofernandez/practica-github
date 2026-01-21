#A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
#eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
print(lista1)
repeat="s"
eliminado=""
while repeat=="s":
    eliminado=input("Introduce el valor que deseas eliminar:")
    if eliminado in lista1:
        if eliminado.isalpha():
            print("Introducir valor númerico")
            repeat=input("¿Deseas introducir otro valor? s/n:")
        elif eliminado.isnumeric():
            lista1.remove(eliminado)
            print(lista1)
            repeat=input("¿Deseas introducir otro valor? s/n:")
    else:
        print("El valor introducido no está en la lista")
        repeat=input("¿Deseas introducir otro valor? s/n:")
        
