cmake_minimum_required(VERSION 3.0.2)
project(ros_msg)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  std_msgs
)


## Generate messages in the 'msg' folder
add_message_files(
  FILES
  IoTSensor.msg
)

 # generate_messages(
 #   DEPENDENCIES
 #   ros_msg
 # )

catkin_package(

 LIBRARIES ros_msg
 CATKIN_DEPENDS roscpp rospy std_msgs message_runtime

)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
