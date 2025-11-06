print("\n CADASTRO DE USUARIO\n")
userC = input("Crie seu nome de usuario: ").strip().lower() #Tirar espaços e maisculas do inicio e do fim da string.
senhaC = input("Crie uma senha de usuario: ").strip()

print("\nUsuario cadastrado com sucesso\n")

while True:
    senhaC = input("Crie uma senha de usuario: ")

    if len(senhaC) <= 8:
        print("\n Usuario cadastrado com sucesso\n")
        break
    else:
        print("Senha muito longa! Digite uma senha com até 8 caracteres.\n")

while True: #True precisa do "T" maiusculo.
    print("== Login ==")
    nome = input("Usuario: ")
    senha = input("Senha: ")
    
    if nome == userC and senha == senhaC:
        print(f"Login realizado com sucesso!\n Bem Vindo(a) {nome}.")
        break 
    else:
        print("Usuario ou senha incorreta! Tente novamente... ")

