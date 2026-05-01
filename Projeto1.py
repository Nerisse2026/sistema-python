cadastro.py
print("=== Sistema de Cadastro ===")

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print("\nCadastro realizado com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")


nome = input("Digite seu nome: ")

while True:
    idade = input("Digite sua idade: ")
    if idade.isdigit():
        idade = int(idade)
        break
    else:
        print("Digite apenas números!")
