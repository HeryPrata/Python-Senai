produtos = ("arroz","feijão","macarrão","leite","pão","ovo")
precos = (5.50, 7.90, 4.20, 6.30, 3.00, 19.96)

print("\n === LISTA DE PRODUTOS ===")
for i in range(len(produtos)):
    print(f"{produtos} - R$ {precos[i]:.2f}")

while True:
    nome = input("\nDigite o nome do produto para ver o preço (ou 'sair'): ").lower()
    #Método.lower() transforma o texto em minusculas para evitar erro de comparação
    if nome == "sair":
       print(f"Programa encerrada.")
       break

if nome in produtos:
    indice = produtos.index(nome)#Se o produto existe, encontramos sua posição em index()
    #index() serve para retormar a posição (indice) onde o nome foi encontrado dentro tupla
    print(f"O preço de {nome} é R$ {precos(indice):.2f}")
else:
    print("Produtos não encontrados.")