veces=0
veces1=0
veces2=0
veces3=0
veces4=0
veces5=0
veces6=0
import time
inicio=time.time()
import random
while time.time()-inicio<3:
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
total_tiempo=time.time()-inicio
print("RESUMEN")
print(f"Tiempo:{total_tiempo}")
print(f"Uno:{veces1}")
print(f"Dos:{veces2}")
print(f"Tres:{veces3}")
print(f"Cuatro:{veces4}")
print(f"Cinco:{veces5}")
print(f"Seis:{veces6}")