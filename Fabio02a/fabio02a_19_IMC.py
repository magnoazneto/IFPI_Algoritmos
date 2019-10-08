def main():
	altura = float(input('Digite sua altura em metros: '))
	peso = float(input('Digite seu peso em KG: '))
	IMC = peso / (altura**2)
	print(f'IMC: {IMC:.2f}')
	if IMC < 25:
		print('Você está com peso normal!')
	elif IMC >= 25 and IMC <= 30:
		print('Você está obeso.')
	elif IMC > 30:
		print('Vocẽ tem obesidade mórbida.')
	else:
		print('Algum dado foi inserido errado.')
		main()


if __name__ == '__main__':
	main()