intervalo=input()
lista=intervalo.split()
a1=int(lista[0])
b1=int(lista[1])
a2=int(lista[2])
b2=int(lista[3])
maximo=max(a1, a2)
minimo=min(b1, b2)
if maximo>minimo:
    print("[]")
else:
    print(f"[{maximo},{minimo}]")