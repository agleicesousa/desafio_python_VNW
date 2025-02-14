def regras_escolares():
    nota = float(input("Digite a nota: "))
    if nota >= 6:
        return "Aprovado"
    elif 0 <= nota < 6:
        return "Reprovado"
    else:
        return "Nota inválida"

regras_escolares()
