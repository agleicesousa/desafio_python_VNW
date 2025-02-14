# Missão 8: Acessando os Registros de Alunos
#   O sistema de alunos está desordenado! Para acessar as informações corretamente,
#   você precisa organizar os dados.
#     Crie uma tupla com os seguintes nomes: Ana, Bruno, Carla, Daniel, Eduardo
#     e exiba o primeiro e o último nome.  

def acessar_registros():
    alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
    primeiro_nome = alunos[0]
    ultimo_nome = alunos[-1]
    return primeiro_nome, ultimo_nome

primeiro, ultimo = acessar_registros()

print(f"O primeiro nome é {primeiro} e o último nome é {ultimo}.")
