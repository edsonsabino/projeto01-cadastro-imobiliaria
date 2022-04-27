from functions.replace_duplicates import replace_duplicates
from modules.InterageDB import interageDB
from functions.df_to_database import df_to_database
from functions.csv_to_df import csv_to_df
import pandas as pd
import os 

##   instanciar banco
obj_banco=interageDB("root","#Es181192","localhost","db_imobiliaria")

##   Path folder with csv's

current_folder= os.getcwd()         #   Getting current fonder
csv_folder='csv_data'               #   Folder with csv files

path_csv_folder=os.path.join(current_folder,csv_folder) #   path to csv folder
csv_names=["inquilinos_mock.csv","proprietarios_mock.csv",
           "alugueis_mock.csv","imoveis_mock.csv"]

##    Extract data with and store in data frame  4 times  

df_inq=csv_to_df(path_csv_folder,csv_names[0])  #   Iquilinos
df_prop=csv_to_df(path_csv_folder,csv_names[1]) #   Proprietarios
df_alug=csv_to_df(path_csv_folder,csv_names[2]) #   Alugueis
df_imo=csv_to_df(path_csv_folder,csv_names[3])  #   Imoveis

##  Correct id_imovel duplicates
        
df_alug=replace_duplicates(df_alug,"id_aluguel",1000)
df_alug=replace_duplicates(df_alug,"id_imovel",100)

##  Force that all id_imovel from df_alug apear in df_imo

df_imo["id_imovel"]=df_alug["id_imovel"]

##  Loading data to database

df_to_database(df_inq,"tbl_inquilinos",df_inq.columns)
df_to_database(df_prop,"tbl_proprietarios",df_prop.columns)
df_to_database(df_imo,"tbl_imoveis",df_imo.columns)
df_to_database(df_alug,"tbl_alugueis",df_alug.columns)



