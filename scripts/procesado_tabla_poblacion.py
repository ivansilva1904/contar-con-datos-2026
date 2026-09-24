
import pandas as pd
import os

directorio = os.path.dirname(os.path.abspath(__file__))
df_poblacion = pd.read_excel(os.path.join(directorio, '..', 'data', 'raw data', 'Proyecciones departamento, 2010-2025.xlsx'))

"""columna_años = ['Año 2010',
                'Año 2011',
                'Año 2012',
                'Año 2013',
                'Año 2014',
                'Año 2015',
                'Año 2016',
                'Año 2017',
                'Año 2018',
                'Año 2019',
                'Año 2020',
                'Año 2021',
                'Año 2022',
                'Año 2023',
                'Año 2024',
                'Año 2025']"""

columna_años = [f"Año {año}" for año in range(2010, 2026)]

columnas = ['Nombre de provincia', 'Departamento', 'Código de departamento', ]

df_poblacion = pd.melt(df_poblacion, columnas, columna_años, "Año", "Poblacion")

df_poblacion['Año'] = df_poblacion['Año'].str.replace('Año ', '').astype(int)
df_poblacion['Poblacion'] = df_poblacion['Poblacion'].astype(int)

print(df_poblacion.info())
print("----")
print(df_poblacion.describe())
print("---")
print(df_poblacion)

df_poblacion.to_excel(os.path.join(directorio, '..', 'data', 'poblacion_estimaciones_tabla.xlsx'), index=False)
print("Archivo guardado correctamente en carpeta data")

