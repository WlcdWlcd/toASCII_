class Avgs():
    def __init__(self):
        pass

    def avgPixelLight(self, pixel):
        return sum(pixel)//len(pixel)

    def avgSliceLight(self, slice):
        shape = slice.shape
        size = shape[0]*shape[1]
        pixelSum = 0
        for i in slice:
            for j in i:
                pixelSum+=self.avgPixelLight(j)
        return pixelSum//size