import cv2
import numpy as np

# Load the image
img = cv2.imread('data/pictures/tp/7.jpg')
# print(img.shape)

image_center_y = img.shape[0] // 2
image_center_x = img.shape[1] // 2
# print(image_center_y, image_center_x)s
cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Define the region of interest (x, y, w, h)
xywh = input()
# print(xywh)
# roi_x, roi_y, roi_w, roi_h = float(xywh[0]), float(xywh[1]), float(xywh[2]), float(xywh[3])

values = [int(x) for x in xywh[1:-1].split(",")]


roi_x, roi_y, roi_w, roi_h = values
#print(roi_x, roi_y, roi_w, roi_h)

# Get the center color of the ROI
roi = img[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w]
# cv2.imshow("roi", roi)
center_x = roi_x + roi_w // 2
center_y = roi_y + roi_h // 2

print(center_x, center_y)
center_color = img[roi_y+ roi_h // 2, roi_x+roi_w //2, :]
# print(center_color.dtype)
# print(center_color)
# print(tuple(center_color))
# Display the RGB value of the center color in the upper left corner of the screen
cv2.putText(img, f"RGB: {(int(center_color[0]), int(center_color[1]), int(center_color[2]))}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (int(center_color[0]), int(center_color[1]), int(center_color[2])), 2)
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Draw a half-radius circle using the center color
center_color = (center_color[0], center_color[1], center_color[2])
# print(center_color[0].dtype(), center_color[1], center_color[2])
print(list(center_color))

print(center_color[0].dtype)
print(center_color[0])
radius = 50
cv2.circle(img, (image_center_x, image_center_y), radius, color = (int(center_color[0]), int(center_color[1]), int(center_color[2])), thickness=-1)
# Display the output image
cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()