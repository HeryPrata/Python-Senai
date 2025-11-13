meses = ("janeiro","fevereiro","marco","maio","abril","junho","julho","agosto","setembro","outubro","novembro","dezembro")

print("=== MESES DO ANO")
while True:
    numero = int(input("Digite um numero entre 1 e 12 para saber o mes correspondente: (Informe o numero -1 para sair)"))
    if numero == -1:
        print("Encerrando sistema")
        break

    if numero >= 1 and numero <= 12:# A tupla e inumerada de 0 a X
        print(f"O mes correspondente é {meses[numero - 1]}")#Serve para pegar o numero informado pelo usuario e subtrair -1 para pegar o valor certo, pois nossa tupla começa com 0
    else:
        print("Número invalido! Digite novamente entre 1 e 12...")