#A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 
import random
lista = ["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]
print(lista)
# Seleccionamos una palabra al azar de la lista
palabra = random.choice(lista)
# Convertimos la palabra en lista de letras para poder desordenarla
letras = list(palabra)
# Desordenamos las letras (shuffle modifica la lista directamente)
random.shuffle(letras)
# Unimos las letras desordenadas en un string
palabra_desordenada = "".join(letras)
# Definimos el número de intentos que tiene el usuario
intentos = 3
# Mostramos la palabra desordenada al usuario
print(palabra_desordenada)
# Bucle que se repite mientras queden intentos
for i in range(intentos):
    # Pedimos al usuario que introduzca su respuesta
    palabra_introducida = input("Introduce la palabra correcta: ")
    # Comprobamos si la palabra introducida es correcta
    if palabra == palabra_introducida:
        print("¡Acertaste!")
        break  # Salimos del bucle si acierta
    else:
        # Mostramos mensaje de fallo y los intentos restantes
        print(f"No has acertado. Te quedan {intentos - i - 1} intentos.")
else:
    # Este bloque se ejecuta solo si NO se usó break (es decir, no acertó)
    print("No has acertado en ninguno de los intentos.")
