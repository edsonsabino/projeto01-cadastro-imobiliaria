import pandas as pd
import os

def csv_to_df(path_csv_folder,nome_csv):
    try:
        path=os.path.join(path_csv_folder,nome_csv)
        df=pd.read_csv(path, sep=",")
        return df
    except Exception as e:
        print(f"Erro in csv_to_df. Filename {nome_csv}", str(e))       