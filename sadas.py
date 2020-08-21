nome = input('Qual seu nome: ')
altura = input('Qual sua altura em metros: ')
peso = input('Qual seu peso e KG: ')

def calkIMC():
    imc = float(peso)/(float(altura)*float(altura))

    print("Ola", nome, "o seu IMC e ", imc)

calkIMC()
