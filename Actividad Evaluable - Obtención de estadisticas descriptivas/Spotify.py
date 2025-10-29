#1.- Carga los datos usando tu lector de csv o con pandas. Es recomendable hacerlo con pandas.
#2.- Verifica la cantidad de datos que tienes, las variables que contiene cada vector de datos e identifica el tipo de variables.
#3.- Analiza las variables para saber que representa cada una y en que rangos se encuentran. Si la descripción del problema no te lo indica, utiliza el máximo y el mínimo para encontrarlo.
#4.- Basándose en la media, mediana y desviación estándar de cada variable, que conclusiones puedes entregar de los datos.

#1.- Cargar datos
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\52331\Desktop\Tecnologico de Monterrey\3er Semestre\ArteAnalitica\Actividad Evaluable - Obtención de estadisticas descriptivas\spotify.csv")

#2.- Cantidad y tipos de datos
print("Informacion general:")
df.info()

print("Informacion especifica:")
shape = df.shape
print("shape = (filas, columnas)", shape)              

dtypes = df.dtypes
print("dtypes =\n", dtypes)

#3.- Rango y resumen por variable
print("Informacion general:")
print(df.describe(include='all').to_string())

print("Mediana:")
#Da error sin el numeric_only
print(df.median(numeric_only=True))