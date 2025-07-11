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
