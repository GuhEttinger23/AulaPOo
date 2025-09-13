# class Pessoa:
#     def __init__(self, nome: str, idade: int, peso: float, genero: str):
#         self.nome = nome 
#         self.idade = idade 
#         self.peso = peso
#         self.genero = genero
        
#     def andar(self):
#         print(f"{self.nome} esta andando")
#     def falar(self):
#         print(f"{self.nome} esta falando")
class Funcionario:
    def __init__(self, nome: str, cargo: str, salario: int):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    def __str__(self):
        return f"Nome: {self.nome}, Cargo: {self.cargo}, Salario: R$: {self.salario}"
    
    
class Empresa:
    def __init__(self, nome_empresa:str):
        self.nome_empresa = nome_empresa
        self.funcionarios = []
        
        
    def adicionar(self, funcionario):
        if isinstance(funcionario,Funcionario):
            self.funcionarios.append(funcionario)
            print(f"Funcionario {funcionario.nome} adicionado a {self.nome_empresa}")
        else:
            print(f"Erro!")
            
            
            
    def remover(self, nome_funcionario):
        funcionario_encot = None
        for func in self.funcionarios:
            if func.nome == nome_funcionario:
                funcionario_encot = func
                break
        if funcionario_encot:
            self.funcionarios.remove(funcionario_encot)
            print(f"Funcionario removido {nome_funcionario}")
        else:
            print(f"Funcionario nao foi encontrado")
            
            
            
    def listar_funcionarios(self):
        print(f"\n--- Funcionarios da {self.nome_empresa} ---")
        if not self.funcionarios:
            print(f"Nenhum funcionario cadrastado")
            return
        
        for func in self.funcionarios:
            print(func)
        print("-----------------")
        
minha_empresa = Empresa("Tech novas")
func1 = Funcionario("Gustavo", "Desenvolvedor", 2000)
minha_empresa.adicionar(func1)
minha_empresa.listar_funcionarios()