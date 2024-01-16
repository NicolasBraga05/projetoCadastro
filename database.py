import sqlite3
from sqlite3 import Error
import main

# criar conexao
def ConexaoBanco():
    caminho = "C://Users//DevNi//PycharmProjects//banco_de_dados.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = ConexaoBanco()


def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela criada')
    except Error as ex:
        print(ex)


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido')
    except Error as ex:
        print(ex)

def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Registro deletado')



