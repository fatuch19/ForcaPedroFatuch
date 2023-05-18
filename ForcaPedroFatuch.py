import random


palavras=["queijo","tomate","salada"]

resposta = random.choice(palavras)

x = len(resposta)

palavraPalpite = [0 for i in range(x)] 
for i in range(0, len(palavraPalpite)):
    palavraPalpite[i]="_"


resposta2 = [0 for i in range(x)]

for i in range(0,len(resposta)):
    resposta2[i]=resposta[i]



for i in range (0,11):

        
    if palavraPalpite==resposta2:
        print("Parabens, você ganhou!")
        break
    else:
        print(f"Tentativa: {i} de 10")
        letraPalpite = input("Digite uma letra:\n")
        for j in range(0,len(resposta)):
            if resposta[j]== letraPalpite:
                palavraPalpite[j]=letraPalpite

    
        print(palavraPalpite)
    if i == 10:
        print("Você perdeu!")    
        break
       