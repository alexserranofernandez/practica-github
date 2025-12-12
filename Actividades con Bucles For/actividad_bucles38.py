#A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10
var_repeticiones=int(input("Introduce el número de notas que quieres introducir:"))
for i in range(var_repeticiones):
    var_nota=float(input("Introduce una nota:"))
    if var_nota>=5 and var_nota<=10:
        print("Asignatura aprobada")
    elif var_nota>=0 and var_nota<=5:
        print("Asignatura suspendida")
    else:
        print("Has introducido una nota equivocada")
