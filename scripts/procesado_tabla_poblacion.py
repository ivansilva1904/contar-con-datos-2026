
import pandas as pd
import os

directorio = os.path.dirname(os.path.abspath(__file__))
df_poblacion = pd.read_excel(os.path.join(directorio, '..', 'data', 'raw data', 'Proyecciones departamento, 2010-2025.xlsx'))

print(df_poblacion)
