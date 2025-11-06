#Inicia um loop que vai se repetir enquanto a condição for verdadeira
while True:#True é uma condição booleana que sempre é verdadeira, logo esse loop será infinito
    nome = input("Usuario: ")
    senha = input("Senha: ")
    #Condição que faz uma comparação para verificar se ambas condições são verdadeiras
    if nome == "admin" and senha == "1234":
        print("Login realizado com sucesso!")
        break #Comando que interrompe imediatamente o loop.
    else:
        print("Usuario ou senha incorreta! Tente novamente... ")
