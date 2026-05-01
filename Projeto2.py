cadastros = []

while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar pessoa")
    print("2 - Listar cadastros")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        
        while True:
            idade = input("Idade: ")
            if idade.isdigit():
                idade = int(idade)
                break
            else:
                print("Digite apenas números!")

        pessoa = {"nome": nome, "idade": idade}
        cadastros.append(pessoa)

        print("Cadastro realizado com sucesso!")

    elif opcao == "2":
        if len(cadastros) == 0:
            print("Nenhum cadastro encontrado.")
        else:
            print("\n=== LISTA DE CADASTROS ===")
            for p in cadastros:
                print(f"Nome: {p['nome']} | Idade: {p['idade']}")

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
