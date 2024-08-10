menu = """
[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

=> """

saldo = 0
LIMITE = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Digite o valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Valor inválido para depósito.')
    elif opcao == 's':
        valor = float(input('Digite o valor a ser sacado: '))
        if valor > saldo:
            print('Saldo insuficiente.')
        elif valor > LIMITE:
            print(f'O valor do saque excede o limite de R$ {LIMITE:.2f}.')
        elif numero_saques >= LIMITE_SAQUES:
            print('Limite de saques diários atingido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Valor inválido para saque.')
    elif opcao == 'e':
        print('\n------ Extrato ------')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo atual: R$ {saldo:.2f}')
        print('----------------------\n')
    elif opcao == 'q':
        break
    else:
        print('Opção inválida.')