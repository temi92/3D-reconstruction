from PyQt4 import QtGui,QtCore 
import sys 
import os
import design# This file holds our MainWindow and all design related things
from config_parser import *
from colour_finder import ColourFinder
from reconstruct import *
from capture_images import *
from logging_info import my_logger
from utils import *

class PointCloud_Gen(QtCore.QThread):
        taskFinished = QtCore.pyqtSignal()
        def __init__(self):
                QtCore.QThread.__init__(self)
        def __del__(self):
                self.wait()

	@my_logger
        def gen_pointcloud(self):
		prepscene()
		sfmrecon()  
        	depthmapgen()
        	genpointcloud()
		
        def run(self):
                self.gen_pointcloud()


class Filter_Cloud(QtCore.QThread):
        taskFinished = QtCore.pyqtSignal()
        def __init__(self):
                QtCore.QThread.__init__(self)
        def __del__(self):
                self.wait()

	@my_logger
        def filter_pointcloud(self):
                filterpoints()
        def run(self):
                self.filter_pointcloud()


               
class Mesh_Gen(QtCore.QThread):
        taskFinished = QtCore.pyqtSignal()
        def __init__(self):
                QtCore.QThread.__init__(self)
        def __del__(self):
                self.wait()
        def gen_mesh(self):
                print "generating mesh..."
		createmesh()
        def run(self):
                self.gen_mesh()





