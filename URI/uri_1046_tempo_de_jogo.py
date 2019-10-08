def main():
	hora_inicial, minutos_iniciais, hora_final, minutos_finais = map(int, input().split())
	calcula_duracao(hora_inicial, minutos_iniciais, hora_final, minutos_finais)


def calcula_duracao(hora_inicial, minutos_iniciais, hora_final, minutos_finais):
	inicio = (hora_inicial * 60) + minutos_iniciais
	final = (hora_final * 60) + minutos_finais
	if final == inicio: 
			duracao_horas = 24
			duracao_minutos = 0
	elif final > inicio:
		duracao = final - inicio
		duracao_horas = duracao // 60
		duracao_minutos = duracao - (duracao_horas * 60)
	else:
		duracao = 1440 - inicio
		duracao = duracao + final
		duracao_horas = duracao // 60
		duracao_minutos = duracao - (duracao_horas * 60)
	print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(duracao_horas, duracao_minutos))


if __name__ == '__main__':
	main()