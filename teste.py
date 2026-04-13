for tentativa in range(1, 4):
    usuarioC = "abiner"
    senhaC = "2007"

    usuario = input(f"Digite Usuario (tentativa {tentativa}/3): ").strip()
    senha = input(f"Digite sua Senha (tentativa {tentativa}/3): ").strip()
    
    if usuario != usuarioC or senha != senhaC:
        print("Você digitou o usuario ou senha incorretos!")
    else:
        print(f"Bem vindo {usuario} tudo bem?")
        break
    
else:
    print("Tentativas esgotadas.")