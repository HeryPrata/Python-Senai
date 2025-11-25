#CADASTRO DO CLIENTE
cliente = {

"nome": input("Digite o seu nome para iniciar o cadastro na nossa concessioária: "),
"telefone": input("Digite o seu telefone: "),
"saldo": float(input("Digite o seu saldo inicial: ")),

}

#Dicionario com os modelos e o valor fipe
tabela_precos = [
 
     
{
    "marca":"Porche",
    "modelo":"Panamera",
    "valor": 10000,

    "fipe": {
    "valor_fipe": 900000,    
    },
},


{
    "marca":"Ferrari",
    "modelo":"LaFerrari",
    "valor":"300000",

    "fipe": {
        "valor_fipe": 250000,
    },
},

{
    "marca":"Mclaren",
    "modelo":"Senna",
    "valor":400000,

    "fipe": {
        "valor":350000,
    },
},

{
    "marca":"Bmw",
    "modelo":"X6",
    "valor":950000,

    "fipe": {
        "valor":900000,
    },
},


 

]

#Lista de dicionarios. Com valores atribuidos a objetos.
# ":" atrela um rotulo nos modelos.
#rotulos "marca" e "modelo". valores
carros_aluguel = [ 
    {"marca":"Ferrari","modelo":"LaFerrari"},
    {"marca":"Mclaren","modelo":"Senna"}
]

carros_vendas = [
    {"marca":"Bmw","modelo":"X6"},
    {"marca":"Porche","modelo":"Panamera"}
]

carros_comprar = [
    {"marca":"Ferrari","modelo":"LaFerrari"},
    {"marca":"Mclaren","modelo":"Senna"},
    {"marca":"Bmw","modelo":"X6"},
    {"marca":"Porche","modelo":"Panamera"}
]

#Copia e cola: veículo, Automóveis, Você, Disponíveis.
def vender_carro():
    print("--- VENDA DE VEÍCULOS ---")
    
    marca = input;("Digite a marca que você deseja")
    modelo = input("Digite o modelo da marca que você escolheu")
    
    if marca not in carros_vendas:
        print("A marca não esta presente em nossa lista")
        return
    valor_referencia = tabela_precos[modelo]
    proposta = valor_referencia*0.80
    
    print(f"Valor referencial: {valor_referencia:.2f}")
    print(f"Prosposta da concessionaria: {proposta:.2f}")

    if cliente["saldo"] < proposta:
        print("Valor em saldo insuficiente. Tente buscar por outro modelo.")
        return

    confirmacao = input("Você aceita a prosposta? (s) ou (n): ")

    if confirmacao == "s":
        cliente ["saldo"] += proposta
        print("Venda realizada com sucesso!")
    else:
        print("Venda cancelada.")


def alugar_carro():
    print("--- ALUGUE DE VEÍCULOS ---")
    if not carros_aluguel:
        print("Não a veículo disponivel para aluguel.")
        return
    
    print("\n--- Veículos Disponíveis ---")
    for carro in carros_aluguel:
     marca = carro["marca"]
     modelo = carro["modelo"]
     print(f"- Marca: {marca}\n- Modelo: {modelo}")
    
    escolha = int(input("Escolha o numero correspondente ao carrro do seu interrese: ")) -1 
    
    if escolha < 0 or escolha >= len(carros_aluguel):
        print("Opção invalida.")
    
    dias = int(input("Quantos dias você gostaria de alugar o carro?"))
    
    valor_final = dias*5

    print(f"O valor total do aluguel é: R$ {valor_final:.2f}")

    print("Verificando seu saldo...")

    if cliente["saldo"] < valor_final:
        print("Valor insuficiente. Tente buscar outro modelo ou diminuir a quantidade dias.")
        return
    
    confimarcao = input("Saldo suficientel, gostaria de alugar o Automóvel: (s) ou (n)")
    if confimarcao == "s":
        cliente["saldo"] -= valor_final
        print("Transação concluida. Você escolheu: {carro[escolha]}")
        carro = carros_aluguel.pop(escolha)#O pop é a ação de remover o item com a ação de obter o item em uma única linha.
    else:
        print("Transação cancelada.")
        return
    

def comprar_carro():
    print("--- COMPRAR DE VEÍCULOS ---")
    print("Automóveis disponiveis.")

    for veiculo in carros_vendas:
        marca = carros_vendas["marca"]
        modelo = carros_vendas["modelo"]
        print(f"Marca - {marca}\n Modelo - {modelo}")    











#Menu Principal
def menu():
    print("--- SEJA BEM VINDO, A NOSSA CONCESSIONARIA. ---")
    print("1 - Vender Carro")
    print("2 - Compra Carro")
    print("3 - Alugar Carro")
    print("4 - Ver saldo")
    print("5 - sair")

while True:
    menu()

    opcao = input("Escolha um opção: ")

    match opcao:
        case "1":
            vender_carro()
        case "2":
            comprar_carro()
        case "3":
            alugar_carro()
        case "4":
            print(f"O saldo disponivel: R${cliente['saldo']:.2f}")
        case "5":
            print("Encerrando sistema.")
            break
        case _:
            print("Opção invalida. Tente novamente.")