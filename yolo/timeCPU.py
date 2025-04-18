import os
import time
from ultralytics import YOLO
from pathlib import Path
from PIL import Image

BASE_PATH = 'C:\\Users\\35196\\Downloads\\MOT15\\MOT15' 
SECTIONS = ['train', 'test']

# Carrega o modelo YOLO
model = YOLO('models/yolo11n.pt')

# Guardar tempos e contagem de frames
tempos = []
total_frames = 0

for section in SECTIONS:
    section_path = Path(BASE_PATH) / section

    for sequence in section_path.iterdir():
        img_folder = sequence / 'img1'
        if not img_folder.exists():
            continue

        print(f"Processando: {sequence}")

        for img_file in sorted(img_folder.glob("*.jpg")):
            img = Image.open(img_file)

            start_time = time.time()
            _ = model.predict(img, verbose=False)
            end_time = time.time()

            tempos.append(end_time - start_time)
            total_frames += 1

# Cálculo estatístico
tempo_total = sum(tempos)
tempo_medio = tempo_total / total_frames if total_frames else 0

print("\nRESULTADOS:")
print(f"Total de frames: {total_frames}")
print(f"Tempo total: {tempo_total:.4f} s")
print(f"Tempo médio por frame: {tempo_medio:.6f} s")
