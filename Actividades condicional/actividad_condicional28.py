#Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza 
#elif.
var1=input("Introduce una letra")
if len(var1) == 1 and var1.isalpha:
    if var1.isupper():
        print("La letra introducida es mayuscula")
    elif var1.islower():
        print("La letra introducida es minuscula")
    elif var1.isnumeric():
        print("La letra introducida es un número")
if not var1.isalpha() and not var1.isnumeric():
    print("La letra inroducida es un simbolo")