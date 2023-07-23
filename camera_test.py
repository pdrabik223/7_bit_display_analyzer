from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (2592,1944)
camera.rotation = -90
time.sleep(2)
camera.capture("./test.jpg")
print("Done.")