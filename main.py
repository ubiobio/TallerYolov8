from ultralytics import YOLO

# Se carga el modelo
model = YOLO("yolov8n.yaml")  # Se crear un nuevo modelo con Yolo nano

# Use the model
model.train(data="config.yaml", epochs=3)  # Se entrena el modelo por 3 ciclos