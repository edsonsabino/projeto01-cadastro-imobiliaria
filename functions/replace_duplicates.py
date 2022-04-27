import pandas as pd

def replace_duplicates(df,col_name,base_icr):
    
    try:
        df_dup=df[col_name].duplicated(keep="first")
    except Exception as e :
        print ("Error in replce_duplicates.Finding duplicates")
    
    try:
        for index,row in df[df_dup].iterrows():
            df.at[index,col_name]+=base_icr
            base_icr= 2*base_icr
        return df
    except Exception as e :
        print ("Error in replce_duplicates.Iteration")
