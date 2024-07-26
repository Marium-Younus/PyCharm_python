
import cv2


image = cv2.imread('kidimage.jpg')
im_original= cv2.resize(image, (800, 800))
cv2.imshow('Original Image', im_original)

cv2.waitKey(0)

# Gaussian Blur
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
im_gauss = cv2.resize(Gaussian, (800, 800))
cv2.imshow('Gaussian Blurring', im_gauss)
cv2.waitKey(0)

# # Median Blur
median = cv2.medianBlur(image, 5)
im_median = cv2.resize(median, (800, 800))
cv2.imshow('Median Blurring', im_median)
cv2.waitKey(0)
#
# # Bilateral Blur
# bilateral = cv2.bilateralFilter(image, 9, 75, 75)
# im_bilateral  = cv2.resize(bilateral, (800, 800))
# cv2.imshow('Bilateral Blurring', im_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows() 