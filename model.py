from conexao import Conexao

class Model:
    def __init__(self):
        self.db_connection = Conexao().conectar()
        self.cur = self.db_connection.cursor()

    def inserir(self, nome, telefone, endereco, data_nascimento):
        try:
            comando = f"insert into person(codigo, nome, telefone, endereco, data_nascimento) values('','{nome}','{telefone}','{endereco}','{data_nascimento}')"
            self.cur.execute(comando)
            self.db_connection.commit()

            return f"{self.cur.rowcount} linha(s) afetada(s)!"
        except Exception as error:
            print(error)