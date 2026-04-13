import cv2
import numpy as np
import config

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def gaussian_blur(img):
    return cv2.GaussianBlur(img, (config.KERNEL_SIZE, config.KERNEL_SIZE), 0)

def canny(img):
    return cv2.Canny(img, config.LOW_THRESHOLD, config.HIGH_THRESHOLD)

def region_of_interest(img):
    height = img.shape[0]
    width = img.shape[1]

    polygons = np.array([[
        (0, height),
        (width, height),
        (width//2, int(height*0.6))
    ]])

    mask = np.zeros_like(img)
    cv2.fillPoly(mask, polygons, 255)

    return cv2.bitwise_and(img, mask)
