import cv2
import os
import numpy as np
from config_parser import *

class ColourFinder:

    # constructor
    def __init__(self):
        # initialise colour filters to no filtering
        self.h_low = 0
        self.h_high = 255
        self.s_low = 0
        self.s_high = 255
        self.v_low = 0
        self.v_high = 255

        # initialise save trackbar setting
        self.save = 0

    # call back for trackbar movements
    def empty_callback(self,x): #x is the value of the slider..
        pass

    # call back for save trackbar that saves colour filters to config file
    def save_callback(self,x):
        if x == 10:
            config.set_integer('segment_roi','h_low',self.h_low)
            config.set_integer('segment_roi','h_high',self.h_high)
            config.set_integer('segment_roi','s_low',self.s_low)
            config.set_integer('sgement_roi','s_high',self.s_high)
            config.set_integer('segment_roi','v_low',self.v_low)
            config.set_integer('segment_roi','v_high',self.v_high)
            config.save();
            print "Saved colour filters to config file!"
        return

    # run - main routine to help user find colour filters
    def run(self):


        # create trackbars for color change
        cv2.namedWindow('Colour Filters')
        cv2.createTrackbar('Hue min','Colour Filters',self.h_low,255,self.empty_callback)
        cv2.createTrackbar('Hue max','Colour Filters',self.h_high,255,self.empty_callback)
        cv2.createTrackbar('Sat min','Colour Filters',self.s_low,255,self.empty_callback)
        cv2.createTrackbar('Sat max','Colour Filters',self.s_high,255,self.empty_callback)
        cv2.createTrackbar('Bgt min','Colour Filters',self.v_low,255,self.empty_callback)
        cv2.createTrackbar('Bgt max','Colour Filters',self.v_high,255,self.empty_callback)
        cv2.createTrackbar('Save','Colour Filters',0,10,self.save_callback)

	#navigate to  pics directory.
        retval = os.getcwd()
        pic_dir = os.path.join(retval, "scan_results/pics")
        os.chdir(pic_dir)
	#grab first frame saved to use for sgementation
	for directory, dir_name, filenames in os.walk(pic_dir):
		pass

	
	frame = filenames[0]
	#print frame
	frame = cv2.imread(frame)

	#go back to previous directory..
	#os.chdir(retval)

        # Convert BGR to HSV
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        while True:

		# get latest trackbar positions
        	self.h_low = cv2.getTrackbarPos('Hue min','Colour Filters')
        	self.h_high = cv2.getTrackbarPos('Hue max','Colour Filters')
       	 	self.s_low = cv2.getTrackbarPos('Sat min','Colour Filters')
        	self.s_high = cv2.getTrackbarPos('Sat max','Colour Filters')
        	self.v_low = cv2.getTrackbarPos('Bgt min','Colour Filters')
        	self.v_high = cv2.getTrackbarPos('Bgt max','Colour Filters')
        
        	# use trackbar positions to filter image
        	colour_low = np.array([self.h_low,self.s_low,self.v_low])
        	colour_high = np.array([self.h_high,self.s_high,self.v_high])
       

        	# Threshold the HSV image
        	mask = cv2.inRange(hsv_frame, colour_low, colour_high)
        
        	# Erode
        	erode_kernel = np.ones((3,3),np.uint8);
        	eroded_img = cv2.erode(mask,erode_kernel,iterations = 1)
        
        	# dilate
        	dilate_kernel = np.ones((10,10),np.uint8);
        	dilated_img = cv2.dilate(eroded_img,dilate_kernel,iterations = 1)
        
        	# Bitwise-AND mask and original image
        	res = cv2.bitwise_and(frame,frame, mask=dilated_img)
        
        	cv2.imshow('Original',frame)
       		cv2.imshow('Mask',mask)
       		cv2.imshow('Filtered Result',res)
             
        	k = cv2.waitKey(1) &0xFF
		if k ==27:
			break
	    	

        	# close all windows
        cv2.destroyAllWindows()
	
if __name__=="__main__":
# create global colour_finder object and run it
	colour_finder = ColourFinder()
	colour_finder.run()
