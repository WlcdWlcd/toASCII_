import cv2 as cv

class Cv():
    def __init__(self):
        pass

    def render_cv2(self):
        #сначала высота, затем ширина
        # for i in range(1,250):
        #     resized_cv2_image = cv.resize(self.cv2_image[300-i:300+i,250-i:250+i], (500, 500), interpolation=cv.INTER_AREA)
        #     # cv.imshow('img', self.cv2_image)
        #     cv.imshow('img', resized_cv2_image)
        #     cv.waitKey(1)
        # for i in range(250,1,-1):
        #     resized_cv2_image = cv.resize(self.cv2_image[300-i:300+i,250-i:250+i], (500, 500), interpolation=cv.INTER_AREA)
        #     # cv.imshow('img', self.cv2_image)
        #     cv.imshow('img', resized_cv2_image)
        #     cv.waitKey(1)
        #     resized_cv2_image = cv.resize(self.cv2_image, (500, 500),interpolation=cv.INTER_AREA)
            cv.imshow('img', self.cv2_image[0:20,0:20])

            print(self.cv2_image[0][0])
            # cv.imshow('img', resized_cv2_image)
            cv.waitKey(1)


    def open_image(self,path):
        self.set_path(path)
        self.createImage()

    def set_path(self,path):
        self.path = path

    def createImage(self):
        self.cv2_image = cv.imread(self.path)
        print(self.cv2_image.shape)
        # print(self.cv2_image)
