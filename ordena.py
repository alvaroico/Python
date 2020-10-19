listnum = []
mai = 0
men = 0

for c in range(0,5):
  listnum.append(int(input(f'Digite um valor para a posição {c}: ')))
  if c == 0:
    mai = men = listnum[c]
  else:
    if listnum[c] > mai:
      mai = listnum[c]
    if listnum[c] < men:
      men = listnum[c]

print(f'O maior valor digitado foi {mai}')
print(f'O menor valor digitado foi {men}')