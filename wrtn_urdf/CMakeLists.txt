cmake_minimum_required(VERSION 3.8)
project(wrtn_urdf)

find_package(ament_cmake REQUIRED)

ament_package()

install(DIRECTORY meshes urdf DESTINATION share/${PROJECT_NAME})