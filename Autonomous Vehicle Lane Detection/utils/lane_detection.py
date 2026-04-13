import cv2
import numpy as np
import config

def hough_lines(img):
    return cv2.HoughLinesP(
        img,
        config.RHO,
        config.THETA,
        config.THRESHOLD,
        np.array([]),
        minLineLength=config.MIN_LINE_LENGTH,
        maxLineGap=config.MAX_LINE_GAP
    )

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []

    if lines is None:
        return None

    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)

        if x1 == x2:
            continue

        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - slope * x1

        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))

    left_avg = np.average(left_fit, axis=0) if left_fit else None
    right_avg = np.average(right_fit, axis=0) if right_fit else None

    return left_avg, right_avg

def make_coordinates(image, line_params):
    slope, intercept = line_params

    y1 = image.shape[0]
    y2 = int(y1 * 0.6)

    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)

    return np.array([x1, y1, x2, y2])

def get_lane_lines(image, lines):
    averaged = average_slope_intercept(image, lines)

    if averaged is None:
        return None

    left, right = averaged
    line_image = []

    if left is not None:
        line_image.append(make_coordinates(image, left))

    if right is not None:
        line_image.append(make_coordinates(image, right))

    return np.array(line_image)