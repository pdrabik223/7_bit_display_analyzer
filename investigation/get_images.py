
import cv2
import os
if __name__ == "__main__":
    cam = cv2.VideoCapture("./investigation/data/first_video_capture_phone.mp4")
    
    if (cam.isOpened()== False): 
        print("Error opening video stream or file")

    print("loading file")
    for i in range(40):
        ret,frame = cam.read()
        
        if ret:
            # if video is still left continue creating images
            name = str(i) + '.jpg'
            print ('new frame captured...' + name)
            cv2.imshow('Frame',frame)
    
            if cv2.waitKey(25):
                break
            cv2.imwrite(name, frame)
    cam.release()
    cv2.destroyAllWindows()