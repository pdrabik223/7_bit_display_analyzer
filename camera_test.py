from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 90
time.sleep(2)
camera.capture("./test.jpg")
print("Done.")