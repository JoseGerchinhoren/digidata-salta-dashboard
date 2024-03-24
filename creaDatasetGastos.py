import pandas as pd
import numpy as np
from random import randint, choice
from datetime import datetime, timedelta

# Obtener datos de ingresos del archivo dataset_ejemplo_digidata.csv
ingresos_df = pd.read_csv('dataset_ejemplo_digidata.csv')
ingresos_df['fecha'] = pd.to_datetime(ingresos_df['fecha'], format='%d/%m/%Y')
ingresos_df['fecha_mes'] = ingresos_df['fecha'].dt.to_period('M')
ingresos_por_mes = ingresos_df.groupby('fecha_mes')['importe'].sum()

# Calcular el porcentaje de beneficio
porcentaje_beneficio = np.random.uniform(0.14, 0.16)

# Generar datos de gastos
data_gastos = []
start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 12, 31)
categorias = ["servicios publicos", "compra de productos e insumos", "alquiler", "gastos administrativos", "publicidad", "transporte", "mantenimiento", "muebles, equipos o maquinaria", "otros"]
nombres_gasto = ["gasto 1", "gasto 2", "gasto 3", "gasto 4", "gasto 5"]

for idGasto in range(501):
    fecha = (start_date + timedelta(days=randint(0, (end_date - start_date).days))).strftime('%d/%m/%Y')
    categoria = choice(categorias)
    valor_mes = ingresos_por_mes.sample().values[0] * porcentaje_beneficio
    valorGasto = round(np.random.uniform(0.5, 1.5) * valor_mes)  # Ajustar según porcentaje de beneficio
    nombreGasto = choice(nombres_gasto)
    metodoPago = choice(["efectivo", "tarjeta de debito", "tarjeta de credito", "codigo QR", "transferencia", "otro"])
    usuario = f"usuario {randint(1, 2)}"
    
    data_gastos.append([idGasto, fecha, categoria, valorGasto, nombreGasto, metodoPago, usuario])

# Crear DataFrame de gastos
df_gastos = pd.DataFrame(data_gastos, columns=['idGasto', 'fecha', 'categoria', 'valorGasto', 'nombreGasto', 'metodoPago', 'usuario'])

# Guardar como CSV
df_gastos.to_csv('gastos_digidata.csv', index=False)

print("Archivo de gastos generado y guardado como 'gastos_digidata.csv'")
