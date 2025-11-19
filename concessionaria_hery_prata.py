#CADASTRO DO CLIENTE
clientes = {

"nome": input("Digite o seu nome para iniciar o cadastro na nossa concessioária: "),
"telefone": input("Digite o seu telefone: "),
"saldo": float(input("Digite o seu saldo inicial: ")),

}

#fipe, valor base.
tabela_precos = {
 {
"marca":"bmw",
"modelo":"panamera",
"valor": 10000,

"fipe": {
 "valor_fipe": 900000,    
},

 }

}


#Tupla 
carros_aluguel = [
    ("LaFerrari","Mclaren Senna")
]

#Tupla
carros_vendas = [
    ("Porche Panamera","Bmw X6")
]

#Menu Principal
def menu():
    print("--- SEJA BEM VINDO, A NOSSA CONCESSIONARIA. ---")
    print("1 - Vender Carro")
    print("2 - Compra Carro")
    print("3 - Ver saldo")
    print("4 - sair")

if menu == 1:
    print("--- Venda De Carro ---")
    
    def vender_carro():
        marca = input("Digite a marca do carro: ")
        
        if marca not in tabela_precos:
            print("Este carro não está na tabela de referência. Venda não realizada.")

        modelo = input("Digite o modelo do carro")
        
        if modelo not in modelos_disponiveis:
            print("Modelo indisponivel.")

    valor_referencia = tabela_precos[marca]
    proposta = valor_referencia*0.80
    print(f"Valor referencia: {valor_referencia} ")
    print(f"Prosposta: R${proposta} ")
    confirmarcao = input("Deseja vender o carro? (s/n): ").lower()
        
   