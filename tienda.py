#Ingresar monto de la compra
#dia de la semana
#si es martes o jueves aplicar 15% descuento a la compra
#ver descuento y total a pagar

compra = int(input("ingrese  monto de la compra"))
dia=input("ingrese dia de compra")

if dia == ("martes") or ("jueves"):
	descuento=compra *0.015
	pago = compra-descuento
	print("su descuento es",descuento)
	print(" monto a pagar",pago)
	 
else:
	print("su total a paga es",compra)