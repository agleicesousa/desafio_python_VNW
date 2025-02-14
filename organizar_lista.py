# Missão 7: Organizando a Lista📋
#   Os números estão misturados e precisam ser organizados! 
#     Para resolver isso, você deve pegar os seguintes números: 8, 3, 10, 1 e 5,
#     armazená-los em uma lista e depois exibi-los em ordem crescente.
#     Isso ajudará a colocar tudo em ordem corretamente!  

def organizar_lista():
    numeros = [8, 3, 10, 1, 5]
    numeros.sort()
    return numeros 

print(organizar_lista())
