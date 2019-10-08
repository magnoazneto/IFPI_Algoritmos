def main():
	hora_inicial, minutos_iniciais = map(int, input('Digite a hora \
inicial do jogo, separando os minutos e as horas com ":" \n').split(':'))
	hora_final, minutos_finais = map(int, input('Digite a hora final do jogo, separando os minutos \
e as horas com ":"\n').split(':'))
	if hora_inicial > 23 or minutos_iniciais > 59 or hora_final > 23 or minutos_finais > 59:
		print('Por favor, note que o valor máximo válido é 23:59.')
		main()
	calcula_duracao(hora_inicial, minutos_iniciais, hora_final, minutos_finais)


def calcula_duracao(hora_inicial, minutos_iniciais, hora_final, minutos_finais):
	inicio = (hora_inicial * 60) + minutos_iniciais
	final = (hora_final * 60) + minutos_finais
	if final >= inicio:
		duracao = final - inicio
		duracao_horas = duracao // 60
		duracao_minutos = duracao - (duracao_horas * 60)
	else:
		duracao = 1440 - inicio
		duracao = duracao + final
		duracao_horas = duracao // 60
		duracao_minutos = duracao - (duracao_horas * 60)
	print('O jogo durou {} horas e {} minutos.'.format(duracao_horas, duracao_minutos))


if __name__ == '__main__':
	main()