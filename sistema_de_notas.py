# Missão 3: Recuperando o Sistema de Notas
#   As classificações das provas desapareceram!
#   Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F.
#   Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota
#   do aluno e imprima sua classificação conforme a escala:
#      - A (90-100) – "Parabéns, você tirou A!"
#      - B (80-89) – "Muito bem, você tirou B."
#      - C (70-79) – "Bom trabalho, você tirou C."
#      - D (60-69) – "Fique atento, você tirou D."
#      - F (menos de 60) – "Estude um pouco mais, você tirou F."

def sistema_de_notas():
    nota = float(input("Digite a nota: "))
    if 90 <= nota <= 100:
        return "Parabéns, você tirou A!"
    elif 80 <= nota < 90:
        return "Muito bem, você tirou B."
    elif 70 <= nota < 80:
        return "Bom trabalho, você tirou C."
    elif 60 <= nota < 70:
        return "Fique atento, você tirou D."
    elif 50 <= nota < 60: # Este foi adicionado como um bônus
        return "Cuidado, você tirou E."
    else:
        return "Estude um pouco mais, você tirou F."

sistema_de_notas()
