import database
from time import sleep
def menu():
    erro_senha = 0
    login = input('Informe seu login: ')
    senha = input('Informe sua senha:  ')
    while True:
        vsql = "SELECT * FROM login WHERE login=('"+login+"') AND senha=('"+senha+"')"
        c = database.consultar(database.vcon, vsql)
        if c:
            print('*******************************')
            print('MENU DE CADASTRO')
            print('*******************************')
            print('')
            escolha = int(input('1- Para realizar cadastro | 2- Para consultar cadastro | 3- Para encerrar o programa: '))
            while True:
                if escolha == 1:
                    nome = str(input('Informe seu nome completo: '))
                    email = str(input('Informe o seu email: '))
                    cep = str(input('Informe o seu cep (ex: 00.000-000): '))
                    cpf = str(input('Informe seu CPF (ex: 000.000.000-00): '))
                    vsql = "INSERT INTO cadastro (NOME, EMAIL, CEP, CPF) VALUES('"+nome+"', '"+email+"', '"+cep+"', '"+cpf+"')"
                    database.inserir(database.vcon, vsql)
                elif escolha == 2:
                    cpf = str(input('Informe o CPF para consultar os dados do cadastro (ex: 000.000.000-00):  '))
                    vsql = "SELECT * FROM cadastro WHERE CPF=('"+cpf+"')"
                    print(database.consultar(database.vcon, vsql))
                elif escolha == 3:
                    print('PROGRAMA ENCERRADO')
                    break
                else:
                    print('Opcao invalida!')
                    escolha = int(input('1- Para realizar cadastro | 2- Para consultar cadastro | 3- Para encerrar o programa: '))
            break
        else:
            print('LOGIN OU SENHA INCORRETOS')
            erro_senha += 1
            if erro_senha >= 3:
                print('TENTE NOVAMENTE EM 1MIN.')
                for i in range(60):
                    i+=1
                    print(i)
                    sleep(1)
            else:
                login = input('Informe seu login: ')
                senha = input('Informe sua senha:  ')
                c = database.consultar(database.vcon, vsql)

if __name__ == '__main__':
    menu()
