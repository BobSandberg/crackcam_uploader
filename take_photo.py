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

filename="test_photo_{0:%Y-%m-%d_%H-%M}.jpg".format(photo_time)
camera.capture(filename)
print("Photo saved to filename {}".format(filename))

