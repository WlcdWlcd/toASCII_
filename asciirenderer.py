from avgs import Avgs

class AsciiRenderer(Avgs):
    def __init__(self):
        self.chars = '   .",:;!~+-xmo*#W&8@'[::-1]
        self.ascii_coef = 255 / (len(self.chars) - 1)

    def sliceAsciis(self,image,slice_size):
        print(123)
        print(self.imageSize[0]-slice_size)
        for row in range(0,self.imageSize[0]-slice_size,slice_size):
            for column in range(0,self.imageSize[1]-slice_size,slice_size):
                light = self.avgSliceLight(image[row:row+slice_size,column:column+slice_size])
                self.printFragment(light)
            print()

    def printFragment(self,light):
        charsCount = len(self.chars)
        charindex =int( light//self.ascii_coef)
        # print(charindex, charsCount)
        letter = self.chars[charindex]
        print(letter,end='')

    def render_ascii(self,image,slice_size=8):
        shape = image.shape
        self.imageSize = shape[0:2]
        self.imageChannels = shape[2]
        print(self.imageSize,"image size")
        print(self.imageChannels,"image channels")
        self.sliceAsciis(image,slice_size = slice_size)