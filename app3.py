from prettytable import PrettyTable
from urllib import parse, request
import pandas as pd
import requests
import bs4
import os
from csv import writer

def data_to_csv():
        cabezeras= []
        fuente_dat = ('http://www.sismologia.cl/ultimos_sismos.html')
        page = requests.get(fuente_dat)
        sopa = bs4.BeautifulSoup(page.text, 'lxml')
        tabla = sopa.find('table')

        for i in tabla.find_all('th'):
                title = i.text.strip()
                cabezeras.append(title)
        df = pd.DataFrame(columns = cabezeras )
        for filas in tabla.find_all('tr')[1:]:
                info = filas.find_all('td')
                filas_info = [td.text.strip() for td in info]
                length = len(df)
                df.loc[length] = filas_info
        data = (df.iloc[0,0:7])
        data2 = (df.iloc[1,0:7])
        print(data2)
        print(data)
        with open('sismos2.csv', 'a', newline='') as f_object:  
                writer_object = writer(f_object)
                writer_object.writerow(data)
                f_object.close()
                with open('sismos2.csv', 'a', newline='') as f_object:  
                         writer_object = writer(f_object)
                         writer_object.writerow(data2)
                         f_object.close()
data_to_csv()
       


