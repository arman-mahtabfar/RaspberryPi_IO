import time
import requests
from picamera import PiCamera
from config import load_configuration
from picamera.array import PiRGBArray

config = load_configuration("./config.json")
camera = PiCamera() 
raw_capture = PiRGBArray(camera)

#allow time for the camera to warmup
time.sleep(2)

#grab image from the camera
camera.capture(raw_capture, format="rgb")
image = raw_capture.array

#send the image array via POST request to flask server with model
res = requests.POST(url = config["BASE_URL"]+config["IMAGE_ENDPOINT"], data = image)

print(f"POST: {config["BASE_URL"]+config["IMAGE_ENDPOINT"]}")
print(f"Status: {res.status_code}")
