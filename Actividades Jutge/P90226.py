palabra=input()
lista=palabra.split()
a=lista[0]
b=lista[1]
if a>b:
    print(f"{a} > {b}")
elif a<b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")