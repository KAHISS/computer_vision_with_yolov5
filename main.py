from webcam import WebCam
from detectors import model, detect_car # importe só o modelo e as funções que vai usar

a = WebCam('data/walking.mp4', model)
a.callWebcam(lambda: detect_car(a.frame), False)
