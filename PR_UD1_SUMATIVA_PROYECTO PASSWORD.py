var_password=input("Introduce una contraseña de entre 6 y 8 caracteres")
caracteres=len(var_password)
if not len(var_password)>=6 or not len(var_password)<=8:
    print(f"ERROR, la contraseña contiene {caracteres} caracteres, lo cual no es viable.")
else:
    caracter0=(var_password[0])
    if 1<=caracter0<=5:
        print("ERROR en el caracter 1")