# Missão 10: Contando Letras
#   O sistema precisa contar quantas letras há em um nome.
#     Crie uma função que receba um nome e diga quantas letras esse nome tem.
#       Exemplo: contar_letras("Ana")
#       Saída:" O nome Ana tem 3 letras"

def contar_letras(nome):
    quantidade_letras = len(nome)
    return f"O nome {nome} tem {quantidade_letras} letras."

nome = input("Digite um nome: ")
resultado = contar_letras(nome)

print(resultado)