
class Pessoa():

    id_pessoa=""
    nome_pessoa=""
    nascimento_pessoa=""

    



    def set_id_pessoa(self,novo_id_pessoa):
        try: 
            self.id_pessoa= novo_id_pessoa
        except Exception as e:
            print("erro metodo set_id_pessoa",str(e))

    def set_nome_pessoa(self,novo_nome_pessoa):
        try: 
            self.nome_pessoa= novo_nome_pessoa
        except Exception as e:
            print("erro metodo set_nome_pessoa",str(e))

    def set_data_pessoa(self,novo_data_pessoa):
        try: 
            self.nascimento_pessoa=novo_data_pessoa
        except Exception as e:
            print("erro metodo set_data_pessoa",str(e))            

def cadastra_pessoa(self):
        try:
            entrada01=input("Qual o ID do pessoa")
            self.set_id_pessoa(entrada01)

            entrada02=input("Qual o nome da pessoa")
            self.set_nome_pessoa(entrada02)
            
            entrada03=input("Qual a data de nascimento dd/mm/yy")
            self.set_data_pessoa(entrada03)

        except Exception as e:
            print("erro em cadastra aluguel", str(e))