#Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de 
#esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
#tenga x oportunidades para ver si letra introducida está en esa palabra.
var_palabra=input("Introduce una palabra:")
var_oportunidades=5
var_longitud=len(var_palabra)
for i in range(var_oportunidades):
    var_letra=input("Introduce una letra:")
    if var_letra in var_palabra:
        print("La letra está en la palabra")
    else: