print("="*20 + " CALCULADORA SENAI " + "="*20)
n1 = float(input("Escreva o primeiro numero: "))
n2 = float(input("Escreva o segundo numero: "))
op = str(input("Digite o operador:  "))

if op == "+":
    print(f"RESULTADO de {n1} + {n2} = {n1 + n2 }")
elif op == "-":
    print(f"RESULTADO de {n1} - {n2} = {n1 - n2 }")
elif op == "/":
    print(f"RESULTADO de {n1} / {n2} = {n1 / n2 }")
elif op == "x":
    print(f"RESULTADO de {n1} X {n2} = {n1 * n2 }")
    

