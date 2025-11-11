#Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos 
#de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’
var_numero=0
var_indice=0
for i in range(0,33):
    var_indice=var_indice+1
    var_numero=str(var_numero)+","+str(var_indice*3)
print(f"{var_numero}")
