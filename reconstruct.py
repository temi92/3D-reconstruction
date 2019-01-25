from subprocess import Popen,PIPE
import os
from config_parser import *


###entry point into the application ...
base_path = os.getcwd()
print base_path

prep_scene = os.path.join(base_path, "executables/makescene")

sfm_recon = os.path.join(base_path, "executables/sfm_pipeline")

depth_map_gen = os.path.join(base_path, "executables/dmrecon")

gen_pointcloud = os.path.join(base_path, "executables/scene2pointcloud")

#convert points to pcd format for processing ...
pcd_converter = os.path.join(base_path, "executables/pcl_ply2pcd")

filter_points = os.path.join(base_path, "executables/segmentation")


create_mesh = os.path.join(base_path, "executables/SSDRecon")

filter_mesh = os.path.join(base_path, "executables/SurfaceTrimmer")


texture_mesh  = os.path.join(base_path, "executables/texrecon")


def prepscene():
	p = Popen([prep_scene,"-i", "scan_results/pics", "scan_results/scene"])
	p.wait()

def sfmrecon():
	p = Popen([sfm_recon, "scan_results/scene"])
	p.wait()
def depthmapgen():
	p = Popen([depth_map_gen, "-s2", "scan_results/scene"])
	p.wait()
def genpointcloud():
	p = Popen([gen_pointcloud, "-F2", "scan_results/scene", "scan_results/pointcloud.ply"])
	p.wait()

def filterpoints():
	ply = os.path.join( os.getcwd(), "scan_results/pointcloud.ply")
	pcd = os.path.join(os.getcwd(), "scan_results/pointcloud.pcd")
	
	p = Popen([pcd_converter, ply, pcd])
	p.wait()
	#filter_points takes in pcd format pointcloud...
	p = Popen([filter_points])
	p.wait()
def createmesh():
	depth = config.get_string("mesh_settings","depth",8)
	trim = config.get_string("mesh_settings", "trim",8)

	mesh = Popen([create_mesh,"--in", "scan_results/final_cloud.ply", "--out", "scan_results/surface.ply", "--depth", depth, "--colors", "--density"])
	mesh.wait()
	trim_mesh = Popen([filter_mesh, "--in", "scan_results/surface.ply", "--out", "scan_results/surface_trimmed.ply", "--trim", trim])
	trim_mesh.wait()


def texturemesh():
	p = Popen([texture_mesh, "scan_results/scene"+"::undistorted", "scan_results/surface_trimmed.ply", "scan_results/textured"])
	p.wait()


#prepscene()
#sfmrecon()
#depthmapgen()
#genpointcloud()
#filterpoints()
#createmesh()
#texturemesh()


