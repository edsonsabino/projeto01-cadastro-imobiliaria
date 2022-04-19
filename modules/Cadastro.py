from modules.Aluguel import Aluguel
from modules.Imovel import Imovel
from modules.Pessoa import Pessoa
from modules.InterageDB import interageDB

class Cadastro(Pessoa,Imovel, Aluguel, interageDB):
    
    ##  Atributos de classe
    
    var_pessoa=Pessoa()
    var_imovel=Imovel()
    var_aluguel=Aluguel()
    var_interageDB=interageDB('root','#Es181192','localhost','db_imobiliaria')

    def faz_cadastro(self):
        control=True
        
        while control==True:
            
            print("\nO que voce gostaria de fazer\n ")
            print ("1 - para cadastrar um novo inquilino")
            print ("2 - para cadastrar um novo proprietario")
            print ("3 - para cadastrar um novo imovek")
            print ("4 - para cadastrar um novo Aluguel")
            print ("0 - para sair do cadastro")
            
            try:
                resposta=int(input("Sua resposta: "))
                if resposta in [0, 1,2,3,4]:
                    control=False
                else:
                    print("\nEntrada inválida, tente novamente")
            except Exception as e:
                print("erro em Cadastro.", str(e))

                
        if resposta in [1,2]:
            #   Arranjo para lidar com os nomes das tabelas
            
            lista_tbls=["inquilinos","proprietarios"]   # table names
            nome_tabela="tbl_"+lista_tbls[resposta-1]   # nome da tabela
                       
            try:
                self.var_pessoa.cadastra_pessoa()
                dicio=self.var_pessoa.__dict__
                
                atr=list(dicio.keys())      # list of column names
                vals=list(dicio.values())   # list of values
                
                self.var_interageDB.insert_one(nome_tabela,atr,vals)
                
            except Exception as e:
                print("Erro em cadastro de pessoa\n",str(e))


        elif resposta == 3:
            try:
                self.var_imovel.cadastra_imovel()
                dicio=self.var_pessoa.__dict__
                
                atr=list(dicio.keys())      # list of column names
                vals=list(dicio.values())   # list of values
                
                self.var_interageDB.insert_one("tbl_imoveis",atr,vals)
                
            except Exception as e:
                print("Erro em cadastro de imovel\n",str(e))
        elif resposta == 4:
            try:
                self.var_aluguel.cadastra_aluguel()
                dicio=self.var_pessoa.__dict__
                
                atr=list(dicio.keys())      # list of column names
                vals=list(dicio.values())   # list of values
                
                self.var_interageDB.insert_one("tbl_alugueis",atr,vals)                
            except Exception as e:
                print("Erro em cadastro de aluguel\n",str(e))
        elif resposta ==0:
            print("Saiu do cadastro\n")






    
    
   
    