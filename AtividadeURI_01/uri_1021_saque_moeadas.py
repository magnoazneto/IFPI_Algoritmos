def main():
	valor = float(input())
	valor = str(round(valor, 2))
	valor = valor.split('.')
	cedulas = int(valor[0])
	moedas = int(valor[1])
	saque(cedulas, moedas)

def saque(cedulas, moedas):	
	# calculo de cedulas
	notas_cem = cedulas // 100
	resto = cedulas % 100
	notas_cinquenta = resto // 50
	resto = resto - (notas_cinquenta*50)
	notas_vinte = resto // 20
	resto = resto - (notas_vinte*20)
	notas_dez = resto // 10
	resto = cedulas % 10
	notas_cinco = (resto // 5)
	resto = resto - (notas_cinco*5)
	notas_dois = resto // 2
	moeda_um_real = resto - (notas_dois*2)
	# calculo de moedas
	moeda_cinquenta = moedas // 50
	resto = moedas - (moeda_cinquenta*50)
	moeda_vinte_cinco = resto // 25
	resto = resto - (moeda_vinte_cinco*25)
	moeda_dez = resto // 10
	resto = resto - (moeda_dez*10)
	moeda_cinco = resto // 5
	moeda_um_cent = resto - (moeda_cinco*5)

	print('NOTAS:')
	print('{} nota(s) de R$ 100.00'.format(notas_cem))
	print('{} nota(s) de R$ 50.00'.format(notas_cinquenta))
	print('{} nota(s) de R$ 20.00'.format(notas_vinte))
	print('{} nota(s) de R$ 10.00'.format(notas_dez))
	print('{} nota(s) de R$ 5.00'.format(notas_cinco))
	print('{} nota(s) de R$ 2.00'.format(notas_dois))
	print('MOEDAS:')
	print('{} moeda(s) de R$ 1.00'.format(moeda_um_real))
	print('{} moeda(s) de R$ 0.50'.format(moeda_cinquenta))
	print('{} moeda(s) de R$ 0.25'.format(moeda_vinte_cinco))
	print('{} moeda(s) de R$ 0.10'.format(moeda_dez))
	print('{} moeda(s) de R$ 0.05'.format(moeda_cinco))
	print('{} moeda(s) de R$ 0.01'.format(moeda_um_cent))


main()