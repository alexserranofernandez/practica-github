#Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el 
#peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado 
#es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso. 
#var1=peso
#var2=altura
print("Este programa calcula tu IMC")
var1=float(input("Por favor, introduce tu peso en kilogramos"))
var2=float(input("Ahora introduce tu altura en metros"))
altura_cuadrado=var2**2
imc=var1/altura_cuadrado
imc_redondeado=round(imc,2)
if imc_redondeado>25:
    print ("Si tu peso es de",var1,"kilogramos, y tu altura es de",var2,"metros, tu imc es de",imc_redondeado,".Tienes sobrepeso.")
else:
    print ("Si tu peso es de",var1,"kilogramos, y tu peso es de",var2,"metros, tu imc es de",imc_redondeado)