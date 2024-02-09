import cv2 as cv

from CV import Cv
from asciirenderer import AsciiRenderer









class Main(Cv,AsciiRenderer):

    def __init__(self,is_cv2show=True):
        self.is_cv2show = is_cv2show
        self.ascii_renderer = AsciiRenderer()

    def render(self):
        self.render_cv2()
        resized_cv2_image = cv.resize(self.cv2_image, (290, 150),interpolation=cv.INTER_AREA)
        self.ascii_renderer.render_ascii(resized_cv2_image)



    def run(self):
        while True:
            self.render()
            break




if __name__ == '__main__':
    app = Main()
    app.open_image("images/5.jpg")
    app.run()