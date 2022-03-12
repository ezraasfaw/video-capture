import cv2

# region Read image from default webcam using OpenCV convert to grayscale and then apply a colormap before displaying.
video_capture = cv2.VideoCapture(2, cv2.CAP_DSHOW)
while True:
    return_code, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)
    colormapped = cv2.applyColorMap(equ, cv2.COLORMAP_JET)
    cv2.imshow(‘Output’, frame)
    if cv2.waitKey(1) & 0xFF == ord(‘q’):
        break
# endregion

# region Release the camera resources.
video_capture.release()
cv2.destroyAllWindows()
# endregion
