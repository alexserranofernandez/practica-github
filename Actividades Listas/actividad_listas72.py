#A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista
milista=[]
sinduplicados=[]
decision="s"
while decision!="n":
    letra=input("Introduce una letra:")
    if letra in "áàâä":
        letra="a"
    elif letra in "éèêë":
        letra="e"
    elif letra in "íìîï":
        letra="i"
    elif letra in "óòôö":
        letra="o"
    elif letra in "úùûü":
        letra="u"      
    if not letra.isnumeric():
        milista.append(letra)
    decision=input("¿Deseas repetir? s/n:")
sinduplicados=list(set(milista))
print(sinduplicados)