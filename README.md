# Datos_Abiertos_MEF
Información disponible en: [https://datosabiertos.mef.gob.pe/](https://datosabiertos.mef.gob.pe/dataset/presupuesto-y-ejecucion-de-gasto-devengado-mensual)

# Objetivos
- Generar una función que permita acceder a la información disponible de consulta amigable de datos abiertos.
- Guardar información reducida en un dataframe de pandas empleando en la extracción un query.

# Resumen función
- Se detalla el punto de acceso de la API que permite realizar consultas vía SQL: https://api.datosabiertos.mef.gob.pe/DatosAbiertos/v1/datastore_search_sql.
- Se genera el query de interés para extraer la información.
- Se emplea el id de la base de interés a partir de la cual se va a extraer la información.
- En caso de recibir una respuesta de la API, se almacena la información en un dataframe.
