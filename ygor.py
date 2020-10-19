import random

i = 0

while i < 3  :


 x = random.randint(0, 9)
 print(x)
 y = random.randint(0, 9)
 print(y)
 z = random.randint(0, 9)
 print(z)


 a = int(input("Acerte a cordenada X "))
 b = int(input("Acerte a cordenada Y "))
 c = int(input("Acerte a cordenada Z "))


 if a == x and b == y and c == z :
    print("Ganhou")
    break

 else : 
     print("Voce Errou ")    


         # SEGUNDA PARTE

 e = int(input("Digite a sua cordenada X "))
 f = int(input("Digite a sua cordenada Y "))
 g = int(input("Digite a sua cordenada Z "))


 v = random.randint(0, 9)
 w = random.randint(0, 9)
 k = random.randint(0, 9)


 if v == e and w == f and k == g :
    print("A maquina ganhou")

 else : 
     print(" A maquina Errou ")         
    

 i = i + 1