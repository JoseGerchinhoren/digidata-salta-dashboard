import pandas as pd
import numpy as np
from random import randint, choice
from datetime import datetime, timedelta

# Definir listas de productos y precios
productos_precios = {
    "producto 1": 1000,
    "producto 2": 2500,
    "producto 3": 1500,
    "producto 4": 3000,
    "producto 5": 2000,
    "producto 6": 3500,
    "producto 7": 1800,
    "producto 8": 2700,
    "producto 9": 2200,
    "producto 10": 4000
}

# Generar datos
data = []
start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 12, 31)
delta = end_date - start_date

for i in range(delta.days + 1):
    idVenta = i
    fecha = (start_date + timedelta(days=i)).strftime('%d/%m/%Y')
    hora = '{:02d}:{:02d}'.format(randint(9, 22), randint(0, 59))
    sucursal = f"sucursal {randint(1, 3)}"
    producto = f"producto {randint(1, 10)}"
    precioU = productos_precios[producto]
    cantidad = randint(1, 5)
    importe = precioU * cantidad
    metodoPago = choice(["efectivo", "tarjeta de debito", "tarjeta de credito", "codigo QR", "transferencia", "otro"])
    usuario = f"usuario {randint(1, 5)}"
    
    data.append([idVenta, fecha, hora, sucursal, producto, precioU, cantidad, importe, metodoPago, usuario])

# Crear DataFrame
df = pd.DataFrame(data, columns=['idVenta', 'fecha', 'hora', 'sucursal', 'producto', 'precioU', 'cantidad', 'importe', 'metodoPago', 'usuario'])

# Guardar como CSV
df.to_csv('dataset_ejemplo_digidata.csv', index=False)

print("Dataset creado y guardado como 'dataset_ejemplo_digidata.csv'")
