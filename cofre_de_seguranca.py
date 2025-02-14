# Missão 5: Recuperando o Cofre de Segurança
#   O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha!
#   Agora, apenas quem souber a combinação correta poderá acessá-lo.
#     Crie um programa que solicite ao usuário uma senha e verifique se ela está correta.
#     A senha correta é "Python123".

def cofre_de_segurança():
    senha = input("Digite a senha: ")
    if senha == "Python123":
        print("Acesso permitido!")
    else:
        print("Acesso negado!")

cofre_de_segurança()
