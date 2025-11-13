numeros = ()
contador = 0

print("=== DIGITE 5 NÚMEROS ===")

for i in range(5):
    n = int(input(f"Digite o {i+1} número: "))
    numeros += (n,)
    if n == 5:
     contador += 1

print(f"Números digitados: {numeros}")
print(f"Maior número é: {max(numeros)}")
print(f"Menor número é: {min(numeros)}")



   
print(f"O número 5 aperece {contador} vezes.")