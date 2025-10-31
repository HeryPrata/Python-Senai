#Simulador de emprestimo

#Solicitação de entradas que serão armazenadas nas variaveis
print("===SISTEMA DE ANALISE DE CREDITO===")
nome = input("Nome do Cliente: ")
renda = float(input("Informe a renda mensal: R$"))
valorPedido = float(input("Informe o valor do emprestimo desejado: R$"))
parcelas = int(input("Informe o numero de parcelas: "))
historico = input("Possui um nome sujo? (Sim)(Não):")

#Calculo do valor da parcela
valorParcela = valorPedido/parcelas

#Exibe um resumo inicial do cliente
print(f"\nCliente: {nome} ") # A letra "F" antes das aspas transforma o texto em variavel.(Quaso a variavel já esteja declarada e com o mesmo nome.)
print(f"Valor do emprestimo: R$ {valorPedido:.2f}")# o comando ":.2f" determina a quantidade de casa decimais que o programa ira mostrar. Ex: o numero de ficaria 3,14.
print(f"Parcelas: {parcelas} x de R$ {valorParcela:.f2}")

#Verifica primeiro se o nome está limpado
if historico == "sim":
    print("Empréstimo NEGADO! Nome com restrição")
else:
    #Verifica se a parcela não ultrapassa 30% da renda
    if valorPedido > renda*0.3:
       print("Emprestimo NEGADO! Parcelas comprometem mais de 30% da renda.")
    else:
        #Verifica valor do emprestimo em relação á renda
        if valorPedido > renda*20:
            print("Emprestimo NEGADO! Valor solicitado muito alto para renda informada.")
        elif renda >= 5000 and valorPedido <= 10000:
            print("Emprestimo APROVADO! com taxa reduzida! Cliente perfil premium.")
        elif renda >= 3000 and renda < 5000:
            print("Emprestimo APROVADO com taxa padrão.")
        else:
            print("Emprestimo APROVADO com taxa elevada (cliente de risco)")
            
print("\n=== ANÁLISE CONCLUIDA ===")