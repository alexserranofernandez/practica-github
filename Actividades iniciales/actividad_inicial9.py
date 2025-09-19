var1=float(input("Introduce un número de segundos"))
total_minutos=var1/60
total_minutos_variosdecimales=round(total_minutos, 3)
total_segundos=var1/3600
total_segundos_variosdecimales=round(total_segundos, 6)
print("El número de segundos introducidos son", total_minutos_variosdecimales, "minutos y el son", total_segundos_variosdecimales,"segundos")
