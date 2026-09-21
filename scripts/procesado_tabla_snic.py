
import pandas as pd
import os

directorio = os.path.dirname(os.path.abspath(__file__))

df_snic = pd.read_excel(os.path.join(directorio, '..', 'data', 'snic-departamentos-anual.xlsx'))

#columnas_innecesarias = ['provincia_id', 'departamento_id', 'cantidad_victimas_masc', 'cantidad_victimas_fem', 'cantidad_victimas_sd', 'tasa_hechos', 'tasa_victimas', 'tasa_victimas_fem', 'tasa_victimas_masc']
#df_snic = df_snic.drop(columns=columnas_innecesarias)
#df_snic = df_snic.query('codigo_delito_snic_id == "31"')


#df_snic.to_excel(os.path.join(directorio, '..', 'data', 'tabla_robos.xlsx'), index=False)
#print(df_snic.info())
#print(df_snic.describe())
