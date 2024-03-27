import pandas as pd

# Cargar archivos de ingresos y gastos
df_ingresos = pd.read_csv('ingresos_digiData.csv')
df_gastos = pd.read_csv('gastos_digiData.csv')

# Convertir la columna 'fecha' a tipo datetime
df_ingresos['fecha'] = pd.to_datetime(df_ingresos['fecha'])
df_gastos['fecha'] = pd.to_datetime(df_gastos['fecha'])

# Extraer año y mes de la fecha
df_ingresos['año'] = df_ingresos['fecha'].dt.year
df_ingresos['mes'] = df_ingresos['fecha'].dt.month
df_gastos['año'] = df_gastos['fecha'].dt.year
df_gastos['mes'] = df_gastos['fecha'].dt.month

# Agrupar ingresos y gastos por año, mes y sucursal y sumar los montos
ingresos_agrupados = df_ingresos.groupby(['año', 'mes', 'sucursal'])['ingreso'].sum().reset_index()
gastos_agrupados = df_gastos.groupby(['año', 'mes', 'sucursal'])['gasto'].sum().reset_index()

# Fusionar datos de ingresos y gastos
datos_combinados = pd.merge(ingresos_agrupados, gastos_agrupados, on=['año', 'mes', 'sucursal'], how='outer').fillna(0)

# Calcular beneficios
datos_combinados['beneficios'] = datos_combinados['ingreso'] - datos_combinados['gasto']

# Seleccionar columnas requeridas y dar formato a la fecha
datos_combinados['fecha'] = datos_combinados.apply(lambda x: f"01/{x['mes']:02d}/{x['año']}", axis=1)
datos_combinados = datos_combinados[['fecha', 'sucursal', 'ingreso', 'gasto', 'beneficios']]

# Guardar datos como CSV
datos_combinados.to_csv('beneficios_digiData.csv', index=False)

print("Archivo de beneficios generado y guardado como 'beneficios_digiData.csv'")
