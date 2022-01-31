import pandas as pd
from csv import writer
df = pd.read_csv("/home/sysbot/datasismos.csv")
 


df2 = df.drop_duplicates(['FechaLocal'],keep='last')
print(df2)
print(df)
data = (df2)

with open('nd.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(data)  
    f_object.close()
    """ df_notduplicate = pd.read_csv("datasismos.csv")
    df_notduplicate.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
    with open('datasismos.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(df_notduplicate)  
        f_object.close()
 """




