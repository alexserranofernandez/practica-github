import math
numero=float(input())
menor=math.floor(numero)
mayor=math.ceil(numero)
resto=numero%2
if resto==0.5:
    numero=numero+0.5
redondeo=round(numero)
print(menor,mayor, int(redondeo))