from modules.Cadastro import Cadastro
from modules.InterageDB import interageDB
import datetime

if __name__ == "__main__":
    
    #obj_teste=Cadastro()
    #obj_teste.faz_cadastro()
    
    #var_teste=obj_teste.var_pessoa.nome_pessoa
    list_atributos=['nome','data_nasc']
    list_valores=['b3', '1941-01-23']
    print (type(list_valores[1]))

    obj_teste=interageDB('root','#Es181192','localhost','db_imobiliaria')
    obj_teste.insert_table('tbl_inquilinos',list_atributos,list_valores)
    obj_teste.execute("delete from tbl_inquilinos where nome = 'b3' ")

    lista=obj_teste.selecionar('*','tbl_inquilinos',"")

    for elemento in lista:
        print(elemento)
