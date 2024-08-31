"""
Module OpenCV
Course: Computer Vision
"""

import cv2
import numpy as np

# Reading and Displaying Images
image = cv2.imread('image.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # Reading and Displaying Videos
# video = cv2.VideoCapture('video.mp4') # 0 for webcam - 1, 2, 3 for external cameras - 'video.mp4' for video files

# while True:
#     ret, frame = video.read()
#     cv2.imshow('Video', frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# video.release()
# cv2.destroyAllWindows()

# # Drawing on Images
# image = cv2.imread('image.jpg')
# cv2.line(image, (0, 0), (100, 100), (255, 0, 0), 5)
# cv2.rectangle(image, (100, 100), (200, 200), (0, 255, 0), 3)
# cv2.circle(image, (300, 300), 50, (0, 0, 255), -1)
# cv2.putText(image, 'OpenCV', (350, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Image Processing
# image = cv2.imread('image.jpg')
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
# canny_edges = cv2.Canny(image, 100, 200)
# cv2.imshow('Gray Image', gray_image)
# cv2.imshow('Blurred Image', blurred_image)
# cv2.imshow('Canny Edges', canny_edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Contour Detection
# image = cv2.imread('image.jpg')
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _, threshold = cv2.threshold(gray_image, 127, 255, 0)
# contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Image Segmentation
# image = cv2.imread('image.jpg')
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _, threshold = cv2.threshold(gray_image, 127, 255, 0)
# contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# for i in range(len(contours)):
#     cv2.drawContours(image, contours, i, (0, 255, 0), 3)

# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Image Filtering
# image = cv2.imread('image.jpg')
# kernel = np.ones((5, 5), np.float32)/25
# filtered_image = cv2.filter2D(image, -1, kernel)
# cv2.imshow('Image', image)
# cv2.imshow('Filtered Image', filtered_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Image Transformation
# image = cv2.imread('image.jpg')
# rows, cols, _ = image.shape
# translation_matrix = np.float32([[1, 0, 50], [0, 1, 50]])
# translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
# cv2.imshow('Image', image)
# cv2.imshow('Translated Image', translated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
