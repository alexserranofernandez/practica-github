#Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
cantidad_valores=len(lista1)
numeros=0
for i in lista1: 
    if i.isnumeric():
        numeros=numeros+1