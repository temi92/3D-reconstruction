import cv2
import time

class CameraNotConnected(Exception):
	def __init__(self):
		Exception.__init__(self, "Camera not connected")



class Camera(object):
	"""" class for accesing webcam images"""
	def __init__(self, camera_id=0):
		self.camera_id = camera_id
		self.capture = None 
		self.is_connected = False

	
	"""
	def initialize(self):
		self.brightness = 0
		self.contrast = 0
		self.saturation = 0
		self.exposure = 0 

	"""
	def connect (self):
		print "connecting camera "
		if self.capture is not None:
			self.capture.release()
		self.capture = cv2.VideoCapture(self.camera_id)
		time.sleep(0.03)
		if self.capture.isOpened():
			self.is_connected = True
			
		
		else:
			
			raise CameraNotConnected()

	def set_resolution(self, width, height):
		if self.is_connected:
			self.capture.set(3, width)
			self.capture.set(4, height)



	def disconnect(self):
		if self.is_connected:
			print "disconnecting camera.."
			if self.capture is not None:
				if self.capture.isOpened():
					self.is_connected = False
					self.capture.release()

	def capture_image(self, flush=0):
		"""captures images from camera"""

		if self.is_connected:
			if flush > 0:
				for i in xrange(flush):
					self.capture.read()

			ret, image = self.capture.read()

			if ret:
				return image

			else: 
				return None
		else:

				return None
					
	def save_image(self, filename, image):
		image = cv2.imwrite(filename, image)




	


		

	
