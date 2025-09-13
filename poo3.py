# class Conta: 
#     def __init__(self, nome_completo, data, endereço, cpf, qtd_dinheiro, agencia, numero_conta, numero):
#         super().__init__(nome_completo, data, endereço, cpf, qtd_dinheiro, agencia, numero_conta)
#         self.agencia = agencia
#         self.numero = numero
#         self.credito = 0
#         self.saldo = 0



# class Autor: 
#     def __init__(self, nome: str):
#         self.nome = nome

# class Livro:
#     def __init__(self, titulo: str, autor: Autor ):
#         self.titulo = titulo
#         self.autor = autor

# a = Autor("Felipe")

# l = Livro("Harry Pottrer", a)

# print(a.__dict__)    
# print(l.__dict__)
        

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
        self.__saldo = novo_saldo

    def depositar(self, valor: float):
        self.__saldo += valor

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

    def depositar(self, valor: float):
        self.saldo += valor

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
 

c1 = ContaCorrente('Felipe', '08/09/2000', '1234567879110', 'elo', 'Nubank', 123, 12345)

c2 = ContaCorrente('Gustavo', '09/10/2000', '10987654321', 'elo', 'Itau', 123, 54321)

c1.depositar(1000)

c1.transferir(200, c2)

print(c1.__dict__)

print('#'*50)

c1.extrato_tranferencias()

# c1.saldo = 10_000_000_000_000

