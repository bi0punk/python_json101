
import csv
from pandas.io.json import json_normalize
import pandas as pd

from csv import writer



url = "https://api-sismologia-chile.herokuapp.com/"
df = pd.read_json(url)


def sismos():
    data = (df.iloc[0,0:7])

    with open('CSVFILE.csv', 'a', newline='') as f_object:  
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(data)  
        # Close the file object
        f_object.close()

sismos()









""" lista = [fec_loc, fec_utc, lat_sis, long_sis, prof_sis, mag_sis, ref_sis]

data_sis_info=open("datos.txt","w") 
data_sis_info(lista)
data_sis_info.close()
 """
 
""" fec_loc = (df.iloc[0, 0])
fec_utc = (df.iloc[0, 1])
lat_sis = (df.iloc[0, 2])
long_sis = (df.iloc[0, 3])
prof_sis = (df.iloc[0, 4])
mag_sis = (df.iloc[0, 5])
ref_sis = (df.iloc[0, 6]) """

""" df.to_csv("data.csv", sep='\t', encoding='utf-8')
 """

""" alldata = (fec_loc, fec_utc, lat_sis, long_sis, prof_sis, mag_sis, ref_sis) """
""" f = open('data1.csv', 'w')
# create the csv writer
writer = csv.writer(f)
# write a row to the csv file
writer.writerow(alldata)

# close the file
f.close()

 """



















""" print(type(df.iloc[1, 4])) """
