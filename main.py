import database
from cep import buscaCEP
def menu():
    print('*******************************')
    print('MENU DE CADASTRO')
    print('*******************************')
    print('')
    while True:
        escolha = int(input('1- Para realizar cadastro | 2- Para consultar cadastro | 3- Para encerrar o programa: '))
        if escolha == 1:
            nome = str(input('Informe seu nome completo: '))
            email = str(input('Informe o seu email: '))
            cep = str(input('Informe o seu cep (ex: 00.000-000): '))
            cpf = str(input('Informe seu CPF: (ex: 000.000.000-00): '))
            vsql = "INSERT INTO cadastro (NOME, EMAIL, CEP, CPF) VALUES('"+nome+"', '"+email+"', '"+cep+"', '"+cpf+"')"
            database.inserir(database.vcon, vsql)
        elif escolha == 3:
            print('PROGRAMA ENCERRADO')
            break


if __name__ == '__main__':
    menu()
