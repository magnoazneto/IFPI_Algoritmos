from utilidades import get_number, get_inteiro
def main():
    alunos = aprovados = reprovados = 0
    while True:
        matricula = get_inteiro('Matrícula: ')
        if matricula == 0: break
        alunos += 1
        nota1 = get_number('Digite a primeira nota: ')
        nota2 = get_number('Digite a segunda nota: ')
        nota3 = get_number('Digite a terceira nota: ')
        media = ((nota1*2) + (nota2*3) + (nota3*5)) / 10
        if media >= 7:
            print(f'Aluno aprovado com média {media:.2f}!')
            aprovados += 1
        else:
            print(f'Aluno reprovado com média {media:.2f}!')
            reprovados += 1
    print(f'Total de alunos: {alunos}')
    print(f'Alunos aprovados: {aprovados}')
    print(f'Alunos reprovados: {reprovados}')

    
main()
