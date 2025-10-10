#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
var1=input("Introduce una letra")
if var1.isupper():
        var2=True
        print(f"¿La letra introducida es mayuscula?{var2}")
else:
    if var1.isnumeric():
        print("La letra es mayuscula ¿?")
    else:
        var2=False 
        print(f"¿La letra introducida es mayuscula?{var2}")
