import numpy as np
import cv2

def imageToBw(image):
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return imageGray
def showImage(image):
    cv2.imwrite("test.png",image)
    