#Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El 
#resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
#resultado entero. Haz que se muestre por pantalla los dos  resultados de todo el proceso 
#sqrt=raiz cuadrada
var1=int(input("Introduce un número"))
import math
total_raiz_cuadradra=math.sqrt(var1)
total_división=total_raiz_cuadradra//2
total_raiz_cuadradra_redondeada=round(total_raiz_cuadradra,1)
print("La raiz cuadrada es:", total_raiz_cuadradra_redondeada)
print("La división de la raiz cuadrada es:", total_división)