
import pandas as pd
import os

directorio = os.path.dirname(os.path.abspath(__file__))

df_snic = pd.read_excel(os.path.join(directorio, '..', 'data', 'raw data', 'snic-departamentos-anual.xlsx'))

df_snic['cantidad_victimas'] = df_snic['cantidad_victimas'].fillna(0).astype(int)
df_snic['cantidad_victimas_masc'] = df_snic['cantidad_victimas_masc'].fillna(0).astype(int)
df_snic['cantidad_victimas_fem'] = df_snic['cantidad_victimas_fem'].fillna(0).astype(int)
df_snic['cantidad_victimas_sd'] = df_snic['cantidad_victimas_sd'].fillna(0).astype(int)

df_snic = df_snic.query('codigo_delito_snic_id == "31"')

#Estos son dos registros con el departamento NaN. Los borro porque las victimas son 0 en ambos
df_snic = df_snic.query('departamento_nombre.isna() == False')

columnas_innecesarias = ['codigo_delito_snic_id', 'codigo_delito_snic_nombre', 'provincia_id', 'departamento_id', 'cantidad_hechos', 'tasa_hechos', 'tasa_victimas', 'tasa_victimas_fem', 'tasa_victimas_masc']
df_snic = df_snic.drop(columns=columnas_innecesarias)

print(df_snic.info())
print("-----------")
print(df_snic.describe())
print("-------")
print(df_snic)


df_snic.to_excel(os.path.join(directorio, '..', 'data', 'snic_tabla.xlsx'), index=False)
print("Archivo snic_tabla.xlsx guardado correctamente en carpeta data")

#with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
#    print(df_snic)

