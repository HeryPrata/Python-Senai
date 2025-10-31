nome = input("Digite seu nome: ")
nota = int(input("Digite sua nota: "))
comp = int(input("Escolha a opção que se encaixe no seu comportanmento. 1 - bom, 2 - regular, 3 - ruim."))

if nota >= 7:
    if comp == 1: # Usei o "elif" é o "Else" para evitar do codigo rodar desnecessariamente
        print("Aprovado com merito!")
    elif comp == 2:
        print("Aprovado.") 
    else:
        print("Aprovado, mas com observações.")
else:
    if comp == 1:
        print("Recuperação, mas com observações. ")
    else:
        print("Reprovado por nota e comportamento.")

