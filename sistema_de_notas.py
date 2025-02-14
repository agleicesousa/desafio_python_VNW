def verificar_nota():
    nota = float(input("Digite a nota: "))
    if 90 <= nota <= 100:
        return "Parabéns, você tirou A!"
    elif 80 <= nota < 90:
        return "Muito bem, você tirou B."
    elif 70 <= nota < 80:
        return "Bom trabalho, você tirou C."
    elif 60 <= nota < 70:
        return "Fique atento, você tirou D."
    elif 50 <= nota < 60:
        return "Cuidado, você tirou E."
    else:
        return "Estude um pouco mais, você tirou F."

print(verificar_nota())
