# data/parqueos.py
from datetime import datetime

parqueos = []

# ZONA 1 (contados en columnas hacia abajo)
zona1_config = [33, 33, 33, 33]  # 6 columnas
id_actual = 1
for col, cantidad in enumerate(zona1_config):
    for _ in range(cantidad):
        parqueos.append({
            'id': id_actual,
            'zona': 'A',
            'subzona': f'col-{col+1}',
            'estado': 'available',
            'hora_inicio_ocupado': None
        })
        id_actual += 1

# ZONA 2 (contados en filas hacia la derecha)
zona2_config = [7, 7, 7, 7, 7, 7]  # 6 filas
for fila, cantidad in enumerate(zona2_config):
    for _ in range(cantidad):
        parqueos.append({
            'id': id_actual,
            'zona': 'B',
            'subzona': f'fila-{fila+1}',
            'estado': 'available',
            'hora_inicio_ocupado': None
        })
        id_actual += 1