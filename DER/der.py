"""Analisis de datos Proyecto Final
Energias renovables"""

#Librerias necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#cargar archivo CSV
file_path = "data/complete_renewable_energy_dataset.csv"
df=pd.read_csv(file_path)
print(df.head())

#Exploración inicial
print("Dimensiones del dataset: ", df.shape)

#tipo
print("Tipos de datos categoricos o numericos", df.dtypes)

#datos nulos
print("Datos nulos por columna:\n", df.isnull().sum())

#Eliminar duplicados
print("Cantidad de filas duplicadas: ", df.duplicated().sum())
df = df.drop_duplicates()
print("Dimensiones del dataset: ", df.shape)
