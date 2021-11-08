import cv2 as cv
import numpy as np
from numpy.lib.type_check import imag

image_color = cv.imread("taeri.png", cv.IMREAD_COLOR)
image_color = cv.cvtColor(image_color, cv.COLOR_BGR2LAB)
#img_result = image_color.copy()

height,width = image_color.shape[:2] #이미지를 저장할 넘파이 배열 생성

#피부색 이미지를 저장할 넘파이 배열을 생성
##img_skincolor = np.zeros((height, width), np.uint8)

#픽셀 접근방법: for 루프를 돌면서 (x,y)에 있는 픽셀을 하나씩 접근한다.
for y in range(0, height):
   for x in range(0, width):
      
    #컬러이미지의 (x,y)픽셀에 있는 픽셀의 l,a,b채널을 읽는다
    l = image_color.item(y,x,0)
    a = round(image_color.item(y,x,1), 2)
    b = image_color.item(y,x,2)
    print('l=', round(l*100/255, 2), ' a=', a-128, ' b=', b-128)
    ##lab= int(l+a+b)
    ##img_skincolor.itemset(y,x,lab)

#img_result = cv.cvtColor(img_skincolor, cv.COLOR_LAB2BGR)

cv.imshow('color', image_color)
##cv.imshow('result', img_skincolor)
#print("pixel value of (x,y,lab) \n", image_color[y,x])
##print('b=', b, ' g=', g, ' r=', r)

cv.waitKey(0)
cv.destroyAllWindows()