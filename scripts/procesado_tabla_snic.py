
import pandas as pd
import os

directorio = os.path.dirname(os.path.abspath(__file__))

df_snic = pd.read_csv(os.path.join(directorio, '..', 'data', 'raw data', 'snic-departamentos-mes-sexo.csv'), sep=";", on_bad_lines="skip", low_memory=False)

df_snic['cantidad_victimas'] = df_snic['cantidad_victimas'].fillna(0).astype(int)
df_snic['cantidad_victimas_masc'] = df_snic['cantidad_victimas_masc'].fillna(0).astype(int)
df_snic['cantidad_victimas_fem'] = df_snic['cantidad_victimas_fem'].fillna(0).astype(int)
df_snic['cantidad_victimas_sd'] = df_snic['cantidad_victimas_sd'].fillna(0).astype(int)

df_snic = df_snic.query('codigo_delito_snic_id == "31"')

#Estos son dos registros con el departamento NaN. Los borro porque las victimas son 0 en ambos
df_snic = df_snic.query('departamento_nombre.isna() == False')

columnas_innecesarias = ['codigo_delito_snic_id', 'codigo_delito_snic_nombre', 'provincia_id', 'cantidad_hechos']
df_snic = df_snic.drop(columns=columnas_innecesarias)

#21 de +160 mil registros tenian 99 por mes, con esto los cambio a 1 para mantenerlos en su año
df_snic.loc[df_snic.query('mes == 99').index, 'mes'] = 1

df_snic['fecha'] = pd.to_datetime(
    '1-' + df_snic['mes'].astype(str) + '-' + df_snic['anio'].astype(str),
    format='%d-%m-%Y',
    errors='coerce'
).dt.date

print(df_snic.info())
print("-----------")
print(df_snic.describe())
print("-------")
print(df_snic)


#df_snic.to_excel(os.path.join(directorio, '..', 'data', 'snic_tabla.xlsx'), index=False)

#Necesito guardarlo con toda esta parafernalia para que me tome 'fecha' como campo datetime
with pd.ExcelWriter(os.path.join(directorio, '..', 'data', 'snic_tabla.xlsx'), engine="xlsxwriter", date_format="yyyy-mm-dd", datetime_format="yyyy-mm-dd") as writer: 
    df_snic.to_excel(writer, index=False)
print("Archivo snic_tabla.xlsx guardado correctamente en carpeta data")

#with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
#    print(df_snic)

