def acessar_registros():
    alunos = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
    primeiro_nome = alunos[0]
    ultimo_nome = alunos[-1]
    return primeiro_nome, ultimo_nome

primeiro, ultimo = acessar_registros()

print(f"O primeiro nome é {primeiro} e o último nome é {ultimo}.")
