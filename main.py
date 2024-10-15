from webcam import WebCam
from detectors import model, detect_car # importe só o modelo e as funções que vai usar

a = WebCam(0, model)
a.callWebcam(lambda: detect_car(2, a.frame), False)
