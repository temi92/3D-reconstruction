import errno
import os
import shutil
import cv2
from config_parser import *
from colour_finder import ColourFinder
import numpy as np
from datetime import datetime

def fit(v, oldmin, oldmax, newmin=0.0, newmax=1.0):
	"""
	Just a standard math fit/remap function 
		number v 		- initial value from old range 
		number oldmin 	- old range min value 
		number oldmax 	- old range max value 
		number newmin 	- new range min value 
		number newmax 	- new range max value  
	Example:
		fit(50, 0, 100, 0.0, 1.0)
		# 0.5
	"""
	scale = (float(v) - oldmin) / (oldmax - oldmin) 
	new_range = scale * (newmax - newmin)
	if newmin < newmax: 
		return newmin + new_range
	else: 
		return newmin - new_range	

def foldercreation():
    mydir = os.path.join(
        "/home/temi/DIGIART_SCANS",
        datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    try:
        os.makedirs(mydir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise  # This was not a "directory exist" error..
    return mydir
 
def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)


def mask():

	colour_finder = ColourFinder()
        colour_finder.run()
                            
	print "reading values for masking from disk...."
	#obtain hsv values ..
	h_low = config.get_integer("segment_roi","h_low",0)
	h_high = config.get_integer("segment_roi","h_high",0)
	s_low = config.get_integer("segment_roi","s_low",0)
	s_high = config.get_integer("segment_roi","s_high",0)
	v_low = config.get_integer("segment_roi","v_low",0)
	v_high = config.get_integer("segment_roi","v_high",0)
	
	colour_low = np.array([h_low,s_low,v_low])
       	colour_high = np.array([h_high,s_high,v_high])
		

	#navigate to  pics directory.
	#retval = os.getcwd()
	retval = "/home/temi/DIGIART/scan_results/pics"	
	
	for filename in os.listdir(retval):
		frame = cv2.imread(os.path.join(retval,filename))
		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		#threshold the hsv_frame
		mask = cv2.inRange(hsv_frame, colour_low, colour_high)
		

		# Erode
            	erode_kernel = np.ones((3,3),np.uint8);
            	eroded_img = cv2.erode(mask,erode_kernel,iterations = 1)
        
            	# dilate
            	dilate_kernel = np.ones((10,10),np.uint8);
            	dilated_img = cv2.dilate(eroded_img,dilate_kernel,iterations = 1)
        
            	# Bitwise-AND mask and original image
		res = cv2.bitwise_and(frame,frame, mask=dilated_img)
		
		#cv2.imshow('Original',frame)
                #cv2.imshow('Mask',mask)
                #cv2.imshow('Filtered Result',res)
		#cv2.waitKey(0)
		cv2.imwrite(os.path.join(retval,filename),res)
	os.chdir("/home/temi/DIGIART")
	#cv2.destroyAllWindows()
	print "finished masking images"



if __name__=="__main__":
	x= fit(5,1,10,0.1,0.9)
	src = "/home/temi/DIGIART/scan_results/pics"
	dest = "/home/temi/DIGIART_SCANS/2018-09-24_16-42-08/pics" 
	copy(src,dest)
	#mask()
