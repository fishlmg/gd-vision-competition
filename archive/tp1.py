import cv2
import numpy as np

# Load the original image
img = cv2.imread('tp1.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding (Otsu's method)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Detect edges using Canny edge detector
edges = cv2.Canny(thresh, 50, 200)

# Create an undirected graph (connected components) from the edges
components, _ = cv2.connectedComponents(edges)

# Perform segmentation by labeling each connected component
labels = np.zeros_like(img)
for i in range(1, components+1):
    labels[components == i] = cv2.getTickCount()

# Visualize the segmentation results
segm = np.zeros_like(img)
segm[labels > 0] = (255, 0, 0)  # Red color for segmented regions

cv2.imshow('Segmented Image', segm)
cv2.waitKey(0)
cv2.destroyAllWindows()