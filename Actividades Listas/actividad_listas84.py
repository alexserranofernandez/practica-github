#A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra. 
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
print(lista)
palabra=random.choice(lista)
palabra_desordenada=random.shuffle(palabra)
intentos=3
palabra_introducida="".join(palabra)
print(palabra_desordenada)
palabra_introducida=input("Introduce la palabra correcta:")
for i in range(intentos):
    if palabra!=palabra_introducida:
        print("No has acertado")
        intentos=intentos-1
        palabra_introducida=input("Introduce la palabra correcta:")
    else:
        print("Acertaste")
        break
print("No has acertado ninguno de los intentos")