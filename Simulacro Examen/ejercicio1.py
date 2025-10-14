nombre=input("Introduce tu nombre.")
edad=int(input("Introduce tu edad."))
nombre_mayusculas=nombre.upper()
if edad>0 and edad<100:
    año_actual=2025
    futuro=año_actual+(100-edad)
    print("Hola",nombre_mayusculas,"cumplirá 100 años en el año",futuro)
else:
    print("Edad no válida")
    