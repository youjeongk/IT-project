import cv2
import dlib
import matplotlib.pyplot as plt

# 얼굴 검출기와 랜드마크 검출기 생성 --- ①
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

img = cv2.imread("iu.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 얼굴 영역 검출 --- ②
faces = detector(gray)

#얼굴영역 추출 후 사진 저장
for f in faces:
  crop = img[f.top():f.bottom(), f.left():f.right()]
cv2.imwrite("cropped.jpg", crop)