class Interface(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
	self.slider_min = 0.1
	self.slider_max = 0.9  #slider range values...
	self.gen_pointcloud = PointCloud_Gen()
	self.filter_cloud = Filter_Cloud()
	self.mesh_gen = Mesh_Gen()
        self.setupUi(self)
        self.BTN_TakePictures.clicked.connect(self.grab_images)
	self.Mask_images.clicked.connect(self.mask_images)  #FIX ME...
	self.BTN_GeneratePointCloud.clicked.connect(self.generate_pointcloud)
	self.BTN_GenerateMeshFile.clicked.connect(self.gen_mesh)
	self.BTN_FilterPointCloud.clicked.connect(self.pointcloud_filtering)

	self.scan_folder = os.path.join(os.getcwd(), "scan_results") 

	#sliders....
	#self.Slider_PlaneFilter.valueChanged.connect(lambda:self.handle_slider_plane(self.Slider_PlaneFilter))
	self.Slider_OutlierFilter.valueChanged.connect(lambda:self.handle_slider_outlierfilter(self.Slider_OutlierFilter))
	self.Slider_Threshold.valueChanged.connect(lambda:self.handle_slider_thresholdfilter(self.Slider_Threshold))



	self.Slider_CleanMesh.valueChanged.connect(lambda:self.handle_slider_cleanmesh(self.Slider_CleanMesh))
	self.Slider_MeshDecimation.valueChanged.connect(lambda:self.trim_mesh(self.Slider_MeshDecimation))
	

	#radio buttons
	self.RBTN_640x480.toggled.connect(lambda:self.btnstate(self.RBTN_640x480))
	self.RBTN_1920x1080.toggled.connect(lambda:self.btnstate(self.RBTN_1920x1080))

	#push buttons..
	self.BTN_PreviewPointCloud.clicked.connect(self.view_cloud)
	self.BTN_PreviewFilteredPointCloud.clicked.connect(self.view_filtered_pointcloud)
	self.BTN_PreviewMesh.clicked.connect(self.view_mesh)
	self.BTN_ViewTexturedMesh.clicked.connect(self.view_texturemesh)

	#sliders...
	self.Slider_NumberOfPictures.valueChanged.connect(self.frames2grab)
	self.Slider_BlurReductionValue.valueChanged.connect(self.handle_slider_blur)


	self.main_window =  QtGui.QMainWindow()
	self.main_window.connect(self.gen_pointcloud,QtCore.SIGNAL("finished()"),self.pointcloud_done) #signal main window once threaded application finishes running
	self.main_window.connect(self.mesh_gen,QtCore.SIGNAL("finished()"),self.mesh_done)
	self.main_window.connect(self.filter_cloud,QtCore.SIGNAL("finished()"),self.pointcloud_filtering_done)




    def btnstate(self,b):
	if b.text() == "640 x 480":
		if b.isChecked() == True:
			config.set_integer("image_settings","width",640)
			config.set_integer("image_settings","height",480)
        		config.save()

	if b.text() == "1920 x 1080":
		if b.isChecked() == True:
			config.set_integer("image_settings","width",1920)
                        config.set_integer("image_settings","height",1080)
                        config.save()

    def handle_slider_blur(self):
	val = self.Slider_BlurReductionValue.value()
	config.set_float("image_settings","threshold",val *20.0)
        config.save()


    def handle_slider_plane(self,b):
	#TODO remove function not needed anymore (no need for plane filter)
	val = self.Slider_PlaneFilter.value()
	newVal = fit(val,0,10,self.slider_min,self.slider_max)
	print newVal
	config.set_float("filter_settings","distance_threshold",newVal)
	config.save()


    def handle_slider_outlierfilter(self,b):	
	val = self.Slider_OutlierFilter.value()
	config.set_integer("filter_settings","no_neighbours",val)
	config.save()
   
    def handle_slider_thresholdfilter(self,b):
	#sets slider for std_deviation...
	val = self.Slider_Threshold.value()
	config.set_integer("filter_settings","std_deviation",val)
	config.save()

    def handle_slider_cleanmesh(self,b):
	
	depth = self.Slider_CleanMesh.value()
	config.set_integer("mesh_settings","depth",depth)
        config.save()

    def trim_mesh(self,b):
	trim =  self.Slider_MeshDecimation.value()
	config.set_integer("mesh_settings","trim",trim)
        config.save()
    def grab_images(self):


	#delete pics folder ..
	pics_folder = os.path.join(self.scan_folder, "pics")
	filelist = [ f for f in os.listdir(pics_folder) if f.endswith(".png")]
	for f in filelist:
		os.remove(os.path.join(pics_folder,f))

	
	#remove scene folder...
	dirpath = os.path.join(self.scan_folder, "scene")
	if os.path.exists(dirpath) and os.path.isdir(dirpath):
		print "removed scene folder"
		shutil.rmtree(dirpath)

	image_grabber()
		

    def mask_images(self):

	mask()  #mask to allow processing of region of interest.	

    def generate_pointcloud(self):
	self.Progress_PointCloud.setRange(0,0)
	self.gen_pointcloud.start()

    def pointcloud_done(self):
	self.Progress_PointCloud.setRange(0,1)
        self.Progress_PointCloud.setValue(1)
	QtGui.QMessageBox.information(self.main_window,"Done!", "Finished processing point cloud")


    def mesh_done(self):
	self.Progress_MeshFile.setRange(0,1)
	self.Progress_PointCloud.setValue(1)
	QtGui.QMessageBox.information(self.main_window,"Done!", "Finished processing mesh")


    def gen_mesh(self):
	self.Progress_MeshFile.setRange(0,0)
	self.mesh_gen.start()
	

    def view_cloud(self):
        ply = os.path.join(self.scan_folder, "pointcloud.ply")
	cmd = " ".join(["cd", self.scan_folder, ";", "meshlab", "pointcloud.ply"])
	if (os.path.exists(ply)):
		p = Popen(cmd, shell=True)
		p.wait()
	else:
		QtGui.QMessageBox.critical(self.main_window, "Message", "failed to generate point cloud, consider increasing number of images taken and ensure the object is within FOV of camera")
    def view_filtered_pointcloud(self):
	cmd = " ".join(["cd", self.scan_folder, ";", "meshlab", "final_cloud.ply"])	
	p = Popen(cmd, shell=True)
	p.wait()
	
    def pointcloud_filtering(self):
	self.Progress_PointCloud.setRange(0,0)
	self.filter_cloud.start()

    def pointcloud_filtering_done(self):
	self.Progress_PointCloud.setRange(0,1)
	self.Progress_PointCloud.setValue(1)
	QtGui.QMessageBox.information(self.main_window,"Done!", "Finished filtering point cloud")

    def view_mesh(self):
	cmd = " ".join(["cd", self.scan_folder, ";", "meshlab", "surface_trimmed.ply"])
	p = Popen(cmd, shell=True)
	p.wait()

    def view_texturemesh(self):
        #TODO... process textured mesh and bind to buttion.
	cmd = " ".join(["cd", self.scan_folder, ";", "meshlab", "textured.obj"])

	QtGui.QMessageBox.information(self.main_window,"processing ..", "generating textured mesh this might take a few seconds")
	texturemesh()
	p = Popen(cmd, shell=True)
	p.wait()


    def frames2grab(self):
	no_frames = self.Slider_NumberOfPictures.value()
	config.set_integer("image_settings","images",no_frames)
	config.save()

def populate_dir():
	mydir = foldercreation() #creates folder that contains results.
	##CONTINUE...NOW....
	source = os.listdir("scan_results")
	os.chdir("scan_results")
	pic_folder = os.path.join(mydir, "pics")
	shutil.copytree("pics",pic_folder)

	for files in source:
		if files.endswith(".ply") or files.endswith(".obj") or files.endswith(".png") or files.endswith(".mtl"):
			shutil.move(files, mydir)


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = Interface()                 #We set the form to be our ExampleApp (design)
    form.show()                    
    app.exec_()                        


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
    populate_dir() 

    
