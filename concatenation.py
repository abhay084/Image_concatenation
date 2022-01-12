import numpy as np
import cv2

img1 = cv2.imread('naruto.jpg')
img2 = cv2.imread('sasuke.jpg')

print(img1.shape)
print(img2.shape)

window_name='naruto'
cv2.imshow(window_name,img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

window_name = 'sasuke'
cv2.imshow(window_name,img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

new_img1 = cv2.vconcat([img1,img2])
cv2.imwrite('ver-concat.jpg',new_img1)

new_img2 = cv2.hconcat([img1,img2])
cv2.imwrite('hori_concat.jpg',new_img2)

b = img1[0:1920,0:960]
window_name = 'naruto_cropped'
cv2.imshow(window_name,b)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(b.shape)

c = img2[0:1080,960:1920]
window_name='sasuke_cropped'
cv2.imshow(window_name,c)
cv2.waitKey(0)
cv2.destroyAllWindows()


print(c.shape)

new = cv2.hconcat([b,c])
cv2.imwrite('new.jpg',new)
