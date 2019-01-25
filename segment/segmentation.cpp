#include <iostream>
//#include <pcl/io/io.h>
#include <pcl/io/pcd_io.h>
#include <pcl/io/ply_io.h>
#include <pcl/point_types.h>
#include <pcl/ModelCoefficients.h>
#include <pcl/filters/extract_indices.h>
#include <pcl/segmentation/sac_segmentation.h>
//#include <pcl/visualization/pcl_visualizer.h>
#include <pcl/filters/statistical_outlier_removal.h>
//#include <pcl/visualization/cloud_viewer.h>
#include "INIReader.h"
#include <Eigen/Dense>


using namespace pcl;
using namespace pcl::io;
using namespace pcl::console;


typedef pcl::PointXYZRGBNormal PointT;

typedef pcl::PointCloud<PointT> PointCloudT;


#define DEBUG 0
#define PLANE_FILTER 0


int main (int argc, char *argv[])
{
	


	INIReader reader("/home/temi/DIGIART/conf.ini");

    	if (reader.ParseError() < 0) {
        	std::cout << "Can't load 'conf.ini'\n";
        	return 1;
    	}

	double dt_threshold = reader.GetReal("filter", "distance_threshold", -1);
	int no_neighbours = reader.GetInteger("filter","no_neighbours",1);
	int std_deviation = reader.GetInteger("filter", "std_deviation",1);

	
	
	PointCloudT::Ptr	cloud (new PointCloudT),
						cloud_inliers (new PointCloudT),
						final_cloud (new PointCloudT),
						cloud_outliers (new PointCloudT);
	



	//pcl::PCLPointCloud2 cloud2;
	//std::string file_name = "pointcloud.ply";
	//bool value = loadCloud(file_name, cloud2);

	//pcl::PCLPointCloud2 cloud2;
	//pcl::PLYReader Reader;
	//Reader.read("pointcloud.ply", *cloud) ;

	//Reader.read("pointcloud.ply", cloud2);
	//std::cout << "loaded ply file" << std::endl;
		
        if (pcl::io::loadPCDFile<PointT> ("/home/temi/DIGIART/scan_results/pointcloud.pcd", *cloud) == -1)
 	{

    		std::cout << "Cloud reading failed." << std::endl;
    		return (-1);

	}
	



#if PLANE_FILTER
	// Segment the ground
	pcl::ModelCoefficients::Ptr plane (new pcl::ModelCoefficients);
	pcl::PointIndices::Ptr 		inliers_plane (new pcl::PointIndices);
	PointCloudT::Ptr 			cloud_plane (new PointCloudT);

	// Make room for a plane equation (ax+by+cz+d=0)
	plane->values.resize (4);

	pcl::SACSegmentation<PointT> seg;				// Create the segmentation object
	seg.setOptimizeCoefficients (true);				// Optional
	seg.setMethodType (pcl::SAC_RANSAC);
	seg.setModelType (pcl::SACMODEL_PLANE);
	seg.setDistanceThreshold (dt_threshold);
	seg.setInputCloud (cloud);
	seg.segment (*inliers_plane, *plane);

	if (inliers_plane->indices.size () == 0) {
		PCL_ERROR ("Could not estimate a planar model for the given dataset.\n");
		return (-1);
	}

	// Extract inliers
	pcl::ExtractIndices<PointT> extract;
	extract.setInputCloud (cloud);
	extract.setIndices (inliers_plane);
	extract.setNegative (false);			// Extract the inliers
	extract.filter (*cloud_inliers);		// cloud_inliers contains the plane

	// Extract outliers
	//extract.setInputCloud (cloud);		// Already done line 50
	//extract.setIndices (inliers);			// Already done line 51
	extract.setNegative (true);				// Extract the outliers
	extract.filter (*cloud_outliers);		// cloud_outliers contains everything but the plane

	printf ("Plane segmentation equation [ax+by+cz+d]=0: [%3.4f | %3.4f | %3.4f | %3.4f]     \t\n", 
			plane->values[0], plane->values[1], plane->values[2] , plane->values[3]);

#else
	pcl::copyPointCloud(*cloud, *cloud_outliers);
	
#endif




	
	#if DEBUG
	// Visualization
	pcl::visualization::PCLVisualizer viewer ("PCL visualizer");

	pcl::visualization::PointCloudColorHandlerCustom<PointT> cloud_inliers_handler (cloud, 255, 20, 20); // Plane in RED
	viewer.addPointCloud (cloud_inliers, cloud_inliers_handler, "cloud inliers");

	pcl::visualization::PointCloudColorHandlerCustom<PointT> cloud_outliers_handler (cloud, 200, 200, 200); // Everything else in GRAY
	viewer.addPointCloud (cloud_outliers, cloud_outliers_handler, "cloud outliers");	

	while (!viewer.wasStopped ()) {
		viewer.spinOnce ();
	}

	#endif

	
	

	//run statistical outlier ... and save point cloud
	pcl::StatisticalOutlierRemoval<PointT> sor;
  	sor.setInputCloud (cloud_outliers);
  	sor.setMeanK (no_neighbours);
  	sor.setStddevMulThresh (std_deviation);
  	sor.filter (*final_cloud);
	
	  	
	pcl::PLYWriter writer;
	writer.write("/home/temi/DIGIART/scan_results/final_cloud.ply",*final_cloud);


	/*
	//save a RGB color without normals for end user to view...
	pcl::PointCloud<pcl::PointXYZRGB>::Ptr coloured_cloud (new pcl::PointCloud<pcl::PointXYZRGB>);

	pcl::copyPointCloud(*final_cloud, *coloured_cloud);
	
	writer.write("final_cloud.ply",*final_cloud);
	*/
	

	return (0);
}
