import cv2 as cv
import numpy as np

while True:

  image_color = cv.imread("me1.png", cv.IMREAD_COLOR) 
  img_result = image_color.copy()

  height,width = image_color.shape[:2] #이미지의 높이와 너비를 가져온다.
  center_x = int(width*0.5)
  center_y = int(height*0.5)

  #ROI 영역을 빨간색으로 표시한다
  cv.rectangle(img_result, (center_x-180, center_y-50),
  (center_x+180, center_y+10), (0,0,255),3)

  #ROI 영역을 구해서 평균을 구한다.
  img_roi = image_color[center_y-50:center_y+10,center_x-180:center_x+180]
  m = cv.mean(img_roi)

  #ROI에 대한 평군 픽셀값으로 채운 이미지를 생성한다. #영역을 roi로 해야 에러 미발생
  img_mean = np.zeros(img_roi.shape, dtype=np.uint8) #평균색 이미지를 저장할 넘파이 배열을 생성한다

  #img_mean = np.zeros(image_color.shape, dtype=np.uint8)
  img_mean[:] = (m[0], m[1], m[2])
  cv.imshow('mean', img_mean)
  cv.imshow('color', img_result)
  cv.imshow('roi', img_roi)

  cv.imwrite('avgroi_facecolor.jpg', img_mean)

  key = cv.waitKey(1)
  if key==27:
    break