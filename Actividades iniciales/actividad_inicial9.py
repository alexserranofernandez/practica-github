#Programa que pida los segundos y muestre por pantalla y en la misma frase los minutos 
#y las horas 
var1=float(input("Introduce un número de segundos"))
total_minutos=var1/60
total_minutos_variosdecimales=round(total_minutos, 3)
total_horas=var1/3600
total_horas_variosdecimales=round(total_horas, 6)
print("El número de segundos introducidos son", total_minutos_variosdecimales, "minutos y el son", total_horas_variosdecimales,"horas")
