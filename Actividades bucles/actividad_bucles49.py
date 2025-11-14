#A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.
var_palabra=input("Introduce una palabra:")
var_palabra=var_palabra.lower
var_oportunidades=5
var_longitud=len(var_palabra)
for i in range(var_oportunidades):
    var_letra=input("Introduce una letra:")
    if var_letra not in var_palabra:
        print("La letra no está en la palabra")
        var_oportunidades=var_oportunidades-1
    if var_oportunidades<=0:
        print("Te has quedado sin oportunidades")
        
    else:   
        print(f"La letra está en la posición  en la palabra")
        exit()