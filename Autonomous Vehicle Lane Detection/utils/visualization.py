import cv2
import numpy as np

def draw_lines(image, lines):
    line_image = np.zeros_like(image)

    if lines is not None:
        for x1, y1, x2, y2 in lines:
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)

    return line_image

def overlay(image, line_image):
    return cv2.addWeighted(image, 0.8, line_image, 1, 1)