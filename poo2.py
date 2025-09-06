class Pessoa:
    def __init__(self,idade, nome):
         self.idade = idade
         self.nome = nome

    def locomover(self):
         print(f"{self.nome} caminha")

class Jogador(Pessoa):
     def __init__(self, idade, nome, velocidade, f_chute, precisao):
          super().__init__(idade, nome)
          self.velocidade = velocidade
          self.f_chute = f_chute
          self.precisao = precisao
     def locomover(self):
        print(f"{self.nome} corre")

class goleiro(Jogador):
     def __init__(self, idade, nome, velocidade, f_chute, precisao, evergadura):
          super().__init__(idade, nome, velocidade, f_chute, precisao)
          self.evergadura = evergadura   
     def locomover(self):
        print(f"{self.nome} pular")

Dida = goleiro(45, "Dida", 8, 70, 90, 1.90)
# neymar = Jogador(32, "Neymar", 12, 88, 82)
# neymar.locomover()
Dida.locomover()

print(Dida.__dict__)           

#   ATIVIDADE 1
# class Formas():
#     def __init__(self, altura, raio, base):
#       self.base = base
#       self.altura = altura
#       self.raio = raio
    
    
# class retangulo(Formas):
#     def __init__(self, altura, raio, base):
#         super().__init__(altura, raio, base)
#     def calcular_area_ret(self):
#         print("RETAGULO")
#         print(f"Area: {self.base} X {self.altura} = {self.base * self.altura}")
#         print(f"Perimetro: 2 ({self.base} + {self.altura}) = {2 * (self.base + self.altura)}")        


# class circulo(Formas):
#     def __init__(self, altura, raio, base):
#         super().__init__(altura, raio, base)
      
#     def calcular_area_cir(self):
#         print("CIRCULO")
#         print(f"Area: 3,14 X {self.raio} = {3,14* self.raio}")
#         print(f"Perimetro: 2 X 3,14 X {self.raio}= {2 * 3,14  *self.altura}")

# retangulo = retangulo(8,8,16)
# print(retangulo.calcular_area_ret())

# circulo = circulo(4,8,8)
# print(circulo.calcular_area_cir())


#   ATIVIDADE 2

# class Veiculo:
#     def __init__(self, cor, modelo, n_rodas):
#         self.cor = cor
#         self.modelo = modelo
#         self.n_rodas = n_rodas

#     def trocar_cor(self, nova_cor):
#         self.cor = nova_cor
#         print(f"A cor do veiculo foi trocada para {self.cor}.")

# class Bicicleta(Veiculo):
#     def __init__(self, cor, modelo, n_rodas):
#         super().__init__(cor, modelo, n_rodas)

# class Carro(Veiculo):
#     def __init__(self, cor, modelo, n_rodas):
#         super().__init__(cor, modelo, n_rodas)

# monark = Bicicleta("Vermelha", "Trabalho", 2)
# print(monark.__dict__)
# monark.trocar_cor("Azul")