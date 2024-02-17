import cv2 as cv


img = cv.imread('C:\\Users\\user\\Desktop\\15. Облака.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', imgGray)
cv.waitKey(0)

# capture = cv.VideoCapture(0)
# capture.set(3, 300)
# capture.set(4, 300)
# capture.set(10, 300)

# while True:
#     success, image = capture.read()
#     cv.imshow("Video", image)
#
#     if cv.waitKey(1) == ord('q'):
#         break

# capture.release()
