x = int(input("Ingrese un entero, por favor: "))
#Pide al usuario ingresar un numero entero.
if x < 0:
	x = 0
	print ('Negativo cambiado a cero')
elif x == 0:
	print('cero')
elif x == 1:
	print('simple')
else:
	print('mas')
	#Nos dira 'mas'