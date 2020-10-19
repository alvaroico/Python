# Exercício 36: Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
# o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a
# cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados
# deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também
# deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro,
# além da média das alturas e dos pesos dos clientes

alunoCodigo = []
alunoAltura = []
alunoPeso = []
codigo = 1
indice = 0
maisAlto = 0
maisBaixo = 0
maisGordo = 0
maisMagro = 0

def ordenar(listagem, maior, menor):
    if indice == 0:
        maior = menor = listagem[indice]
    else:
        if listagem[indice] > maior:
            maior = listagem[indice]
        if listagem[indice] < menor:
            menor = listagem[indice]
    return (maior, menor)
while codigo > 0:
    codigo = int(input("Digite seu Código ou 0 para finalizar: "))
    if codigo > 1:
        alunoCodigo.append(codigo)
        alunoAltura.append(int(input("Digite sua altura: ")))
        maisAlto, maisBaixo = ordenar(alunoAltura, maisAlto, maisBaixo)
        alunoPeso.append(int(input("Digite seu Peso: ")))
        maisGordo, maisMagro = ordenar(alunoPeso, maisGordo, maisMagro)
        indice += 1
def codigoAlunoBusca(listagem, oquebuscar, alunoCodigo):
    for i, v in enumerate(listagem):
        if v == oquebuscar:
            print(f'Código do mais baixo {alunoCodigo[i]}')
print(f'O mais Baixo, {maisBaixo}', end=' ')
codigoAlunoBusca(alunoAltura, maisBaixo, alunoCodigo)
print(f'O mais Alto, {maisAlto}', end=' ')
codigoAlunoBusca(alunoAltura, maisAlto, alunoCodigo)
print(f'O mais Magro, {maisMagro}', end=' ')
codigoAlunoBusca(alunoPeso, maisMagro, alunoCodigo)
print(f'O mais Gordo, {maisGordo}', end=' ')
codigoAlunoBusca(alunoPeso, maisGordo, alunoCodigo)
print(f'Media da altura {sum(alunoAltura)/len(alunoAltura)}')
print(f'Media da altura {sum(alunoPeso)/len(alunoPeso)}')