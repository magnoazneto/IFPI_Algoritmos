def main():
	inicio, fim = map(int, input().split())
	print('O JOGO DUROU {} HORA(S)'.format(tempo_jogo(inicio, fim)))


def tempo_jogo(inicio, fim):
	inicio = inicio * 60
	fim = fim * 60
	if inicio == fim:
		duracao = 24
	elif inicio > fim:
		duracao = ((1440 - inicio) + fim) / 60
	else:
		duracao = (fim - inicio) / 60
	return int(duracao)


main()