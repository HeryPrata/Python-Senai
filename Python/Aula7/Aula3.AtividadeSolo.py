lista = []

while True: #Como não sabemos quantos números irão ser informados usamos o "WHILE" ao inves do "For".
    al = input("Digite o nome dos alunos (ou 'sair' para finalizar o programa): ")#pega as informações do uruario
    if al == 'sair':#Comando para interromper o codigo.
       break
    lista.append(al)#adicionando informações na lista

print(f"A quantidade de alunos é: {len(lista)}")
print(f"Lista completa:\n {lista}")