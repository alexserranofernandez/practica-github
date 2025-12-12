#Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número.
veces=0
veces1=0
veces2=0
veces3=0
veces4=0
veces5=0
veces6=0
import random
while veces<=100:
    dado=random.randint(1,6)
    if dado==1:
        veces1=veces1+1
        veces=veces+1
    if dado==2:
        veces2=veces2+1
        veces=veces+1
    if dado==3:
        veces3=veces3+1
        veces=veces+1
    if dado==4:
        veces4=veces4+1
        veces=veces+1
    if dado==5:
        veces5=veces5+1
        veces=veces+1
    if dado==6:
        veces6=veces6+1
        veces=veces+1
print(f"El 1 ha salido {veces1} veces")
print(f"El 2 ha salido {veces2} veces")
print(f"El 3 ha salido {veces3} veces")
print(f"El 4 ha salido {veces4} veces")
print(f"El 5 ha salido {veces5} veces")
print(f"El 6 ha salido {veces6} veces")