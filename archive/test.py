import cv2
import numpy as np

# Load the image
img = cv2.imread('color.jpg')

# Define the region of interest (x, y, w, h)
roi_x, roi_y, roi_w, roi_h = 100, 100, 200, 200

# Calculate the center point coordinates within the ROI
center_x = roi_x + roi_w // 2
center_y = roi_y + roi_h // 2

# Extract the color of the center point
center_color = img[center_y, center_x]

print(f"Center Color: RGB({center_color[0]}, {center_color[1]}, {center_color[2]})")

# Display the RGB values in the top-left corner of the screen
cv2.putText(img, f"RGB({center_color[0]}, {center_color[1]}, {center_color[2]})", (10, 20),
cv2.FONT_HERSHEY_SIMPLEX, 0.5, center_color)

# Draw a filled circle with a radius of 50 at the center of the image
cv2.circle(img, (center_x, center_y), 50, tuple(center_color), -1)

# Display the output image
cv2.imshow('Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()