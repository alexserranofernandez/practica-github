intervalo=input()
lista=intervalo.split()
a1=int(lista[0])
b1=int(lista[1])
a2=int(lista[2])
b2=int(lista[3])
if a1==a2 and b1==b2:
    print("=")
elif a1>=a2 and b2>=b1:
    print(1)
elif a1<=a2 and b2<=b1:
    print(2)
else:
    print("?")