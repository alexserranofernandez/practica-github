#Mejora el programa anterior para controlar que el valor introducido es una letra y en 
#caso de introducir un número, aparezca un aviso por pantalla
var1=input("Introduce una letra")
if var1.isupper():
        var2=True
        print(f"¿La letra introducida es mayuscula?{var2}")
else:
    if var1.islower():
        var2=False
        print(f"¿La letra introducida es mayuscula?{var2}")
    else:
        if var1.isnumeric():
            print("La letra introducida es un número")
        else:
             print("La letra introducida es mayuscula ¿?")
        