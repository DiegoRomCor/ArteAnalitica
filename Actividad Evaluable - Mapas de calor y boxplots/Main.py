#Carga los datos usando tu lector de csv o con pandas. Es recomendable hacerlo con pandas.
#Realiza el análisis de las variables usando diagramas de cajas y bigotes, histogramas y mapas de calor.
#Responde las siguientes preguntas:
#¿Hay alguna variable que no aporta información?
#Si tuvieras que eliminar variables, ¿cuáles quitarías y por qué?
#¿Existen variables que tengan datos extraños?
#Si comparas las variables, ¿todas están en rangos similares? ¿Crees que esto afecte?¿
#¿Puedes encontrar grupos qué se parezcan? ¿Qué grupos son estos?

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Carga los datos usando tu lector de csv o con pandas. Es recomendable hacerlo con pandas.
df = pd.read_csv(r"C:\Users\52331\Desktop\Tecnologico de Monterrey\3er Semestre\ArteAnalitica\Actividad Evaluable - Mapas de calor y boxplots\Mall_Customers.csv")

#Realiza el análisis de las variables usando diagramas de cajas y bigotes, histogramas y mapas de calor.
print(df.head())
print(df.columns.tolist())

plt.figure(figsize=(14,6))
sns.boxplot(data=df_clean, x="track_genre", y="duration_min", order=order_by_duration)
plt.title("Duración (min) de canciones por género (ordenado por mediana)")
plt.xticks(rotation=90)
plt.ylabel("Duración (min)")
plt.show()