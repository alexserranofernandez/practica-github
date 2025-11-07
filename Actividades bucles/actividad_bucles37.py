#Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
#o suspendido.
var_repeticiones=int(input("Introduce el número de notas que quieres introducir:"))
for i in range(var_repeticiones):
    var_nota=float(input("Introduce una nota:"))
    if var_nota>=5:
        print("Asignatura aprobada")
    else:
        print("Asignatura suspendida")
