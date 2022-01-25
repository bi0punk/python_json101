
from pandas.io.json import json_normalize
import pandas as pd
import mysql.connector
from mysql.connector import Error


import mysql.connector

""" mydb = mysql.connector.connect(
  host="localhost",
  user="sysbot",
  password="abc1",
  database="Sismologia"
) """

url = "https://api-sismologia-chile.herokuapp.com/"
df = pd.read_json(url)


print(type(df.iloc[0,:].tolist()))


fec_loc = (df.iloc[1, 0])
fec_utc = (df.iloc[1, 1])
lat_sis = (df.iloc[1, 2])
long_sis = (df.iloc[1, 3])
prof_sis = (df.iloc[1, 4])
mag_sis = (df.iloc[1, 5])
ref_sis = (df.iloc[1, 6])

""" print(fec_loc, fec_utc, lat_sis, long_sis, prof_sis, mag_sis, ref_sis)
print(type(df.iloc[1, 4])) """

""" mycursor = mydb.cursor() """

sql = "INSERT INTO Sismos (hor_locSis, hor_UtcSis, latSis, lonSis, profSis, magSis, refGeoSis) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = ('2012-06-18 10:34:09', '2012-06-18 10:34:09', lat_sis, long_sis, prof_sis, mag_sis, ref_sis)
""" mycursor.execute(sql, val) """

""" mydb.commit() """

""" print(mycursor.rowcount, "Dato insertado correctamente.") """

""" print(type(df.head(1))) """