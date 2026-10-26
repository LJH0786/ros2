cmake_minimum_required(VERSION 3.0.2)
project(air_teleop)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  std_msgs
)

catkin_package()

catkin_install_python(PROGRAMS
  scripts/keyboard_teleop.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
