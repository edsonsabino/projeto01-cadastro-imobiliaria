from Cadastro import Cadastro
from InterageDB import interageDB

if __name__ == "__main__":
    
    #obj_teste=Cadastro()
    #obj_teste.faz_cadastro()
    
    #var_teste=obj_teste.var_pessoa.nome_pessoa
    list_atributos=["nome","data_nasc"]
    list_valores=["Joao Ubaldo Ribeiro", '1941-01-23']

    obj_teste=interageDB('root','#Es181192','localhost','db_imobiliaria')
    obj_teste.insert_table("tbl_inquilinos",list_atributos,list_valores)
    lista=obj_teste.selecionar('*','tbl_inquilinos',"")
    
    for iten in lista:
        pass
        print(iten,"\n")
    