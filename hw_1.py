# -*- coding: utf-8 -*-
"""HW_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i5lDRithCpKk03GUVqaDBMH6SbJl1nxg

**Note:** We use plt.imshow function instead of cv2.imshow because cv2.imshow is disabled from colab. If you want to see good results check images which are written by cv2.imwrite function
"""

import cv2
import numpy as np
import math

!wget -O image.png https://raw.githubusercontent.com/ozgunsungar/Corner-Edge_Detection/main/image.png

image = cv2.imread("image.png",0)

h,w = image.shape
print(h,w)

"""## flips image vertically"""

image_copy = np.copy(image)
row = 0
for i in range(h-1,-1,-1):
  image_copy[row,:] = image[i,:]
  row+=1

cv2.imwrite("vertical_flips.png",image_copy)

plt.figure(figsize = (12, 9))
plt.axis('off')
plt.imshow(image_copy,cmap='gray', vmin=0, vmax=255) 
plt.show()



"""## flips image horizontally"""

image_copy = np.copy(image)
col = 0
for i in range(w-1,-1,-1):
  image_copy[:,col] = image[:,i]
  col+=1

cv2.imwrite("horizontal_flips.png",image_copy)

plt.figure(figsize = (12, 9))
plt.axis('off')
plt.imshow(image_copy,cmap='gray', vmin=0, vmax=255)  
plt.show()

"""## rotates the image 90 deg counterclockwise"""

img_zeros = np.zeros((w,h))
row = 0
for i in range(0,w):
  img_zeros[row,:] = image[:,-i]
  row+=1
img_counterclockwise = np.copy(img_zeros)
cv2.imwrite("image_counterclockwise.png",img_counterclockwise)

plt.figure(figsize = (9, 12))
plt.axis('off')
plt.imshow(img_counterclockwise,cmap='gray', vmin=0, vmax=255)  
plt.show()

"""## rotates the image 90 deg clockwise

"""

img_zeros = np.zeros((w,h))
col = 0
for i in range(0,h-1):
  img_zeros[:,col] = image[-i,:]
  col+=1
img_clockwise = np.copy(img_zeros)
cv2.imwrite("image_clockwise.png",img_clockwise)

plt.figure(figsize = (9, 12))
plt.axis('off')
plt.imshow(img_clockwise,cmap='gray', vmin=0, vmax=255)  
plt.show()

"""## resizes the image to the half by keeping the aspect ratio

"""

rezied_image = image[0::2,0::2]
cv2.imwrite("rezied_image.png",rezied_image)
print(image.shape)
print(rezied_image.shape)

plt.figure(figsize = (12, 9))
plt.axis('off')
plt.imshow(rezied_image,cmap='gray', vmin=0, vmax=255)  
plt.show()

"""## applies negative transformation on the image"""

negative_image = np.ones((h,w))*255
negative_image = negative_image-image

cv2.imwrite("negative_image.png",negative_image)

plt.figure(figsize = (12, 9))
plt.axis('off')
plt.imshow(negative_image,cmap='gray', vmin=0, vmax=255)  
plt.show()

"""## applies gamma transformation on the image"""

# compute gamma = log(mid*255)/log(mean)
mid = 0.4
mean = np.mean(image)
gamma = math.log(mid*255)/math.log(mean)

# do gamma correction
image_gamma = np.power(image, gamma).clip(0,255).astype(np.uint8)
cv2.imwrite("image_gamma.png",image_gamma)

plt.figure(figsize = (12, 9))
plt.axis('off')
plt.imshow(image_gamma,cmap='gray', vmin=0, vmax=255)  
plt.show()

"""## computes the histogram of the image"""

control_histogram = [*range(0,256)]
indexes = control_histogram.copy()

h,w = image.shape

for i in range(0,h):
  for j in range(0,w):
    pixel_value = image[i,j]
    control_histogram[pixel_value]+=1

import matplotlib.pyplot as plt
index = 0
fig = plt.figure(figsize = (10, 7))
plt.plot(indexes, control_histogram)
plt.xlabel("0-255 pixel value")
plt.ylabel("Count")
plt.title("Histogram chart")

plt.show()

