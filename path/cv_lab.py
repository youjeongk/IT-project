import cv2

BGR_img = cv2.imread("koreanflag.jpg", cv2.IMREAD_COLOR) #컬러 영상 읽기
if BGR_img is None: raise Exception("영상파일 읽기 오류")

Gray_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2GRAY)
LAB_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2LAB) #La*b*컬러 공간 변환

Lab_ch = cv2.split(LAB_img) #채널 분리

sp3 = ['L', 'A', 'B']

for i in range(3):
  cv2.imshow("LAB_img[%d]-%s" %(i, sp3[i]), Lab_ch[i])
cv2.waitKey(0)