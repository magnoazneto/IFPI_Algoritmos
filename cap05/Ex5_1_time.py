import time

def main():
	tempo_decorrido = int(time.time())
	calcula_tempo(tempo_decorrido)


def calcula_tempo(tempo_decorrido):
	horas = tempo_decorrido // 3600
	minutos = tempo_decorrido // 60 - (horas * 60)
	segundos_final = tempo_decorrido - ( minutos * 60) - (horas * 3600)
	dias = horas // 24
	horas  = horas - (dias * 24)
	print(f'Esse valor equivale a {dias} dias, {horas} horas, {minutos} minutos e {segundos_final}')


if __name__ == '__main__':
	main()