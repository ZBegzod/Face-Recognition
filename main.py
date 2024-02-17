import cv2 as cv

# img = cv.imread('C:\\Users\\user\\Desktop\\img.jpg', flags=cv.IMREAD_GRAYSCALE)
# img = cv.resize(img, (800, 500))
# cv.imshow('Cat', img)

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([250, 250], [200, 400], 'c')
# plt.show()

# cv.waitKey(0)
# cv.destroyAllWindows()
# capture = cv.VideoCapture(1)

# while True:
#     ret, frame = capture.read()
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#
#     cv.imshow('frame', frame)
#     cv.imshow('frame', gray)
#
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# capture.release()
# cv.destroyAllWindows()


capture = cv.VideoCapture(0)
while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    img = cv.circle(frame, (width // 2, height // 2), 60, (0, 0, 255), 1)
    cv.line(frame, (320, 200), (320, 290), (0, 0, 0), 1)
    cv.line(frame, (275, 245), (360, 245), (0, 0, 0), 1)

    cv.imshow('frame', img)

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
