var_password=input("Introduce una contraseña de entre 6 y 8 caracteres")
caracteres=len(var_password)
if not len(var_password)>"6" and len(var_password)<"8":
    print(f"Error, la contraseña contiene {caracteres} caracteres, lo cual no es viable.")