extrato = []
saldo = float(0)
LIMITE_SAQUES = 3
limite_diario = 500
saques_realizados = 0
total_saques = 0

print("""
Digite (1) para Saque.
Digite (2) para Depósito.
Digite (3) para Extrato.
Digite (4) para sair.
""")

while True:
    operacao = input("Qual operação voce deseja realizar?")
    operacao = int(operacao)
    if operacao < 1:
        print("Digite uma opcao valida!")
    elif operacao > 4:
        print("Digite uma opcao valida!")
    elif operacao == 1: #Deposito
        deposito = input("Qual o valor do seu depósito?")
        deposito = float(deposito)
        if deposito < 0:
            print("[ERROR] Depósito apenas para valores positivos")
        else:
            saldo += deposito
            extrato.append({"tipo": "Depósito", "valor": deposito})
            print(f"Seu novo saldo é {saldo}")

    elif operacao == 2:
        if saques_realizados >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques.")
            continue
        saque = input("Qual o valor que você quer sacar?")
        saque = float(saque)
        if saque < 0:
            print("Digite um valor valido!")
        elif saldo < saque:
            print("Você não tem saldo suficiente")
        elif total_saques + saque > limite_diario:
            print("Você excedeu o limite diário de saque.")
        else:
            saldo -= saque
            extrato.append({"tipo": "Saque", "valor": saque})
            saques_realizados += 1
            total_saques += saque
            print(f"Seu novo saldo é {saldo}")
    elif operacao == 3:
        print(f"Seu saldo atual é: {saldo}")
        for operacao in extrato:
            print(f"Tipo: {operacao['tipo']}, Valor: {operacao['valor']}")
    elif operacao == 4:
        total_saques = 0
        break