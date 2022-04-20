from modules.InterageDB import interageDB
import pandas as pd

#   instanciar banco
obj_banco=interageDB("root","#Es181192","localhost","atividade_13")

#   Path csv's (achar alguma forma de referenciar OS, talvez)
        ## Fazer um for para cada elemento na pasta         
#   Buscar dados de arquivos # raw data
df1=pd.read_csv("DADOS_1.csv")
df2=pd.read_csv("DADOS_2.csv")

#   Tratamento dos dados

#   Inserção nos bancos (criar função aqui para não ter que repetir código)

for linha in dt_grande.intertuples():
        
val_id=linha.id
val_data=linha.data
val_valor=linha.valor
            
str_atr="id, data, valor"
str_val=str(val_id)+str(val_data)+str(val_valor)

obj_banco.insert_one("tbl_resultado",str_atr,str_val)