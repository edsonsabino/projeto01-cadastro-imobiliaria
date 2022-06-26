from modules.Cadastro import Cadastro
from modules.InterageDB import interageDB
from config.database_info import db_infos

#TO do => criar mensagens de sucesso para tarefas feitas

if __name__ == "__main__":
    
    obj_teste=Cadastro()
    print ("Bem vindo ao sistema de cadastro da imobiliária XPTO")
    
    try:
        resp=int(input ("""Digite a opção que deseja
                1 para cadastrar
                2 para executar algum comando SQL
                3 para fazer um select
                4 para sair
           """
           ))
    except Exception as e:
        print ("Error in input")
        
    if resp==4:
        print("Saiu do programa") 

    elif resp==1:
        obj_cadastro=Cadastro()
        obj_cadastro.faz_cadastro()
    
    elif resp==2:
        
        obj_db=interageDB(db_infos.get("user"),db_infos.get("password"),
                          db_infos.get("host"),db_infos.get("database")
                        )                   
        sql_string=input("Digite o comando SQL: ")
        obj_db.execute(sql_string)
        
    elif resp==3:
        
        obj_db=interageDB(db_infos.get("user"),db_infos.get("password"),
                          db_infos.get("host"),db_infos.get("database")
                            )
        
        sql_string=input("Digite o comando SQL: ")
        obj_db.selecionar(sql_string)

