from time import sleep
from picamera import PiCamera
from datetime import datetime
from datetime import tzinfo

camera = PiCamera()
camera.resolution = (1024, 768)

camera.start_preview()
print("SMILE")
print("Taking picture in 2 seconds")
sleep(2)
photo_time = datetime.utcnow()

photo_path="/home/pi/crackcam_uploader/photos"
filename="{0}/test_photo_{1:%Y-%m-%d_%H-%M}.jpg".format(photo_path,photo_time)
camera.capture(filename)
print("Photo saved to filename {}".format(filename))

