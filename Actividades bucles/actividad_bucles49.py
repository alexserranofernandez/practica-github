#A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.
palabra=input("Introduce una palabra:")
palabra=palabra.lower()
var_oportunidades=5
for i in range(var_oportunidades):
    for j in range (0,len(palabra)):
        var_letra=input("Introduce una letra:")
        index=palabra.index(var_letra)+1
        if var_letra not in palabra:
            print("La letra no está en la palabra")
        var_oportunidades=var_oportunidades-1
        if var_oportunidades<=0:
            print("Te has quedado sin oportunidades")
        else:   
            print(f"La letra está en la posición {index} en la palabra y te han sobrado {var_oportunidades+1} oportunidades.")
exit()