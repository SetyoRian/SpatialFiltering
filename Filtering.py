import cv2
from matplotlib import pyplot as plt

img = cv2.imread('brrr.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

blur = cv2.blur(img, (9, 9))
gauss = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 3)

plt.subplot(221), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur), plt.title('Mean')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(gauss), plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(median), plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.show()
