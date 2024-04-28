class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def abrir_conta(self, tipo_conta, saldo_inicial):
        if tipo_conta.lower() not in ["corrente", "poupanca"]:
            print("Tipo de conta inválido.")
            return None
        if saldo_inicial < 0:
            print("Saldo inicial não pode ser negativo.")
            return None

        nova_conta = None
        if tipo_conta.lower() == "corrente":
            nova_conta = ContaCorrente(saldo_inicial)
        elif tipo_conta.lower() == "poupanca":
            nova_conta = ContaPoupanca(saldo_inicial)

        if nova_conta:
            self.contas.append(nova_conta)
            print("Conta aberta com sucesso.")
        return nova_conta

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"


class Conta:
    def __init__(self, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial não pode ser negativo.")
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor <= 0:
            print("Valor do depósito deve ser maior que zero.")
            return
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor do saque deve ser maior que zero.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return
        self.saldo -= valor
        print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")

    def __str__(self):
        return f"Saldo: R${self.saldo}"


class ContaCorrente(Conta):
    def __init__(self, saldo_inicial):
        super().__init__(saldo_inicial)


class ContaPoupanca(Conta):
    def __init__(self, saldo_inicial):
        super().__init__(saldo_inicial)


def menu_principal():
    print("\n### Menu Principal ###")
    print("1. Abrir conta")
    print("2. Acessar conta")
    print("3. Sair")


def menu_acesso_conta(cliente):
    print("\n### Acessar Conta ###")
    print("Escolha a conta que deseja acessar:")
    for i, conta in enumerate(cliente.contas):
        print(f"{i + 1}. {conta}")
    print("0. Voltar")


# Solicitar nome e CPF do usuário
nome_usuario = input("Digite seu nome: ")
cpf_usuario = input("Digite seu CPF: ")
cliente1 = Cliente(nome_usuario, cpf_usuario)

while True:
    menu_principal()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tipo_conta = input("Digite o tipo de conta (corrente ou poupanca): ")
        saldo_inicial = float(input("Digite o saldo inicial da conta: "))
        cliente1.abrir_conta(tipo_conta, saldo_inicial)
    elif opcao == "2":
        if cliente1.contas:
            menu_acesso_conta(cliente1)
            opcao_conta = input("Escolha uma opção: ")
            if opcao_conta.isdigit() and 0 < int(opcao_conta) <= len(cliente1.contas):
                conta_selecionada = cliente1.contas[int(opcao_conta) - 1]
                while True:
                    print("\n### Menu da Conta ###")
                    print("1. Depositar")
                    print("2. Sacar")
                    print("3. Voltar")
                    opcao_operacao = input("Escolha uma opção: ")
                    if opcao_operacao == "1":
                        valor_deposito = float(input("Digite o valor do depósito: "))
                        conta_selecionada.depositar(valor_deposito)
                    elif opcao_operacao == "2":
                        valor_saque = float(input("Digite o valor do saque: "))
                        conta_selecionada.sacar(valor_saque)
                    elif opcao_operacao == "3":
                        break
                    else:
                        print("Opção inválida.")
            elif opcao_conta == "0":
                continue
            else:
                print("Opção inválida.")
        else:
            print("Cliente não possui contas.")
    elif opcao == "3":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida.")
