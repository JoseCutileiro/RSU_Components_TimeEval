import os
import time
from ultralytics import YOLO
from pathlib import Path
from PIL import Image

BASE_PATH = 'C:\\Users\\35196\\Downloads\\MOT15\\MOT15' 
SECTIONS = ['train', 'test']
BATCH_SIZE = 16

model = YOLO('models/yolo11x.pt').to('cuda')

tempos = []
total_frames = 0

for section in SECTIONS:
    section_path = Path(BASE_PATH) / section

    for sequence in section_path.iterdir():
        img_folder = sequence / 'img1'
        if not img_folder.exists():
            continue

        print(f"Processando: {sequence}")

        img_files = sorted(img_folder.glob("*.jpg"))
        for i in range(0, len(img_files), BATCH_SIZE):
            batch_files = img_files[i:i + BATCH_SIZE]
            imgs = [Image.open(f) for f in batch_files]

            start_time = time.time()
            _ = model.predict(imgs, verbose=False)
            end_time = time.time()

            batch_time = end_time - start_time
            tempos.append(batch_time)
            total_frames += len(batch_files)

# Cálculo estatístico
tempo_total = sum(tempos)
tempo_medio = tempo_total / total_frames if total_frames else 0

print("\nRESULTADOS:")
print(f"Total de frames: {total_frames}")
print(f"Tempo total: {tempo_total:.4f} s")
print(f"Tempo médio por frame: {tempo_medio:.6f} s")
