import mysql.connector

class Conexao:
    def __init__(self):
        pass

    def conectar(self):
        try:
            db_connection = mysql.connector.connect(host="localhost", user="root", password="", database="bancoFlask")
            return db_connection
        except Exception as error:
            print(error)