while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == senha:
        print("Erro: A senha não pode ser igual ao nome do usuário. Por favor, tente novamente.")
    else:
        print("Usuário e senha aceitos!")
        break