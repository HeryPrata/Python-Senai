#Objetivo, criar um programa de gerenciador de notas e mostrar o uso de len(), append(), sum(), remove().

#lista vazia para armazenar as notas
notas = []

print("=== GERENCIADOR DE NOTAS ===")

while True:
    print("\nMENU DE OPÇÕES: ")
    print("1 - Adicionar nota")
    print("2 - Remover nota")
    print("3 - Mostrar todas notas")
    print("4 - Mostrar a quantidade e media de notas")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))
    #Se a opção for igual a 1, adicionar nota
    if opcao == 1:
        nota =float(input("Digite a nota: "))
        notas.append(notas)
        print("Nota adicionada com sucesso!")
    #Remove nota
    elif opcao:
        if len(notas) == 0:
            print("Não há notas para remover!")
        else:
            print(f"Notas atuais: {notas}")
            remover = float(input("Digite a nota que deseja remover"))
            if remover in notas:
               notas.remover(remover)
               print(f"Nota {remover} removida com sucesso!")
            else:
               print("Essa nota não esta na lista")
#Mostrar todas as notas
    elif opcao == 3:
        if len(notas) == 0:
           print("Nenhuma nota cadastrada ainda.")
        else:
            print(f"Notas cadastradas: {notas}")
#Mostrar quantidade e média
    elif opcao == 4:
        if len(notas) == 0:
           print("Nenhuma nota cadastrada ainda para calcular media")
        else:
            quantidade = len(notas)
            soma = sum(notas)
            media = soma/quantidade
            print(f"Quantidade de notas: {quantidade}")
            print(f"Soma das notas: {soma}")
            print(f"Média da turma: {media}")

            if media >= 7:
                print("A turma está com um bom desemponho")
            else:
                print("A turma precisa melhorar.")
    #Sair
    elif opcao == 5:
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção invalida! Tente novamente.")