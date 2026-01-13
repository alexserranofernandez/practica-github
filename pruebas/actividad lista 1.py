milista=[1,2,3,4,5,6]
milistapor2=[]
milistacopiada=[]
milistacopiada=milista
maximo=max(milista)
minimo=min(milista)
suma=sum(milista)
print(milista)
print(f"Maximo: {maximo}")
print(f"Minimo: {minimo}")
print(f"Suma: {suma}")

for i in range (len(milista)):
    calculo=milista[i]*2
    milistapor2.append(calculo)
print(milistapor2)
print(milistacopiada)