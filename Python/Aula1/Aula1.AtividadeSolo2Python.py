valorCompra = float(input("Digite o valor"))
if valorCompra > 100:
    desconto = valorCompra*(0.9/100)
valorFinal = valorCompra - desconto
print("O valor total da compra com o desconto de 10% é: ",valorFinal)
