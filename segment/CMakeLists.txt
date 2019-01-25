cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(filter_project)

find_package(PCL 1.8 REQUIRED)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable (segmentation segmentation.cpp INIReader.h)
target_link_libraries (segmentation ${PCL_LIBRARIES})
