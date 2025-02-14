# Missão 2: O Sistema Eleitoral Secreto
#   O grêmio estudantil da escola realiza votações para decidir melhorias e inovações,
#   mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa
#   que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

def sistema_eleitoral():
    idade = int(input("Digite sua idade: "))
    
    if idade >= 16:
        print("Você pode votar!")
    else:
        print("Você não pode votar!")

sistema_eleitoral()
