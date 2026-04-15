while True:
    comando = input("Ecreva a ação que deseja realizar no jogo: ").lower()
 
    match comando:
        case "salvar":
            print("Salvando o seu jogo...")
        case "carregar":
            print("Carregando o jogo salvo...")
        case "sair":
            print("Saindo do jogo...")
        case _:
            print("Comando inválido! Tente novamente. ")
    break