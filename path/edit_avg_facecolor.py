import cv2 as cv
import numpy as np
from numpy.lib.type_check import imag

while True:

  image_color = cv.imread("me1.png", cv.IMREAD_COLOR)
  image_color = cv.cvtColor(image_color, cv.COLOR_BGR2LAB)
  img_result = image_color.copy()

  height,width = image_color.shape[:2] #이미지를 저장할 넘파이 배열 생성

  #피부색 이미지를 저장할 넘파이 배열을 생성
  img_skincolor = np.zeros((height, width), np.uint8)

#픽셀 접근방법: for 루프를 돌면서 (x,y)에 있는 픽셀을 하나씩 접근한다.
  for y in range(0, height):
    for x in range(0, width):
      
      #컬러이미지의 (x,y)픽셀에 있는 픽셀의 l,a,b채널을 읽는다
      l = image_color.item(y,x,0)
      a = image_color.item(y,x,1)
      b = image_color.item(y,x,2)
      
      print("pixel value of (x,y,lab) \n", image_color[y,x])
      print('l=', l, ' a=', a, ' b=', b)

      #검정색을 뺀 살색부위 (l=0인 픽셀을 뺀 나머지 픽셀의 평균색구하기, a, b값으로 웜쿨을 판별하기.)
#픽셀에 접근하여 살색을 추출한 후 평균살색을 하나만든다. 그리고 그 값의 lab값을 각각 구해서 웜쿨 판별. 

  center_x = int(width*0.5)
  center_y = int(height*0.5)
  #ROI 영역을 빨간색으로 표시한다
  cv.rectangle(img_result, (center_x-180, center_y-50),
  (center_x+180, center_y+10), (0,0,255),3)

  #필요 영역을 구해서 평균을 구한다.
  img_roi = image_color[center_y-50:center_y+10,center_x-180:center_x+180]
  #skin_area = image_color
  #mask1 = np.zeros(img_result.shape, np.uint8)
  m = cv.mean(img_roi) ##
  #m = cv.mean(np.float32(img_roi)) ##

  #살색 픽셀에 대한 평균 픽셀값으로 채운 이미지를 생성한다. #영역을 roi로 해야 에러 미발생
  img_mean = np.zeros(img_roi.shape, dtype=np.uint8)
  #img_mean = np.zeros(image_color.shape, dtype=np.uint8)
  img_mean[:] = (m[0], m[1], m[2])
  #cv.imshow('mean', img_mean)
  #cv.imshow('color', img_result)
  #cv.imshow('roi', img_roi)
  #결과 이미지에 LAB를 표시하기 위해 LAB 이미지로 변환한다.

  key = cv.waitKey(1)
  if key==27:
    break