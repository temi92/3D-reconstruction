import time
import serial
import cv2
from config_parser import *
from camera_driver import Camera
from logging_info import my_logger

def detect_blur_images(image):
	#use laplacian method to compute 2nd derivate of the image..
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	focus = cv2.Laplacian(image, cv2.CV_64F).var()
	return focus

@my_logger
def image_grabber():
	no_images = config.get_integer("image_settings", "images",50)
	width = config.get_integer("image_settings", "width",640)
	height = config.get_integer("image_settings", "height",480)
	threshold = config.get_float("image_settings", "threshold",100.0)
	cam = Camera()
	cam.connect()
	cam.set_resolution(width, height)
	arduino = serial.Serial("/dev/ttyUSB0",9600) #connect to arduino..
	image_counter = 0 # track overall no of frames
	i = 0 # track only good frames..
	
	while True:
		arduino.write('R'.encode())
		time.sleep(1)
		frame = cam.capture_image(flush=5)
		if frame is not None:
			cv2.imshow("frame",frame)
			if cv2.waitKey(1) & 0XFF == ord('q'):
				break
			focus_measure = detect_blur_images(frame)
			print "focus measure for image {} is {}".format(image_counter, focus_measure)
			if focus_measure > threshold:

				cam.save_image("scan_results/pics/frame"+str(image_counter)+".png",frame)
				i +=1
			image_counter+=1
			if  i > no_images:
				break
				
		else:
			raise Exception ("cannot acquire frames from camera")

	cam.disconnect()
	cv2.destroyAllWindows()
	

if __name__=="__main__":
	image_grabber()




