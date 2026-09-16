
import os
import pandas as pd

directorio = os.path.dirname(os.path.abspath(__file__))

df_snic = pd.read_excel(os.path.join(directorio, '..', 'data', 'snic-departamentos-anual.xlsx'))

codigos_defunciones = ['X60', 'X61', 'X62', 'X63', 'X64', 'X65', 'X66', 'X67', 'X68', 'X69', 'X70', 'X71', 'X72', 'X73', 'X74', 'X75', 'X76', 'X78', 'X79', 'X80', 'X81', 'X82', 'X83', 'X84']
df_codigos_defunciones = pd.read_excel(os.path.join(directorio, '..', 'data', 'descdef1.xlsx'), sheet_name="CODMUER")
df_codigos_provincias = pd.read_excel(os.path.join(directorio, '..', 'data', 'descdef1.xlsx'), sheet_name="PROVRES")
df_codigos_sexo = pd.read_excel(os.path.join(directorio, '..', 'data', 'descdef1.xlsx'), sheet_name="SEXO")

df_2005 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2005.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2006 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2006.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2007 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2007.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2008 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2008.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2009 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2009.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2010 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2010.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2011 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2011.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2012 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2012.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2013 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2013.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2014 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2014.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2015 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2015.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2016 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2016.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2017 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2017.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2018 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2018.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2019 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2019.csv'), encoding='latin1').query("CAUSA in @codigos_defunciones")
df_2020 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2020.csv'), sep=';', encoding='utf-8-sig').query("CAUSA in @codigos_defunciones")
df_2021 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2021.csv'), sep=';', encoding='utf-8-sig').query("CAUSA in @codigos_defunciones")
df_2022 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2022.csv'), sep=';', encoding='utf-8-sig').query("CAUSA in @codigos_defunciones")
df_2023 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2023.csv'), sep=';', encoding='utf-8-sig').query("CAUSA in @codigos_defunciones")
df_2024 = pd.read_csv(os.path.join(directorio, '..', 'data', 'datos_sobre_defunciones_2024.csv'), sep=';', encoding='utf-8-sig').query("CAUSA in @codigos_defunciones")


lista_df05_24 = [df_2005, df_2006, df_2007, df_2008, df_2009, df_2010, df_2011, df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022, df_2023, df_2024]
años = range(2005, 2025, 1)

for df, año in zip(lista_df05_24, años):
    df.insert(0, 'AÑO', año)

df_deis = pd.concat(lista_df05_24, ignore_index=True).drop(columns="MAT").query("PROVRES not in [98, 99]")

df_deis = pd.merge(left=df_deis, right=df_codigos_defunciones, how="inner", left_on="CAUSA", right_on="CODIGO").rename(columns={'VALOR': 'CAUSA_DESC'}).drop(columns="CODIGO")
df_deis = pd.merge(left=df_deis, right=df_codigos_provincias, how="inner", left_on="PROVRES", right_on="CODIGO").rename(columns={'VALOR': 'PROVINCIA'}).drop(columns="CODIGO")
df_deis = pd.merge(left=df_deis, right=df_codigos_sexo, how="left", left_on="SEXO", right_on="CODIGO").rename(columns={'VALOR': 'SEXO'}).drop(columns="CODIGO")

df_deis['GRUPEDAD'] = df_deis['GRUPEDAD'].str[3:]
df_deis['CAUSA_DESC'] = df_deis['CAUSA_DESC'].str.replace('autoinfligido intencionalmente ', '')
df_deis['CAUSA_DESC'] = df_deis['CAUSA_DESC'].str.replace('autoinfligida intencionalmente ', '')

print(df_deis)


#columnas_innecesarias = ['provincia_id', 'departamento_id', 'cantidad_victimas_masc', 'cantidad_victimas_fem', 'cantidad_victimas_sd', 'tasa_hechos', 'tasa_victimas', 'tasa_victimas_fem', 'tasa_victimas_masc']
#df_snic = df_snic.drop(columns=columnas_innecesarias)
#df_snic = df_snic.query('codigo_delito_snic_id == "31"')


#df_snic.to_excel(os.path.join(directorio, '..', 'data', 'tabla_robos.xlsx'), index=False)
#print(df_snic.info())
#print(df_snic.describe())
