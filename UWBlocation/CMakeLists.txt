cmake_minimum_required(VERSION 2.8.3)
project(UWBlocation)




find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg)

## Declare ROS messages and services
add_message_files(FILES location.msg)
# add_service_files(FILES AddTwoInts.srv)

## Generate added messages and services
generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

## Build talker and listener
# include_directories(include ${catkin_INCLUDE_DIRS})

# add_executable(UWB_location src/UWB_location.cpp)
# target_link_libraries(UWB_location ${catkin_LIBRARIES})
# add_dependencies(UWB_location beginner_tutorials_generate_messages_cpp)

# add_executable(location_sub src/location_sub.cpp)
# target_link_libraries(location_sub ${catkin_LIBRARIES})
# add_dependencies(location_sub beginner_tutorials_generate_messages_cpp)

# add_executable(int8 src/int8_pub.cpp)
# target_link_libraries(int8 ${catkin_LIBRARIES})
# add_dependencies(int8 beginner_tutorials_generate_messages_cpp)
# %EndTag(FULLTEXT)%
