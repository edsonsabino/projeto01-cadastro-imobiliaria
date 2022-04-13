import mysql.connector
#from modules.funcoes.func_gera_str import func_gera_str

class interageDB:
    
    ##  Atributos de classe
    
    usuario=""
    senha=""
    host=""
    nome_banco=""
    
    ##  Construtor da classe
    
    def __init__(self,vusuario,vsenha,vhost,vnome_banco):
        
        try:
            self.usuario=vusuario
            self.senha=vsenha
            self.host=vhost
            self.nome_banco=vnome_banco
        except Exception as e:
            print("erro construtor classe interageDB ",str(e))
            
    ##  Método conectar
    
    def conectar(self):
            try:
                obj_con= mysql.connector.connect(user=self.usuario,
                                                password=self.senha,
                                                host=self.host,
                                                database=self.nome_banco)
                ft = obj_con.cursor()   #   cursor
                
                return obj_con, ft
            except Exception as e:
                print("Erro em conectar",str(e)) 

    ##  Método desconectar

    def desconectar(self, vcon, vcursor):
        try:
            vcursor.close() # fecha o cursor
            vcon.commit()   # formaliza mudança banco
            vcon.close()    # fecha obj de conexão
        except Exception as e:
            print("Erro no desconectar",str(e))
    ##  Método para gerar strings pro insert (tentar buscar de pasta funções)

    ##  Método selecionar
    
    def selecionar(self, o_que, de_onde, argumento):
        try:
            (obj_con, ft) = self.conectar()
            query="SELECT "+o_que+" FROM "+de_onde+argumento+";"
            ft.execute(query)
            return ft.fetchall()
                    
        except Exception as e:
            print("Erro em selecionar",str(e))
        finally:
            self.desconectar(obj_con, ft)
            
    ##  Método inserir
    
    def inserir(self, nome_tabela, lista_atributos, lista_valores):
        
        #   montando strings (eliminado 27/11)
        #str_list_atrib=func_gera_str(lista_atributos)
        #str_list_val=func_gera_str(lista_valores)
        #print(str_list_atrib)
        
        
        str_list_atrib=lista_atributos
        str_list_val=lista_valores
        
        try:
            obj_con, ft = self.conectar()
            query="INSERT INTO "+nome_tabela+"("+str_list_atrib+")"+ " VALUES" +"(" +str_list_val+")"+";"
            ft.execute(query)
            obj_con.commit()
        except Exception as e:
            print("Erro em inserir", str(e))
        finally:
            self.desconectar(obj_con, ft)
    
    ##  Método deletar
        #todo
    ##  Método update
        #todo