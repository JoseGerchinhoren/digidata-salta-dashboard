import pandas as pd
import numpy as np
from random import randint, choice

# Leer el archivo de Excel
df = pd.read_excel('Finanzas DigiData Salta - ficticio.xlsx')

# Reemplazar la columna 'País' por 'sucursal', cambiando 'Chile' por 'Argentina'
df.rename(columns={'País': 'sucursal'}, inplace=True)
df['sucursal'] = df['sucursal'].apply(lambda x: "Argentina" if x == "Chile" else f"{x}")

# Procesar para ingresos
ingresos_data = []
for i, row in enumerate(df.itertuples(), start=0):
    idIngreso = i
    fecha = row.Fecha
    hora = '{:02d}:{:02d}'.format(randint(9, 22), randint(0, 59))
    sucursal = row.sucursal
    producto = f"producto {randint(1, 10)}"
    ingreso = row.Ingresos
    metodoPago = choice(["efectivo", "tarjeta de debito", "tarjeta de credito", "codigo QR", "transferencia", "otro"])
    usuario = f"usuario {randint(1, 5)}"
    
    ingresos_data.append([idIngreso, fecha, hora, sucursal, producto, ingreso, metodoPago, usuario])

# Crear DataFrame de ingresos
df_ingresos = pd.DataFrame(ingresos_data, columns=['idIngreso', 'fecha', 'hora', 'sucursal', 'producto', 'ingreso', 'metodoPago', 'usuario'])

# Guardar ingresos como CSV
df_ingresos.to_csv('ingresos_digiData.csv', index=False)

print("Archivo de ingresos generado y guardado como 'ingresos_digiData.csv'")

# Procesar para gastos
gastos_data = []
for i, row in enumerate(df.itertuples(), start=0):
    idGasto = i
    fecha = row.Fecha
    sucursal = row.sucursal
    categoria = choice(["servicios publicos", "compra de productos e insumos", "alquiler", "gastos administrativos", "publicidad", "transporte", "mantenimiento", "muebles, equipos o maquinaria", "otros"])
    gasto = row.Gastos
    nombreGasto = f"gasto {randint(1, 5)}"
    metodoPago = choice(["efectivo", "tarjeta de debito", "tarjeta de credito", "codigo QR", "transferencia", "otro"])
    usuario = f"usuario {randint(1, 5)}"
    
    gastos_data.append([idGasto, fecha, sucursal, categoria, gasto, nombreGasto, metodoPago, usuario])

# Crear DataFrame de gastos
df_gastos = pd.DataFrame(gastos_data, columns=['idGasto', 'fecha', 'sucursal', 'categoria', 'gasto', 'nombreGasto', 'metodoPago', 'usuario'])

# Guardar gastos como CSV
df_gastos.to_csv('gastos_digiData.csv', index=False)

print("Archivo de gastos generado y guardado como 'gastos_digiData.csv'")
