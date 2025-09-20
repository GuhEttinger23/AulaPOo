from imports import *
from random import randint

def exibicao():
    while True:
        print('Passo inicial para criar uma conta no banco Bradesco')

        nome_completo = input('Digite seu nome completo: ')
        data_nascimento = input('Digite a data do seu nascimento: Ex(08/09/2002)')
        cpf = int(input('Digite seu CPF: '))

        instrituicao_financeira = 'Bradesco'
        bandeira_cartao = 'ELO'
        agencia = '1990'

        numero = randint(1000, 9999)

        print('''
        ===== MENU PRINCIPAL ===== 
        1- Cadrastar uma Conta Poupança
        2- Cadrastar uma Conta corrente
        3-Sair
                ''')  
        tipo_conta = int(input("Digite uma das opcoes a cima:  "))

        if tipo_conta == 1:
            conta = ContaPoupanca(
                nome_completo=nome_completo,
                data_nascimento=data_nascimento,
                cpf=cpf,
                instituicao_financeira=instrituicao_financeira,
                bandeira_cartao=bandeira_cartao,
                agencia=agencia,
                numero=numero
            )
            print('Conta Poupança criada!!!')
            
        elif tipo_conta == 2:
        
            conta = ContaCorrente(
                nome_completo=nome_completo,
                data_nascimento=data_nascimento,
                cpf=cpf,
                instituicao_financeira=instrituicao_financeira,
                bandeira_cartao=bandeira_cartao,
                agencia=agencia,
                numero=numero
            )
            print('Conta Corrente criada!!!')
        elif tipo_conta == 3:
            break   


exibicao()
while True:


    op1 = input("Deseja fazer algo na conta? S/N:  ")

    if op1 == "S": 
        print('''
    ===== MENU DE OPÇOES ===== 
    1- Depositar
    2- Ver saldo
    3- Adicionar Credito
    4- Sacar
    5- Transferir
    6- Ver extrato de transferencias 
    7- Sair         
            ''')  
        op_menu = int(input("Digite alguma das opcoes do menu: "))

        if op_menu == 1:
            print(conta.saldo)
            depositar = float(input("Digite quanto vc quer depositar:  "))
            ContaPoupanca.depositar(depositar)
            print(conta.saldo)
        elif op_menu == 2:
           print(f"Seu saldo e {conta.saldo}")
        elif op_menu == 3:
            print(conta.saldo)
            adi_credito =  depositar = float(input("Digite quanto vc quer depositar:  "))
            ContaPoupanca.adicionar_credito(adi_credito)
            print(conta.saldo)
        elif op_menu == 4:
            print(conta.saldo)
            sacar = float(input("Digite quanto vc quer sacar:  "))

            ContaPoupanca.sacar(sacar)
            print(conta.saldo)
        elif op_menu == 5:
           conta1 = ContaPoupanca("chico", "01/03/1999", "12345678910", 'visa' "itau", "156", "1676728")
        elif op_menu == 6: 
            conta.extrato_tranferencias



