#A B C + D * + == A + (b+c)*d
def poisk(massiv):
	znaki = ['+', '-', '*', '/']
	i = 0
	while massiv[i] not in znaki:
		i += 1
	return i

def schet(massiv):
	i = poisk(massiv)
	a = int(massiv[i-2])
	b = int(massiv[i-1])
	if massiv[i] == '+':
		result = a+b
	elif massiv[i] == '-':
		result = a-b
	elif massiv[i] == '*':
		result = a*b
	elif massiv[i] == '/':
		result = a/b
	massiv[i] = str(result)
	del massiv[i-1]
	del massiv[i-2]
	if len(massiv) != 1:
		schet(massiv)

vvod = '8 9 + 1 7 - *'
massiv = []
for i in range(len(vvod)):
	if not vvod[i].isspace():
		massiv.append(vvod[i])

schet(massiv)
print(massiv[0])