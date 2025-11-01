print("=== CADASTRO DE USUARIO ===")
userCadastrado = input("Crie um usuario:")
senhaCadastrada = input("Crie uma senha de usuario:")

print("\nUsuário cadastrado com sucesso! \n agora faça o login para acessar o sistema.\n")

print("=== LOGIN ===")
user = input("Digite seu nome de usuario: ")
senha = input("Digite sua senha: ")

if user == userCadastrado and senha == senhaCadastrada:
    print("Login realizado com sucesso!")

    nivel = int(input("Digite o seu nivel de acesso (1 - admin, 2 = comum)"))

    if nivel == 1:
        print(f"Bem vindo(a), administrador {userCadastrado}")
    elif nivel == 2:
        print(f"Bem vindo(a), usuario {userCadastrado}")
    else:
        print("Nivel de acesso invalido.")
else:
    print("Senha ou Usuario invalido, tente novamente.")