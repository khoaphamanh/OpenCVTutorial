import cv2
import matplotlib.pyplot as plt

# open webcam
cap = cv2.VideoCapture(0)

while True:
    # read the webcam
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    print("ret:", ret)
    # shape of the webcam
    print("frame:", frame.shape)

    # webcam as a window
    cv2.imshow("Your webcam", frame)

    # cv2.waitKey(1) for 1 milisecond for a key event, if q pressed, break the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
