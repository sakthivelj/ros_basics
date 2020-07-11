ROS TOPICS
create a simple ROS topic creating using by a cpp(ros_basic/src) and python(ros_basic/script) code

ros_basics
          ├── CMakeLists.txt
          ├── include
          │   └── ros_basics
          ├── package.xml
          ├── script
          │   ├── listener.py
          │   └── talker.py
          └── src
              ├── listener.cpp
              └── talker.cpp


Running python subscriber and publisher nodes
$ rosrun ros_basicsbasic listener.py
$ rosrun ros_basicsbasic talker.py

Running python subscriber and publisher nodes
$ rosrun ros_basicsbasic listener.cpp
$ rosrun ros_basicsbasic talker.cpp
