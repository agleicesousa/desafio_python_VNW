# Missão 1: Restaurando as Regras Escolares
#   O vírus apagou os critérios de aprovação dos alunos!
#   Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar
#   um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou
#   reprovado (nota menor ou igual à 5).

def regras_escolares():
    nota = float(input("Digite a nota: "))
    if nota >= 6:
        return "Aprovado"
    elif 0 <= nota < 6:
        return "Reprovado"
    else:
        return "Nota inválida"

regras_escolares()
