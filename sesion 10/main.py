# Importar la librería pandas, que es fundamental para el análisis de datos
import pandas as pd

# Define la ruta del archivo csv que contiene los datos
# Si el archivo está en el mismo directorio que este script, solo necesitas el nombre del archivo
path = 'Online_Retail.csv'

# Lee el archivo csv usando la función read_csv de pandas
# Se especifica la codificación latín 1 para manejar caracteres especiales
retail_data = pd.read_csv(path, encoding= 'latin1')

# Muestre el tipo de la variable retail_data para confirmas que es un dataframe de pandas.
# Un dataframe es una estructura de datos bidimensional similar a una tabla.
print(type(retail_data))


# Imprime todo el contenido del dataframe
print(retail_data)


