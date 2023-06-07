print("Bem vindo ao Banco Oxetech")
print("Insira qual operação deseja realizar")
print("1 - Saque")
print("2 - Depósito")
print("3 - Transferência")
print("4 - Saldo")
print("5 - Sair")

opcao = int(input("Digite a opção desejada: "))

dinheiro = 0

def Saque():
    global dinheiro
    saque = int(input("Digite o valor que deseja sacar: "))
    if saque > dinheiro:
        print("Saldo insuficiente")
    else:
        dinheiro = dinheiro - saque
        print("Saque realizado com sucesso")
        print("Seu saldo atual é de: ", dinheiro)

def Deposito():
    global dinheiro
    deposito = int(input("Digite o valor que deseja depositar: "))
    dinheiro = dinheiro + deposito
    print("Depósito realizado com sucesso")
    print("Seu saldo atual é de: ", dinheiro)

def Transferencia():
    global dinheiro
    transferencia = int(input("Digite o valor que deseja transferir: "))
    if transferencia > dinheiro:
        print("Saldo insuficiente")
    else:
        dinheiro = dinheiro - transferencia
        print("Transferência realizada com sucesso")
        print("Seu saldo atual é de: ", dinheiro)
        
def Saldo():
    global dinheiro
    print("Seu saldo atual é de: ", dinheiro)

while opcao != 5:
    if opcao == 1:
        Saque()
    elif opcao == 2:
        Deposito()
    elif opcao == 3:
        Transferencia()
    elif opcao == 4:
        Saldo()
    else:
        print("Opção inválida")
    opcao = int(input("Digite a opção desejada: "))
print("Obrigado por utilizar o Banco Oxetech")
print("Volte sempre")
