class Pessoa:
    def __init__(self, nome_completo: str, data_nascimento: str, cpf: str):
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self._cpf = cpf # Protegido


# Abstrata
class Conta(Pessoa):
    def __init__(self, nome_completo, data_nascimento, cpf, bandeira_cartao, instituicao_financeira):
        super().__init__(nome_completo, data_nascimento, cpf)
        self.bandeira_cartao = bandeira_cartao
        self.instituicao_financeira = instituicao_financeira


class Transferencia:
    def __init__(self, conta_origem: int, conta_destino: int, valor: float):
        self.conta_origem = conta_origem
        self.conta_destino = conta_destino
        self.valor = valor


class ContaCorrente(Conta):
    def __init__(self, nome_completo, data_nascimento, cpf, bandeira_cartao, instituicao_financeira,agencia: int, numero: int):
        super().__init__(nome_completo, data_nascimento, cpf, bandeira_cartao, instituicao_financeira)
        self.agencia = agencia
        self.numero = numero
        self.__saldo = 0
        self.credito = 0
        self.tranferescias: list[Transferencia] = []

    # Pegar o valor dentro do atributo privado
    # Getter
    @property
    def saldo(self):
        return self.__saldo
    # Setter
    @saldo.setter
    def saldo(self, novo_saldo):
        self.saldo = novo_saldo

    def depositar(self, valor: float):
        self.saldo += valor

    def adicionar_credito(self, valor):
        self.credito += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            return 'Saldo insuficente para saque'
        
    def transferir(self, valor: float, conta: Conta):
        if self.saldo >= valor:
            self.saldo -= valor
            conta.saldo += valor
            tranferencia = Transferencia(self.numero, conta.numero, valor)
            self.tranferescias.append(tranferencia)
        else:
            return 'Não possível fazer a transferência'
        
    def extrato_tranferencias(self):
        for transferencia in self.tranferescias:
            print(f'[Conta destino: {transferencia.conta_destino}, Conta origem: {transferencia.conta_origem}, Valor: {transferencia.valor}]')

class ContaPoupanca(Conta):
    def __init__(self, nome_completo, data_nascimento, cpf, bandeira_cartao, instituicao_financeira, agencia: int, numero: int):
        super().__init__(nome_completo, data_nascimento, cpf, bandeira_cartao, instituicao_financeira)
        self.agencia = agencia
        self.numero = numero
        self.saldo = 0
        self.tranferescias: list[Transferencia] = []

    # Pegar o valor dentro do atributo privado
    # Getter
    @property
    def saldo(self):
        return self.__saldo
    # Setter
    @saldo.setter
    def saldo(self, novo_saldo):
        self.saldo = novo_saldo

    def depositar(self, valor: float):
        self.saldo += valor

    def adicionar_credito(self, valor):
        self.credito += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            return 'Saldo insuficente para saque'
        
        def transferir(self, valor: float, conta: Conta):
            if self.saldo >= valor:
                self.saldo -= valor
                conta.saldo += valor
                tranferencia = Transferencia(self.numero, conta.numero, valor)
                self.tranferescias.append(tranferencia)
            else:
                return 'Não possível fazer a transferência'
        
    def extrato_tranferencias(self):
        for transferencia in self.tranferescias:
            print(f'[Conta destino: {transferencia.conta_destino}, Conta origem: {transferencia.conta_origem}, Valor: {transferencia.valor}]')
   
