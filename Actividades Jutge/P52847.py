num=input()
lista=num.split()
a=int(lista[0])
b=int(lista[1])
c=int(lista[2])
if a>c and a>b:
    print(a)
if b>c and b>a:
    print(b)
if c>a and c>b:
    print(c)