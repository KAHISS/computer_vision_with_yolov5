import cv2


class WebCam(cv2.VideoCapture):
    def __init__(self, webcam, model):
        super().__init__(webcam)
        self.validation, self.frame = self.read()
        self.model = model

    def callWebcam(self, function, imshow=True):
        while self.validation:
            self.validation, self.frame = self.read()
            function()
            if imshow:
                cv2.imshow("v", self.frame)
            key = cv2.waitKey(5)
            if key == 27:
                break
        self.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    a = WebCam(0, 'Haarcascade/haarcascade_lefteye_2splits.xml')