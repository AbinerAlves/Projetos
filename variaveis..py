nome_usuario = "instrutor"
senha_usuario = "senai123"
print("="*3 , "🔐 SISTEMA DE ACESSO SENAI" , "="*3 )
print("="*3 , "🔐 ENTRADA DE DADOS SENAI" , "="*3 )
usuario = input("Digite Usuario: ")
senha = input("Digite sua senha:  ")
if usuario != nome_usuario or senha != senha_usuario:
    print("Usuario ou senhas incorretos")
else:
    print("Senha e usuario CORRETA!🔓")
