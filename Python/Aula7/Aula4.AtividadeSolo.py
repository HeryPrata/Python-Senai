nomes = []
salarios = []

while True:
    nome = input("Digite o seu nome (Digite 'sair' para interrompe o programa): ")
    if nome == "sair":
        print("Programa finalizado.")
        break
    nomes.append(nome)
    
    salario = float(input("Digite o seu salario: "))
    salarios.append(salario)
    
   
media = sum(salarios)/len(salarios)

print(f"Quantidade de funcionarios: {len(nomes)}.")#len para ver a quantidade dentro da lista "nomes"
print(f"A media é: {media}.")
print(f"Maior salario: {max(salarios)}.")
print(f"Menor salario: {min(salarios)}.")