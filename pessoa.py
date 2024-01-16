from database import inserir
class Pessoa:

    def __init__(self: object, nome: str, idade: int, email: str, cep: int):
        self.__nome = nome
        self.__idade = idade
        self.__email = email
        self.__cep = cep
