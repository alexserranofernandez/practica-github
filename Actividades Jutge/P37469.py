segundos=int(input())
horas=segundos//3600
resto=segundos%3600
minutos=resto//60
segundos_final=resto%60
print(horas, minutos, segundos_final)