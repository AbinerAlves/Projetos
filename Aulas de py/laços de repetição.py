opcao = 0

while opcao != 3:
    print("\n --- Menu do sistema ---")
    print("\n1. Saudação")
    print("\n2. Informação do sistema")
    print("\n3. Sair")

    try:opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Por favor Digite apenas números!")
        continue

# Estruturas de Decisão           
    if opcao == 1:
        print("\nOlá! é um prazer ajudar você.")
    elif opcao == 2:
        print("\nSistema: Python 3.10")
        print("\nStatus: Operacional")
    elif opcao == 3:
        print("\nSaíndo... Até logo!")
    else:
        print("\nOpção inválida ! Tente novamente.")

        