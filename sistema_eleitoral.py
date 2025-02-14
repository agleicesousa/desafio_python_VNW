def sistema_eleitoral():
    idade = int(input("Digite sua idade: "))
    
    if idade >= 16:
        print("Você pode votar!")
    else:
        print("Você não pode votar!")

sistema_eleitoral()
