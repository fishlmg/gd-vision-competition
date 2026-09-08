import cv2
import numpy as np

# Load the original image
img = cv2.imread('t1.png')

# Prompt user to input the number of rows and columns
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Calculate the height and width of each sub-image
sub_img_height, sub_img_width = img.shape[0] // rows, img.shape[1] // cols

# Loop through each row and column to extract small rectangles
for i in range(rows):
    for j in range(cols):
        top_left_y, top_left_x, bottom_right_y, bottom_right_x = i * sub_img_height, j * sub_img_width, (i + 1) * sub_img_height, (j + 1) * sub_img_width

        region = img[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

        cv2.imwrite(f'region_{i}_{j}.jpg', region)