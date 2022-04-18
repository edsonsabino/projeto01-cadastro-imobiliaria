
class Aluguel():
    
    ##  Atributos de classe
    
    id_aluguel=""
    id_imovel=""
    id_inquilino=""
    
    ##  Colhe informações

    def cadastra_aluguel(self):
        try:
            entrada01=input("Qual o ID do aluguel: ")
            self.set_id_aluguel(entrada01)

            entrada02=input("Qual o ID do imóvel: ")
            self.set_id_imovel_aluguel(entrada02)
            
            entrada03=input("Qual o ID do inquilino: ")
            self.set_id_inquilino_aluguel(entrada03)

        except Exception as e:
            print("erro em cadastra aluguel", str(e))

    ##  Setters
    
    def set_id_aluguel(self,novo_id_aluguel):

        try: 
            self.id_aluguel= novo_id_aluguel
        except Exception as e:
            print("erro metodo set_id_aluguel",str(e))

    def set_id_imovel_aluguel(self,novo_id_imovel):
        try: 
            self.id_imovel= novo_id_imovel
        except Exception as e:
            print("erro metodo set_id_imovel",str(e))

    def set_id_inquilino_aluguel(self,novo_id_inquilino_aluguel):
        try: 
            self.id_inquilino=novo_id_inquilino_aluguel
        except Exception as e:
            print("erro metodo set_id_inquilino_aluguel",str(e))
            

            
