from Cadastro import Cadastro
from InterageDB import interageDB

if __name__ == "__main__":
    
    #obj_teste=Cadastro()
    #obj_teste.faz_cadastro()
    
    #var_teste=obj_teste.var_pessoa.nome_pessoa
    
    obj_teste=interageDB('root','#Es181192','localhost','db_imobiliaria')
    lista=obj_teste.selecionar('*','tbl_inquilinos',"")
    for iten in lista:
        print(iten,"\n")
    