
import csv
from pandas.io.json import json_normalize
import pandas as pd
import time
import threading
from csv import writer



url = "https://api-sismologia-chile.herokuapp.com/"
df = pd.read_json(url)

data = (df.iloc[0,0:7])

with open('datasismos.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(data)  
    f_object.close()
    df_notduplicate = pd.read_csv("datasismos.csv")
    df_notduplicate.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
    with open('datasismos.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(df_notduplicate)  
        f_object.close()


""" print(df_notduplicate) """ 
    
    

    



