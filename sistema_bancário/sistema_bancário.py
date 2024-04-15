menu = """"

[d] Depositar
[s] Sacar
[e] Extrato 
[q] Sair

=> """

saldo  = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 


while True: 

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        # Evitar depositos de numeros negativos 
        if valor > 0: 
            saldo += valor # Sendo maior que 0, add o valor na conta 
            extrato += f"Depósito: R${valor:.2f}\n"
        
        # Se for um numero negativo, avisa e volta para a tela principal 
        else: 
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite 
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        # Valor valido: 
        elif valor > 0: 
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        
        # Se tentar sacar um valor negativo da conta
        else:
            print("Operação falhou! O valor informado é inválido")


    elif opcao == "e":
        print("\n ================ EXTRATO ===============")
        print("Não foram realizadas movimetações." if not extrato else extrato) # if ternario verificando se o extrato ta vazio ou não
        print(f"\n Saldo: R${saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        break

    else: 
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")



