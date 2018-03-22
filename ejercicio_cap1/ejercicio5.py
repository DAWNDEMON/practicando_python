a, b = 0, 1
while b < 1000:
	print (b, end=',')
	a, b = b, a+b
	#esto tendria que dar 1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987
