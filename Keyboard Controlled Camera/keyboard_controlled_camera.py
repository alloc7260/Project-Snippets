from imutils.video import WebcamVideoStream
import cv2
import keyboard

def read():
    while 1:
        frame = vs.read()
        cv2.imshow("Video", frame)
        cv2.waitKey(1)
        if keyboard.is_pressed('c'): cv2.destroyAllWindows() ; break                # capture and show
        if keyboard.is_pressed('q'): vs.stop(); cv2.destroyAllWindows(); quit()     # quit
    while 1:
        cv2.imshow("Video", frame)
        cv2.waitKey(1)
        if keyboard.is_pressed('r'): cv2.destroyAllWindows() ; break                # resume streaming
        if keyboard.is_pressed('q'): vs.stop(); cv2.destroyAllWindows(); quit()     # quit
    read()


# vs = WebcamVideoStream("http://192.168.43.1:8080/video").start()

vs = WebcamVideoStream(0).start()

read()