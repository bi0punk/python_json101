
import csv
from pandas.io.json import json_normalize
import pandas as pd
import time
import threading
from csv import writer



url = "https://api-sismologia-chile.herokuapp.com/"
df = pd.read_json(url)



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def sismos():
    print(f"{bcolors.HEADER}ESTO ES UN TEXTO DE PRUEBA / este es un texto de prueba{bcolors.HEADER}")
    print(f"{bcolors.OKBLUE}ESTO ES UN TEXTO DE PRUEBA / este es un texto de prueba{bcolors.OKBLUE}")
    print(f"{bcolors.OKCYAN}ESTO ES UN TEXTO DE PRUEBA / este es un texto de prueba{bcolors.OKCYAN}")
    print(f"{bcolors.OKGREEN}ESTO ES UN TEXTO DE PRUEBA / este es un texto de prueba{bcolors.OKGREEN}")
    print(f"{bcolors.WARNING}ESTO ES UN TEXTO DE PRUEBA / este es un texto de prueba{bcolors.WARNING}")
    print(f"{bcolors.RED}ESTO ES UN TEXTO DE PRUEBA / este es un texto de prueba{bcolors.RED}")
    print(f"{bcolors.ENDC}ESTO ES UN TEXTO DE PRUEBA / este es un texto de prueba{bcolors.ENDC}")
    print(f"{bcolors.BOLD}ESTO ES UN TEXTO DE PRUEBA / este es un texto de prueba{bcolors.BOLD}")
    print(f"{bcolors.UNDERLINE}ESTO ES UN TEXTO DE PRUEBA / este es un texto de prueba{bcolors.UNDERLINE}")

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






