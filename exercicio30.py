Salario_Bruto = int(input("Digite seu salário bruto: "))


def INSS(x):
    if x <= 1751.81:
        return x * 0.08
    if x > 1751.81 and x <= 2919.72:
        return x * 0.09
    if x > 2919.72 and x <= 5839.45:
        return x * 0.11


def IR(x):
    if x <= 1903.98:
        return 0
    if x >= 1903.99 and x <= 2826.65:
        return (x * 0.075) - 142.80
    if x >= 2826.66 and x <= 3751.05:
        return (x * 0.15) - 354.80
    if x >= 3751.06 and x <= 4664.68:
        return (x * 0.225) - 636.13
    if x >= 4664.68:
        return (x * 0.275) - 869.36


valorINSS = INSS(Salario_Bruto)
valorIR = IR(Salario_Bruto)

print(" Seu INSS será de: ", valorINSS)
print(" Seu IR será de: ", valorIR)
print(" Seu Salario liquido será de: ", Salario_Bruto - valorINSS - valorIR)
