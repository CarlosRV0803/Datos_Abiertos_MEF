'''
Created on May 11

@author: cramirez
'''

import requests
import pandas as pd

def query_api_consulta_amigable(sql_query):
    url = 'https://api.datosabiertos.mef.gob.pe/DatosAbiertos/v1/datastore_search_sql'
    params = {'sql': sql_query}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        #Accedemos a la información y lo guardamos en un dataframe
        data = response.json()
        records = data.get('records', [])
        df = pd.DataFrame(records)
        return df
    else:
        #En caso de error, mostramos el número del error
        print(f"Error: {response.status_code}")
        return None

#Declaramos el id de la base de datos abiertos de interés
id_api_2023 = "c28a4a61-8813-414c-ab72-44fd888292d4"

#Generamos un query para extraer la información del Pliego -- Ministerio de Desarrollo e Inclusión Social
sql_query = f"SELECT * FROM \"{id_api_2023}\" WHERE \"SECTOR\" = '40'" and \"PLIEGO\" = '040' 

df_midis_2023 = query_api_consulta_amigable(sql_query)

print(df_midis_2023.shape)
