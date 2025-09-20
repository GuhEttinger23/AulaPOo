class Pessoa:
    def __init__(self, nome_completo: str, data_nascimento: str, cpf: str):
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self._cpf = cpf # Protegido