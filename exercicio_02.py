class ContaBancaria:
    def __init__(self, nome):
        self.nome = nome
        self.__saldo = 0.0

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado.")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Erro: saldo insuficiente.")
        else:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")

    def consultar_saldo(self):
        print(f"Titular: {self.nome}")
        print(f"Saldo atual: R$ {self.__saldo:.2f}")


class ContaEspecial(ContaBancaria):
    def __init__(self, nome, limite):
        super().__init__(nome)
        self.limite = limite

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print("Erro: saldo e limite insuficientes.")
        else:
            self.saldo = self.saldo - valor
            print(f"Saque de R$ {valor:.2f} realizado.")


conta = ContaEspecial("Junior", 300)
conta.depositar(500)
conta.sacar(700)
conta.consultar_saldo()
