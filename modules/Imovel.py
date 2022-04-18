
class Imovel():
    
    ##  Atributos de classe
    
    id_imovel=""
    id_proprietario=""
    logradouro=""
    CEP=""
    bairro=""
    cidade=""
    
    ##  Colhe as informações

    def cadastra_imovel(self):
        try:
            entrada01=input("Qual o ID do imovel: ")
            self.set_id_imovel(entrada01)
            
            entrada012=input("Qual o ID do proprietario(a): ")
            self.set_id_proprietario(entrada012)

            entrada02=input("Qual o endereco do imóvel: ")
            self.set_logradouro(entrada02)
            
            entrada03=input("Qual o CEP do imovel (sem pontos e sem traços): ")
            self.set_CEP(entrada03)

            entrada04=input("Qual o bairro do imóvel: ")
            self.set_bairro(entrada04)
            
            entrada05=input("Em qual cidade o imvovel está localizado ")
            self.set_cidade(entrada05)

        except Exception as e:
            print("erro em cadastra_imovel ", str(e))


    ##  Setters
    def set_id_imovel(self,novo_id_imovel):
        try: 
            self.id_imovel= novo_id_imovel
        except Exception as e:
            print("erro metodo set_id_imovel",str(e))

    def set_id_proprietario(self,novo_id_proprietario):
        try: 
            self.id_proprietario= novo_id_proprietario
        except Exception as e:
            print("erro metodo set_id_proprietario",str(e))
    
    def set_logradouro(self,novo_logradouro):
        try: 
            self.logradouro= novo_logradouro
        except Exception as e:
            print("erro metodo set_logradouro",str(e))

    def set_CEP(self,novo_CEP):
        try: 
            self.CEP=novo_CEP
        except Exception as e:
            print("erro metodo set_CEP",str(e))

    def set_bairro(self,novo_bairro):
        try: 
            self.bairro=novo_bairro
        except Exception as e:
            print("erro metodo set_bairro",str(e))

    def set_cidade(self,novo_cidade):
        try: 
            self.cidade=novo_cidade
        except Exception as e:
            print("erro metodo set_cidade",str(e))