def main():
    while True:
        h_i, m_i, h_f, m_f = map(int, input().split())
        if h_i == 0 and m_i == 0 and h_f == 0 and m_f == 0: break
        print(tempo_pdormir(h_i, m_i, h_f, m_f))
        


def tempo_pdormir(hora_inicial, minuto_inicial, hora_final,\
                     minuto_final):
	inicio = (hora_inicial * 60) + minuto_inicial
	fim = (hora_final * 60) + minuto_final
	if inicio > fim:
		inicio = 1440 - inicio
		duracao = inicio + fim
	elif inicio <= fim:
		duracao = fim - inicio
	return duracao


main()
