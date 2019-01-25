import datetime
## wrapper fuctions for logging...

def my_logger(func):
	import logging 
	import time
	logging.basicConfig(filename='anlysis.log', level=logging.INFO)
	logging.info("Timestamp: {:%Y-%b-%d %H:%M:%S}".format(datetime.datetime.now()))

	def wrapper(*args, **kwargs):
		
		t1 = time.time()
		result = func(*args, **kwargs)
		t2 = time.time() - t1
		minutes, seconds = divmod(t2, 60)
		if func.__name__ == "image_grabber":

			logging.info("processing time for image capture  is {} minutes and {:.3f} seconds".format(minutes, seconds))
		elif func.__name__ == "gen_pointcloud":
			logging.info("processing time for point cloud processing is {} minutes and {:.3f} seconds".format(minutes, seconds))

		elif func.__name__ == "filter_pointcloud":
				logging.info("processing time for filtering point clouds is {} miunutes and {:.3f} seconds".format(minutes, seconds))
		else:
			raise Exception("supplied invalid function")
	return wrapper
