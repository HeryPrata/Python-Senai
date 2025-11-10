#Append() - Metodo que serve para adicionar um novo elemento ao final da lista
paises = ["Brasil","Argentina"]
print(paises)
paises.append("Russia")
print(paises)

#Remove() - Metodo que remove um elemento da lista

paises.remove("Argentina")
print(paises)

if "Brasil" in paises:
    paises.remove("Brasil")
    print(f"Pais removido com sucesso! {paises}")
else:
    print("Pais não existe")