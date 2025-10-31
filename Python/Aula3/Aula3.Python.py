import random

secreto = random.randint(1,100)
tentativas = 3

print("=== Desafio do numero secreto")
print("=== Desafio do numero secreto")

while tentativas > 0:
    chute = int(input("Seu Chute"))

    if chute == secreto:
        print("Voce acertou")
        break
    elif chute < secreto:
        print("chute muito baixo")
    else:
        print("chuto muito alto")
        
    tentativas -= 1
    print(f"Tentativas restantes: {tentativas}\n")

if tentativas == 0:
   print(f"Acabaram as tentativas, o numero era: {secreto}")
   