produto = {"nome": "café", "preco": 25.96, "categoria": "alimentos", "estoque": 30}
{"nome":"detergente","preco": 2.99, "categoria":"limpeza","estoque": 50}
{"nome":"sabao em pó","preco" :17.99, "categoria":"limpeza","estoque": 5}
{"nome":"detergente","preco": 7.99, "categoria":"limpeza","estoque": 15}


print("\n --- LISTA DE PRODUTO ---")
for i in produto:
    print("---------------------")
for chave, valor in i.items():#Serve para pegar chave e valor dentro do dicionario
    print(f"{chave}:{valor}")
