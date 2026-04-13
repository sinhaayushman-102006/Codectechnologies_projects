import cv2
from utils.image_processing import *
from utils.lane_detection import *
from utils.visualization import *

def process_frame(frame):
    gray = grayscale(frame)
    blur = gaussian_blur(gray)
    edges = canny(blur)

    roi = region_of_interest(edges)

    lines = hough_lines(roi)
    lane_lines = get_lane_lines(frame, lines)

    line_image = draw_lines(frame, lane_lines)

    return overlay(frame, line_image)

# Load input video
cap = cv2.VideoCapture("test_videos/solidWhiteRight.mp4")

# Get video properties
width = int(cap.get(3))
height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 🎯 Define output video writer
out = cv2.VideoWriter(
    "output/output_video.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    output = process_frame(frame)

    # Show
    cv2.imshow("Lane Detection", output)

    # ✅ Save frame
    out.write(output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()   # IMPORTANT
cv2.destroyAllWindows()