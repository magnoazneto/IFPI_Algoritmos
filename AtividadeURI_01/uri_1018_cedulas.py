def main():
	N = int(input())
	saque(N)

def saque(N):	
	notas_cem = N // 100
	resto = N % 100
	notas_cinquenta = resto // 50
	resto = resto - (notas_cinquenta*50)
	notas_vinte = resto // 20
	resto = resto - (notas_vinte*20)
	notas_dez = resto // 10
	resto = N % 10
	notas_cinco = (resto // 5)
	resto = resto - (notas_cinco*5)
	notas_dois = resto // 2
	resto = resto - (notas_dois*2)

	print(N)
	print('{} nota(s) de R$ 100,00'.format(notas_cem))
	print('{} nota(s) de R$ 50,00'.format(notas_cinquenta))
	print('{} nota(s) de R$ 20,00'.format(notas_vinte))
	print('{} nota(s) de R$ 10,00'.format(notas_dez))
	print('{} nota(s) de R$ 5,00'.format(notas_cinco))
	print('{} nota(s) de R$ 2,00'.format(notas_dois))
	print('{} nota(s) de R$ 1,00'.format(resto))


main()