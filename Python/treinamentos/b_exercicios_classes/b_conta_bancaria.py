class ContaBancaria:
    def __init__(self, titular, saldo, numero_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta

    def exibir_dados(self):
        print(f"\nTitular: {self.titular}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Saldo: R${self.saldo:.2f}\n")

    def depositar(self):
        valor = float(input("Qual o valor do depósito? R$"))
        if valor > 0:
            self.saldo += valor
            print(f"Depósito realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self):
        valor = float(input("Qual o valor será sacado? R$"))
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print(f"Saldo insuficiente. Saldo atual: R${self.saldo:.2f}")

# Criar conta fora do loop
titular = input("Por favor, coloque seu nome: ")
numero_conta = int(input("Por favor, insira o número da sua conta: "))
conta = ContaBancaria(titular, 0.0, numero_conta)

# Menu interativo
while True:
    entrada = int(input(
        "\n🟢 Oliveira Bank\n"
        "1 - Consultar dados da conta\n"
        "2 - Realizar depósito\n"
        "3 - Realizar saque\n"
        "4 - Sair\n"
        "Escolha uma opção: "
    ))

    match entrada:
        case 1:
            conta.exibir_dados()
        case 2:
            conta.depositar()
        case 3:
            conta.sacar()
        case 4:
            print("Encerrando o sistema. Obrigado por usar o Oliveira Bank!")
            break
        case _:
            print("Opção inválida. Tente novamente.")