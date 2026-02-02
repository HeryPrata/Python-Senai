user = "HeryPrata"
senha = 1234

tentativaUser = input("Digite o seu user: ")

if user == "HeryPrata":
    print("Usuario correto")
else:
    print("Usuario incorreto")


tentativaSenha = int(input("Digite sua senha: "))

if tentativaSenha == 1234:
    opcao = int(input("1 = administrador, 2 = comum"))
    if opcao == 1:
        print("Bem Vindo, administrador!")
    else:
        print("Bem Vindo, usuário!")
else:
    print("Usuário ou senha incorretos.")



