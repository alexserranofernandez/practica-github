#A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 
import random
lista=["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]
print(lista)
palabra=random.choice(lista)
letras=list(palabra)
random.shuffle(letras)
palabra_desordenada = "".join(letras)
intentos=3
print(palabra_desordenada)
for i in range(intentos):
    palabra_introducida=input("Introduce la palabra correcta: ")
    if palabra==palabra_introducida:
        print("¡Acertaste!")
        break
    else:
        print(f"No has acertado. Te quedan {intentos-i-1} intentos.")
else:
    print("No has acertado en ninguno de los intentos.")
