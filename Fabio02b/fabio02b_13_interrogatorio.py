def main():
	contador = 0
	if input('Telefonou para a vitima?').upper() == 'S': contador += 1
	if input('Esteve no local do crime?').upper() == 'S': contador += 1 
	if input('Morava perto da vitima?').upper() == 'S': contador += 1 
	if input('Devia para a vítima?').upper() == 'S': contador += 1  
	if input('Já trabalhou com a vítima?').upper() == 'S': contador += 1 
	print(classificacao(contador))


def classificacao(contador):
	if contador == 2: return 'Suspeito' 
	if contador in range(3, 5): return 'Cúmplice' 
	if contador == 5: return 'Assassino' 
	return 'Inocente'


main()
	