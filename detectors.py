import torch
import cv2
import numpy as np

# Carregar o modelo YOLOv5 pré-treinado
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_car(frame):
    # Obter as dimensões da imagem
    height, width = frame.shape[:2]

    # Criar uma máscara circular para manter o centro focado e desfocar as bordas
    mask = np.zeros((height, width), dtype=np.uint8)
    center = (width // 2, height // 2)  # Centro da imagem
    radius = int(min(width, height) * 0.3)  # Definir o raio do centro focado
    cv2.circle(mask, center, radius, (255, 255, 255), thickness=-1)

    # Desfocar a imagem inteira
    blurred_frame = cv2.GaussianBlur(frame, (21, 21), 0)

    # Aplicar a máscara: combinar o centro focado com as bordas desfocadas
    focused_frame = np.where(mask[:, :, np.newaxis] == 255, frame, blurred_frame)

    results = model(frame)

    # Filtrar detecções para mostrar apenas carros
    car_detections = results.pandas().xyxy[0]
    car_detections = car_detections[car_detections['class'] == 2]

    # Se houver carros detectados, renderizar a imagem
    if not car_detections.empty:
        results.render()
        cv2.imshow('Detecção de Carros', results.ims[0])
        print('para')
    else:
        cv2.imshow('Detecção de Carros', frame)