print("Bem vindo ao Banco Oxetech, qual operação gostaria de realizar?")
print("1 - Saque")
print("2 - Depósito")
print("3 - Transferência")
print("4 - Saldo")
print("5 - Sair")

saldo = 0
while True:
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print("Você escolheu a opção de saque.")
        valor = float(input("Digite o valor que deseja sacar: "))
        if valor <= saldo:
            saldo = saldo - valor
            print("Saque realizado com sucesso!")
            print("Seu novo saldo é de: ", saldo)
        else:
            print("Saldo insuficiente.")
    elif opcao == 2:
        print("Você escolheu a opção de depósito.")
        valor = float(input("Digite o valor que deseja depositar: "))
        saldo = saldo + valor
        print("Depósito realizado com sucesso!")
        print("Seu novo saldo é de: ", saldo)
    elif opcao == 3:
        print("Você escolheu a opção de transferência.")
        valor = float(input("Digite o valor que deseja transferir: "))
        if valor <= saldo:
            saldo = saldo - valor
            print("Transferência realizada com sucesso!")
            print("Seu novo saldo é de: ", saldo)
        else:
            print("Saldo insuficiente.")
    elif opcao == 4:
        print("Você escolheu a opção de saldo.")
        print("Seu saldo é de: ", saldo)
    elif opcao == 5:
        print("Você escolheu a opção de sair.")
        print("Até logo!")
        break
        quit()
    else:
        print("Opção inválida.")