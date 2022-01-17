
import csv
from pandas.io.json import json_normalize
import pandas as pd

from csv import writer



url = "https://api-sismologia-chile.herokuapp.com/"
df = pd.read_json(url)


def sismos():
    data = (df.iloc[0,0:7])

    with open('datasismos.csv', 'a', newline='') as f_object:  
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(data)  
        # Close the file object
        f_object.close()

sismos()







