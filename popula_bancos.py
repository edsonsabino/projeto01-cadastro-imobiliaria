from modules.InterageDB import interageDB
import pandas as pd
import os 

##   instanciar banco
#obj_banco=interageDB("root","#Es181192","localhost","db_imobiliaria")

##   Path folder with csv's

current_folder= os.getcwd()         #   Getting current fonder
csv_folder='csv_data'               #   Folder with csv files

path_csv_folder=os.path.join(current_folder,csv_folder) #   path to csv folder

csv_names=["inquilinos_mock.csv",
           "proprietarios_mock.csv",
           "alugueis_mock.csv",
           "imoveis_mock.csv"]

##    Extract data with and store in data frame  4 times  


try:
    path=os.path.join(path_csv_folder,csv_names[0]) #   Iquilinos
    df_inq=pd.read_csv(path, sep=",")
except Exception as e:
    print(f"Erro in reading {csv_names[0]}", str(e))
    
try:
    path=os.path.join(path_csv_folder,csv_names[1]) #   Proprietarios
    df_prop=pd.read_csv(path, sep=",")
except Exception as e:
    print(f"Erro in reading {csv_names[1]}", str(e))    
    
try:
    path=os.path.join(path_csv_folder,csv_names[2]) #   Alugueis
    df_alug=pd.read_csv(path, sep=",")
except Exception as e:
    print(f"Erro in reading {csv_names[2]}", str(e))

try:
    path=os.path.join(path_csv_folder,csv_names[3]) #   Imoveis
    df_imo=pd.read_csv(path, sep=",")
except Exception as e:
    print(f"Erro in reading {csv_names[3]}", str(e))    

##  Correct id_imovel mismatch

try:
    df_alug['id_imovel']=df_imo['id_imovel']
except Exception as e:
    print("Error in correction", str(e))

##  Loading data to database

#   para cada df fazer a sequência de insert into
#   Dentro de cada df fazer intertuples para inserir no banco
#       Não está claro como conseguirei a lista de valores para enviar ao insert
#       Farei com iterrows por enquanto

