password=input("Introduce una contraseña de entre 6 y 8 caracteres")
errores=0
caracteres=len(password)
if not len(password)>=6 or not len(password)<=8:
    print(f"ERROR, la contraseña contiene {caracteres} caracteres, lo cual no es viable.")
else:
    caracter1=(password[0])
    if caracter1.isnumeric():
        if 1<=int(caracter1) and 5>=int(caracter1):
            print("Carácter 1 correcto")
        else:
            print("ERROR en el caracter 1")
            errores=errores+1
    else:
        print("ERROR en el caracter 1")
        errores=errores+1
    caracter2=(password[1])
    if caracter2.isalpha():
        if caracter2.islower():
            print("Carácter 2 correcto")
        else:
            print("ERROR en el caracter 2")
            errores=errores+1
    else:
        print("ERROR en el caracter 2")
        errores=errores+1
    caracter3=(password[2])
    if caracter3.isalpha():
        if caracter3.isupper():
            print("Caracter 3 correcto")
            errores=errores+1
        else:
            print("ERROR en el caracter 3")
            errores=errores+1
    else:
        print("ERROR en el caracter 3")
    caracter4=(password[3])
    if caracter4=="*" or caracter4=="_" or caracter4=="@":
        print("Caracter 4 correcto")
    else:
        print("ERROR en el caracter 4")
        errores=errores+1
    caracter5=(password[4])
    if caracter5.isalpha():
        if caracter5.islower():
            print("Carácter 5 correcto")
        else:
            print("ERROR en el caracter 5")
            errores=errores+1
    else:
        print("ERROR en el caracter 5")
        errores=errores+1
    caracter6=(password[5])
    if caracter6.isnumeric:
        if 6<=caracter6 and 9>=caracter6:
            print("Caracter 6 correcto")
        else:
            print("ERROR en el caracter 6")
    else:
        print("ERROR en el caracter 6")
