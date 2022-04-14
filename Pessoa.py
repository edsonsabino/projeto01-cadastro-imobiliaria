
class Pessoa():

    ##  Atributos de classe
    
    id_pessoa=""
    nome=""
    nascimento=""
    
    ##  Colhe as informações

    def cadastra_pessoa(self):
        try:

            entrada02=input("Qual o nome da pessoa: ")
            self.set_nome_pessoa(entrada02)
            
            entrada03=input("Qual a data de nascimento yyyy-mm-dd: ")
            self.set_data_pessoa(entrada03)

        except Exception as e:
            print("erro em coleta informação", str(e))
            
        self.insert_table("tbl_inquilinos",list_atributos,list_valores)

    ##  Setters

    def set_nome_pessoa(self,novo_nome_pessoa):
        try: 
            self.nome= novo_nome_pessoa
        except Exception as e:
            print("erro metodo set_nome_pessoa",str(e))

    def set_data_pessoa(self,novo_data_pessoa):
        try: 
            self.nascimento=novo_data_pessoa
        except Exception as e:
            print("erro metodo set_data_pessoa",str(e))            

