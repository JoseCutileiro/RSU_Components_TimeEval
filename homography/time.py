import math
import time
import random

def xy_to_latlon(X, Y, lat0_deg, lon0_deg):
    R = 6371000.0
    lat0 = math.radians(lat0_deg)
    lon0 = math.radians(lon0_deg)

    lat = Y / R + lat0
    lon = X / (R * math.cos(lat0)) + lon0

    lat_deg = math.degrees(lat)
    lon_deg = math.degrees(lon)
    return lat_deg, lon_deg

# Gerar 1000 pontos (X, Y) aleatórios
num_pontos = 10000
lat0 = 38.7169  # exemplo: Lisboa
lon0 = -9.1399

pontos = [(random.uniform(-1000, 1000), random.uniform(-1000, 1000)) for _ in range(num_pontos)]

# Medir o tempo
start_time = time.time()

for X, Y in pontos:
    xy_to_latlon(X, Y, lat0, lon0)

end_time = time.time()

tempo_total = end_time - start_time
tempo_medio = tempo_total / num_pontos

print(f"Tempo total para {num_pontos} conversões: {tempo_total:.6f} segundos")
print(f"Tempo médio por ponto: {tempo_medio:.9f} segundos")
