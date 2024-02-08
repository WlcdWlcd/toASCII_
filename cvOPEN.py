import cv2 as cv

def open_image(path,is_show=False,display_title = "cv2"):
    img = cv.imread(path)
    if is_show:
        cv.imshow(display_title,img)

    return img