lista=[]
while len(lista) < 3:
    num=input()
    if num != "":
        for i in num.split():
            lista.append(int(i))
            if len(lista)==3:
                break
print(lista[0]+lista[1]+lista[2])