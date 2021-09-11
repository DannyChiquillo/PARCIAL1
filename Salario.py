#hacer en python para ayudar a un trabajador a saber 
#cual sera su sueldo semanal, se sabe que 
#si tarbaja 40 horas o menos se le pagara 20 por hora 
#pero si trabaja mas de 40 horas entonces se le pagara a 25 por hora.

trabajo=int(input("Ingrese las horas que trabajó"))

if trabajo <=40:
	horas=trabajo *20
	print("su pago es de: $",horas)
elif trabajo >=41:
	horas=trabajo *25
	print("su pago es de: $",horas)