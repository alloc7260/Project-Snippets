import cv2

def show_webcam(mirror=0):
    """
    Simply display the contents of the webcam with optional mirroring using OpenCV via the new Pythonic cv2 interface.
    """
    #cam = cv2.VideoCapture("http://192.168.155.29:8080/video")
    cam = cv2.VideoCapture(0)
    while 1:
        ret, img = cam.read()
        if mirror: img = cv2.flip(img, 1) # flip vertically
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: break # esc to quit  
    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=1)

if __name__ == '__main__':
    main()