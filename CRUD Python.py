import mysql.connector

conexao = mysql.connector.connect(
    host='us-cdbr-east-05.cleardb.net',
    user='bccba512679edf',
    password='b0001474',
    database='heroku_bc6c7101c5632c0',
)

#mysql://bccba512679edf:b0001474@us-cdbr-east-05.cleardb.net/heroku_bc6c7101c5632c0?reconnect=true

cursor = conexao.cursor()

# CRUD

# CREATE
#nome_produto = "Pastel"
#valor = 4.50
#comando = f'INSERT INTO cantina (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados

# READ
#comando = f'SELECT * FROM cantina'
#cursor.execute(comando)
#resultado = cursor.fetchall() # ler banco de dados
#print(resultado)


# UPDATE
#nome_produto = "toddynho"
#valor = 3.50
#comando = f'UPDATE cantina SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados


# DELETE
#nome_produto = "toddynho"
#comando = f'DELETE FROM cantina WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados


cursor.close()
conexao.close()


