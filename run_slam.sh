#!/bin/bash
if [ "$HOSTNAME" = robotino ]; then
    echo "This script should NOT be run on the robotino robot"
fi
colcon build
export ROS_DOMAIN_ID=1
source install/setup.sh
ros2 launch robotino_ros2 robotino_slam.launch.py