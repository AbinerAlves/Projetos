
media = float(input("Escreva a sua nota: "))

match media:
    case m if m  < 5.0:
        print("Reprovado! (média:", media, ")")
    case m if m >= 7.0:
        print("Aprovado! (média:", media, ")")
    case m if m >= 5.0:
        print("Em recuperação! (média:", media, ")")
    case _:
        print("Média invalida! Digite a média novamente.")