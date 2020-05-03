#from image import get_image
import cv2
import numpy as np
from random import sample

#images=get_image()
images = []
images.append(cv2.imread("gallery/c_im.jpg"))
images.append(cv2.imread("gallery/im1.jpg"))
images.append(cv2.imread("gallery/im2.jpeg"))
images.append(cv2.imread("gallery/im3.jpg"))

for i in range(4):
    images[i] = cv2.cvtColor(images[i], cv2.COLOR_RGB2GRAY)
    images[i] = cv2.resize(images[i], (512, 512))



mo = []
mo.append(images[0]/images[1])
mo.append(images[0]/images[2])
mo.append(images[0]/images[3])

 print(len)
y_arr = np.zeros((512, 512))
im_mat = np.zeros((512, 512))
mo1 = np.zeros((512, 512, 3))

l=[0,1,2]
print(mo[3][0])
for i in range(512):
    for j in range(512):
        y = sample(l, 3)
        y_arr[i, j] = y[0]*100 + y[1]*10  + y[2]
        #print(i, j)
        #print(mo[i][j][y[0]])
        mo1[i, j, 0] = np.round(mo[i][j][y[0]], 2)*100
        mo1[i, j, 1] = np.round(mo[i][j][y[1]], 2)*100
        mo1[i, j, 2] = np.round(mo[i][j][y[2]], 2)*100
        im_mat[i, j] = ((mo1[i, j, 0]*1000) + mo1[i, j, 1]*1000) + mo1[i, j, 2]


maxx = max(im_mat)
maxx2 = max(max)
print(max)