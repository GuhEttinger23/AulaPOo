# class Veiculo():
#     def __init__(self):
#         self.cor = None
#         self.modelo =  None
#     def set_cor(self, cor):
#         self.cor = cor
#         return self

#     def set_modelo(self, modelo):
#         self.modelo = modelo
#         return self


# class Carro(Veiculo):
#     pass
      

# class Bicicleta(Veiculo):  
#     pass


# carro = Carro().set_cor("Vermelho").set_modelo("Sedan")
# bike = Bicicleta().set_cor("Azul").set_modelo("Speed")

# print(f"Carro: {carro.cor}, Modelo: {carro.modelo}")
# print(f"Bicicleta: {bike.cor}, Modelo: {bike.modelo}")

# class Calculadora():
#     def somar(self, a, b ):
#         if isinstance(a, int) and isinstance (b, int):
#             return a + b 
#         elif isinstance(a, str) and isinstance(b, str):
#             return a + " " + b 
#         else: 
#             return "Tipos incompativeis!"

# calc = Calculadora()

# print(calc.somar(5, 3))
# print(calc.somar("Ola", "mundo"))
# print(calc.somar("Ola", 3))

# class Veiculo():
#     def __init__(self):
#        pass
#     def acelerar(self, acelerar):
#         pass
#     def frear(self, frear):
#         pass

# class Carro(Veiculo):
#     def acelerar(self):
#         print("Carro esta acelerando")
        
#     def frear(self):
#         print("Carro esta freando")
    

# class Bicicleta(Veiculo):
#     def acelerar(self):
#         print("Bicicleta esta acelerando")
        
#     def frear(self):
#         print("Bicicleta esta freando")

# #POLIFORISMO
# veiculos = [Carro(), Bicicleta()]

# for v in veiculos:
#     v.acelerar()
#     v.frear()