repeat="s"
numero=0
lista=[]
while repeat=="s":
    numero=input("Introduce un número:")
    lista=list(numero)
    for i in lista:
        if not i.isnumeric() and i!=".":
            print("Entrada no válida")
            break
    else:
        if "." in lista:
            print("Es decimal")
        else:
            print("No es decimal")
    repeat=input("¿Desea continuar? s/n:")