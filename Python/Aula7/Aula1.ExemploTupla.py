numeros = ()#Criação de tupla com o nome números que ira guardar numeros fornecidos pelo usuario.
#Estrutura de repetição para permitir que o usuario digite várias números.
while True: #Como não sabemos quantos números irão ser informados usamos o "WHILE" ao inves do "For".
    n = int(input("Digite um número (ou -1 para sair): "))
    if n == -1:
       break #Codigo para interromper o laço.
    numeros += (n,)#Significado =+ numeros. Tupla e imutavel. logo para colocar novas informações colocamos uma tupla dentro de outra tupla,tupla essa que vai conter as novas informações que queremos acrecentar.

#Após sair da tupla, verificamos se a tupla está vazia ou não.
if len(numeros) > 0:
    print("\n === RESULTADOS ===")
    print(f"Números digitados: {numeros}")
    print(f"Quantidade: {len(numeros)}")#Len server para contar a quantidade de numeros digitados.
    print(f"Soma: {sum(numeros)}")#Sum server para somar todos os números.
    print(f"Maior números: {max(numeros)}")#Max pega o maior número.
    print(f"Menor número: {min(numeros)}")#Min pega o menor número.

    media = sum(numeros)/len(numeros)

    if media >= 50:
        print(f"Média: {media:.2f} -> Alta!")
    else:
        print(f"Média: {media:.2f} -> Baixa!")

else:
    print("Nenhum número foi adicionado!")