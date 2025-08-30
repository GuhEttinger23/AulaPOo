# nome = "Felipe"
# lista = []

# class Carro:
#     def __init__(self, qtd_portas: int , cor: str , modelo: str , ano: int):
#         self.qtd_portas = qtd_portas
#         self.cor = cor 
#         self.moedelo = modelo
#         self.ano = ano

# carro1 = Carro(4, "Azul", "Uno", 2005) 
# print(carro1.__dict__)
# print(carro1.cor)
# print(carro1.ano)
# print(carro1.moedelo)
# print(carro1.qtd_portas)

# print(type(carro1))
# tupla = {}
# tupla = tuple()CPF, nome completo, filiação e endereço. 
# nome = str("felipe")
# idade = int(6)

class Pessoa: 
    def __init__(self, nome_completo: str,data: str, endereço: str, cpf: int, qtd_dinheiro: int, agencia: str):
        self.nome_completo = nome_completo
        self.data = data
        self.endereço = endereço
        self.qtd_dinheiro = qtd_dinheiro
        self.agencia= agencia



class ContaCorrente:
    def __init__(self, agencia: int, numero: int ):
        self.agencia = agencia
        self.numero = numero
        self.credito = 0
        self.saldo = 0

    def depositar(self, valor: int):
        self.saldo += valor
  
    def add_credito(self, valor: int):
        self.credito += valor 

    def sacar(self,valor: float):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            return "Saldo insuficente para saque!!"
   
    def transferir(self, valor:float, conta):
        if self.saldo >= valor:
           conta.saldo += valor
           self.saldo -= valor
        else:
            return "Saldo insufciente para fazer transferencia"
        


class ContaPoupança:
    def __init__( self, agencia: int, numero: int):
        self.agencia = agencia
        self.numero = numero
        self.saldo = 0
    def depositar(self, valor: int):
        self.saldo += valor
  
    def sacar(self,valor: float):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            return "Saldo insuficente para saque!!"
   
    def transferir(self, valor:float, conta):
        if self.saldo >= valor:
           conta.saldo += valor
           self.saldo -= valor
        else:
            return "Saldo insufciente para fazer transferencia"
        
    


p1 = Pessoa("Gustavo Ettinger", "23/03/2009", "Rua joaquim", 48727450905, 3000, "Itau")    



conta1 = ContaCorrente(16728, 6827829009)
conta2 = ContaCorrente(16727, 6827829019)

# print(conta.__dict__)

# conta.depositar(1000)
# print(conta.__dict__)

# conta.sacar(10000)
print(conta1.__dict__)
print(conta2.__dict__)

conta1.transferir(500, conta2)

print(conta1.__dict__)
print(conta2.__dict__)


contap = ContaPoupança(175200, 62894990290)

conta1.transferir(100,contap)


print(conta1.__dict__)
print(contap.__dict__)