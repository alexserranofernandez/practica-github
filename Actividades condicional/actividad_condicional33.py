#Programa un código que permita contar el número de vocales de la siguiente frase: No 
#hay mal que dure cien años

var_frase="No hay mal que dure cien años"
var_frase=var_frase.lower()
vocal_a="a"
vocal_e="e"
vocal_i="i"
vocal_o="o"
vocal_u="u"
contador_vocal_a=0
contador_vocal_e=0
contador_vocal_i=0
contador_vocal_o=0
contador_vocal_u=0
for letra in var_frase:
    if letra==vocal_a:
        contador_vocal_a=contador_vocal_a+1
    elif letra==vocal_e:
        contador_vocal_e=contador_vocal_e+1
    elif letra==vocal_i:
        contador_vocal_i=contador_vocal_i+1
    elif letra==vocal_o:
        contador_vocal_o=contador_vocal_o+1
    elif letra==vocal_u:
        contador_vocal_u=contador_vocal_u+1   
print(f"El número de a es {contador_vocal_a}, el número de e es {contador_vocal_e} el número de i es {contador_vocal_i} el número de o es {contador_vocal_o} y el número de u es {contador_vocal_u}")
