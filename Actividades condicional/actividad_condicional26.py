#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
var1=input("Introduce una letra")
if len(var1) == 1 and var1.isalpha:
    if var1.isupper():
        print("La letra introducida es mayuscula")
    elif var1.islower():
        print("La letra introducida es minuscula")
    elif var1.isnumeric():
        print("La letra es mayuscula ¿?")
