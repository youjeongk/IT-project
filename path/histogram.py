import numpy as np, cv2

def calc_histo(image, histSize, ranges=[0,256]): #행렬 원소의 1차원 히스토그램 계산
  hist = np.zeros((histSize, 1), np.uint8) #히스토그램 누적 행렬 /문제의 줄. 'list' object cannot be interpreted as an integer
  gap = ranges[1] / histSize                 #계급 간격

  for row in image:                          #2차원 행렬 순회 방식
    for pix in row:
      idx = int(pix/gap)
      hist[idx] += 1
  return hist 

image = cv2.imread("IU.png", cv2.IMREAD_GRAYSCALE) #images/pixel_test.jpg
if image is None: raise Exception("영상파일 읽기 오류")

histSize, ranges = [32], [0, 256]
gap = ranges[1]/histSize[0]
ranges_gap = np.arange(0, ranges[1]+1, gap)
hist1 = calc_histo(image, histSize, ranges)
hist2 = cv2.calcHist([image], [0], None, histSize, ranges)
hist3, bins = np.histogram(image, ranges_gap)

print("User 함수: \n", hist1.flatten())
print("OpenCV 함수: \n", hist2.flatten())
print("numpy 함수: \n", hist3)