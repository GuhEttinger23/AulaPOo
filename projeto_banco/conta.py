from pessoa import Pessoa
# Abstrata
class Conta(Pessoa):
    def __init__(self, nome_completo, data_nascimento, cpf, bandeira_cartao, instituicao_financeira):
        super().__init__(nome_completo, data_nascimento, cpf)
        self.bandeira_cartao = bandeira_cartao
        self.instituicao_financeira = instituicao_financeira