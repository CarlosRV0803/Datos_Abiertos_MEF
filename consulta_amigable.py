'''
Created on May 11
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
