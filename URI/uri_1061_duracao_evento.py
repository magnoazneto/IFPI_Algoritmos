def main():
	dia = input().split()
	dia_inicial = int(dia[1])
	hora_inicial, minuto_inicial, segundo_inicial = map(int,\
(input().replace(' ', '')).split(':'))
	dia = input().split()
	dia_final = int(dia[1])
	hora_final, minuto_final, segundo_final = map(int,\
(input().replace(' ', '')).split(':'))
	duracao_evento(dia_inicial, hora_inicial, minuto_inicial, segundo_inicial,\
hora_final, dia_final, minuto_final, segundo_final)


def duracao_evento(dia_inicial, hora_inicial, minuto_inicial, segundo_inicial,\
hora_final, dia_final, minuto_final, segundo_final):
	dias = dia_final - dia_inicial
	inicio = (minuto_inicial * 60) + segundo_inicial
	inicio = inicio + (hora_inicial * 3600)
	fim = (minuto_final * 60) + segundo_final
	fim = fim + (hora_final * 3600)
	if inicio > fim:
		dias -= 1
		inicio = 86400 - inicio
		duracao = inicio + fim
	elif inicio <= fim:
		duracao = fim - inicio
	duracao_horas = duracao // 3600
	duracao_minutos = (duracao - (duracao_horas*3600)) // 60
	duracao_segundos = (duracao - (duracao_horas*3600) - (duracao_minutos*60))
	print('{} dia(s)'.format(dias))
	print('{} hora(s)'.format(duracao_horas))
	print('{} minuto(s)'.format(duracao_minutos))
	print('{} segundo(s)'.format(duracao_segundos))


main()