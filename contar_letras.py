def contar_letras(nome):
    quantidade_letras = len(nome)
    return f"O nome {nome} tem {quantidade_letras} letras."

nome = input("Digite um nome: ")
resultado = contar_letras(nome)

print(resultado)