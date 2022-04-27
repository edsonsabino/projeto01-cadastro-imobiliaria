from modules.InterageDB import interageDB

def df_to_database(df,nome_tabela,lista_atributos):
    
    obj_banco=interageDB("root","#Es181192","localhost","db_imobiliaria")
    
    try:
        for index, linha in df.iterrows():
            obj_banco.insert_one(nome_tabela,lista_atributos,linha.tolist())
    except Exception as e:
        print(f"Error in df_to_database table {nome_tabela}", str(e))
