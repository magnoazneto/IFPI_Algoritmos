def main():
	segundos = int(input())
	horas = segundos // 3600
	minutos = segundos // 60 - (horas * 60)
	segundos_final = segundos - ( minutos * 60) - (horas * 3600)
	print('{}:{}:{}'.format(horas, minutos, segundos_final))


main()