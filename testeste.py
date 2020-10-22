faturaDia = []
faturaValor = []
dia = 1
indice = 0
maiorFatura = 0
menorFatura = 0

def ordenar(listagem, maior, menor):
    if indice == 0:
        maior = menor = listagem[indice]
    else:
        if listagem[indice] > maior:
            maior = listagem[indice]
        if listagem[indice] < menor:
            menor = listagem[indice]
    return (maior, menor)
while dia > 0:
    dia = int(input("Digite o dia ou 0 para finalizar: "))
    if dia > 1:
        faturaDia.append(dia)
        faturaValor.append(int(input("Digite o faturamento: ")))
        maiorFatura, menorFatura = ordenar(faturaValor, maiorFatura, menorFatura)
        indice += 1
def diaDaFatura(listagem, oquebuscar, alunoCodigo):
    for i, v in enumerate(listagem):
        if v == oquebuscar:
            print(f'Código do mais baixo {alunoCodigo[i]}')
print(f'Menor valor de fatura, {menorFatura}', end=' ')
diaDaFatura(faturaValor, menorFatura, faturaDia)
print(f'Maior valor de fatura, {maiorFatura}', end=' ')
diaDaFatura(faturaValor, maiorFatura, faturaDia)
