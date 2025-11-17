
pessoa = {}#Criando um dicionario vazio chamado pessoa.

pessoa["nomes"] = input("Digite o nome: ")#Nome é chave e o que o usuario digitar sera o valor associado
pessoa["idade"] = int(input("Digite sua idade: "))#Idade é chave e o que o usuario digitar será valor associado,usamos int pois será um número inteiro
pessoa["cidade"] = input("Digite sua cidade: ")#Cidade é chave e o que o usuario digitar será o valor associado

print("\n === DADOS CADASTRADOS ===")
#Percorrendo o dicionario usando items(), chave = nome - valor = o conteudo guardado
for chave, valor in pessoa.items():
    print(f"{chave}:{valor}")#Exibindo chave e valor formatados
