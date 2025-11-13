nomes = ()#Tupla vazia

print("=== LISTA DE NOMES ===")
#Estrutura de repetição que vai rodar cinco vezes pedindo nomes
for i in range(5):
    nome =input(f"Digite o {i+1} nome: ")
    nomes += (nome,)#Adiciona os nomes informados pelo usuario á tupla

print(f"Nomes cadastrados: {nomes}")
print(f"O primeiro nome é: {nomes[0]}")
print(f"O ultimo nome é: {nomes[-1]}")
print(f"A quantidade total de nomes é: {len(nomes)}")
