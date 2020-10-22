sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

def total():
  valorTotal= sp+rj+mg+es+outros
  return valorTotal

def stado(uf):
  porcentagem = (uf*100)/total()
  return porcentagem

print(f'A porcentagem de participação do estado de SP foi: {round(stado(sp), 2)}%')
print(f'A porcentagem de participação do estado de RJ foi: {round(stado(rj), 2)}%')
print(f'A porcentagem de participação do estado de MG foi: {round(stado(mg), 2)}%')
print(f'A porcentagem de participação do estado de ES foi: {round(stado(es), 2)}%')
print(f'A porcentagem de participação do estado de Outros foi: {round(stado(outros), 2)}%')
