# Este é um Modelo de CRUD em Python que está constuido com a importação do MySQL, porém pode ser usado com qualquer Banco de Dados!!

import mysql.connector

conexao = mysql.connector.connect(
    host='',
    user='',
    password='',
    database='',
)

cursor = conexao.cursor()

# CRUD

# CREATE
#nome das colunas =
#nome das colunas =
#comando = f'INSERT INTO nome da tabela (nome das colunas, nome das colunas) VALUES ({nome das colunas}, {nome das colunas})'
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados

# READ
#comando = f'SELECT * FROM nome da tabela'
#cursor.execute(comando)
#resultado = cursor.fetchall() # ler banco de dados
#print(resultado)


# UPDATE
#nome das colunas =
#nome das colunas =
#comando = f'UPDATE nome da tabela SET nome das colunas = {nome das colunas} WHERE nome das colunas = {nome das colunas}'
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados


# DELETE
#nome das colunas =
#comando = f'DELETE FROM nome das colunas WHERE nome das colunas = {nome das colunas}'
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados


cursor.close()
conexao.close()


