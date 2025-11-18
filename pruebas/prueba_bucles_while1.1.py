edad=int(input("Introduce la edad:"))
while edad>120 or edad<0:
    print("Edad incorrecta")
    edad=int(input("Vuelve a introdcuir la edad:"))
print("Edad correcta")