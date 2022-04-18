from logging import exception
import mysql.connector
#TO DO: função que cria a string da query
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
        """Conects to the database

        Returns:
            _tuple_: _connection object, cursor of that connection object_
        """
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
        """Disconects from database

        Args:
            vcon (_object_): _connection object_
            vcursor (_object_): _cursor_
        """
        
        try:
            vcursor.close() # fecha o cursor
            vcon.commit()   # formaliza mudança banco
            vcon.close()    # fecha obj de conexão
        except Exception as e:
            print("Erro no desconectar",str(e))

    ##  Método selecionar    
    def selecionar(self, o_que, de_onde, argumento):
        """Selects data from a database

        Args:
            o_que (_string_): what is to look for
            de_onde (_string_): in wich table to look for
            argumento (_string_): arguments to enrich the query statement

        Returns:
            _object_: _list of tuples with retrieved data_
        """
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
    def inser_one(self, nome_tabela, lista_atributos, lista_valores):
        """Inserts data into the table one row at a time

        Args:
            nome_tabela (_string_): name of the table
            lista_atributos (_list_): list with all columns names
            lista_valores (_list_): list with values to be inserted

        """
        str_list_atrib= ",".join(lista_atributos)
        obj_con, ft = self.conectar()
        try:
            ls=[]
            for elemento in lista_atributos:
                ls.append("""%s""")
                
            str_s=", ".join(ls)
            query2=f"""VALUES ({str_s})"""
            query1=f"""INSERT INTO {nome_tabela} ({str_list_atrib}) """
            query=(query1+query2)
            
            ft.execute(query,tuple(lista_valores))
            obj_con.commit()
            
        except mysql.connector.Error as e:
            print("Erro em insert_table", str(e))
        finally:
            self.desconectar(obj_con, ft)
    
    ##  Método geral execute
    def execute(self, query):
        """Método para inserir, alterar ou deletar um dado no banco de dados

        Args:
            query (string): query para buscar dados no banco de dados
        Returns:
            result: retorna o resultado da operação
        """
        try:
            con, ft = self.conectar()
            result = ft.execute(query)
            con.commit()
            return result
        except Exception as e:
            print("Error in def execute: ", str(e))
        finally:
            self.desconectar(con, ft)