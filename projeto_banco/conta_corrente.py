from conta import Conta
from transferencia import Transferencia

class ContaCorrente(Conta):
    def __init__(self, nome_completo, data_nascimento, cpf, bandeira_cartao, instituicao_financeira,agencia: int, numero: int):
        super().__init__(nome_completo, data_nascimento, cpf, bandeira_cartao, instituicao_financeira)
        self.agencia = agencia
        self.numero = numero
        self.__saldo = 0
        self.credito = 0
        self.tranferescias: list[Transferencia] = []

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self.saldo = novo_saldo

    def depositar(self, valor):
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
