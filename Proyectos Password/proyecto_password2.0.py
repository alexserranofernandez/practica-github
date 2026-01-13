#mostramos condiciones por pantalla
print("INSTRUCCIONES")
print("")
print("1. Debe tener una longitud entre 6 y 8 caracteres")
print("2. CARACTERISTICAS:")
print("")
print("     2.1 Un número menor o igual que 6")
print("     2.2 Un número mayor o igual que 1 y menor o igual que 5")
print("     2.3 Un número mayor o igual que 7 y menor o igual que 9")
print("     2.4 Dos letras mayúsculas")
print("     2.5 Una letra minúscula")
print("     2.6 Un símbolo (@, %, /, #)")

intentos = 3
simbolos = "@%/#"

for intento in range(intentos):
    password = input("Introduce una palabra clave: ")

    # Validación de longitud
    if not (6 <= len(password) <= 8):
        print(f"ERROR, la contraseña contiene {len(password)} caracteres, lo cual no es viable.")
        print("PASSWORD INCORRECTA")
        print(f"Te quedan {intentos - intento - 1}")
        continue

    # Contadores por intento (reiniciar cada vez)
    letra_mayuscula = 0
    letra_minuscula = 0
    numero_menor_6 = 0
    numero_entre_1y5 = 0
    numero_entre_7y9 = 0
    cantidad_simbolos = 0
    condicion1=numero_menor_6>=1
    condicion2=numero_entre_1y5>=1
    condicion3=numero_entre_7y9>=1
    condicion4=letra_mayuscula>=2
    condicion5=letra_minuscula>=2
    condicion6=cantidad_simbolos>=1
    # Analizamos cada carácter de la contraseña
    for i in password:
        if i in "0123456789":
            num = int(i)
            if num <= 6:
                numero_menor_6 += 1
            if 1 <= num <= 5:
                numero_entre_1y5 += 1
            if 7 <= num <= 9:
                numero_entre_7y9 += 1
        elif i.isalpha():
            if i.isupper():
                letra_mayuscula += 1
            else:
                letra_minuscula += 1
        elif i in simbolos:
            cantidad_simbolos += 1

    # Comprobamos todas las condiciones
    if condicion1 and condicion2 and condicion3 and condicion4 and condicion5 and condicion6:
        print("PASSWORD CORRECTA")
        print(f"Te han sobrado {intentos - intento - 1} intentos")
        break
    else:
        print("PASSWORD INCORRECTA")
        if not condicion1:
            print("Debe contener al menos un número igual a 6")
        if not condicion2:
            print("Debe contener un número entre 1 y 5")
        if not condicion3:
            print("Debe contener un número entre 7 y 9")
        if not condicion4:
            print("Debe contener al menos dos letras mayúsculas")
        if not condicion5:
            print("Debe contener al menos una letra minúscula")
        if not condicion6:
            print("Debe contener al menos un símbolo (@, %, /, #)")
        print(f"Te quedan {intentos - intento - 1} intentos")  
else:
    print("Te has quedado sin intentos")
    if not condicion1:
        print("Debe contener al menos un número igual a 6")
    if not condicion2:
        print("Debe contener un número entre 1 y 5")
    if not condicion3:
        print("Debe contener un número entre 7 y 9")
    if not condicion4:
        print("Debe contener al menos dos letras mayúsculas")
    if not condicion5:
        print("Debe contener al menos una letra minúscula")
    if not condicion6:
        print("Debe contener al menos un símbolo (@, %, /, #)")
# Testeos:

# 1: 348MiU% Password Correcta
# 2: 43HHu%2 Password Incorrecta
# 3: 8/2Ou1l Password Incorrecta
# 4: #196o@LP Password Correcta
# 5: 1%Uk86L Password Correcta
# 6: Ulo#196 Password Incorrecta
# 7: %14Ew9M Password Correcta
# 8: 6Y@lm19ML Password Incorrecta - 9 carácteres, demasiado larga.
# 9: 23Iu/ Password Incorrecta - 5 carácteres. demasiado corta.
# 10: 8UkL#14 Password Correcta