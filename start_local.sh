#!/bin/bash
if [ ! "$HOSTNAME" = robotino ]; then
    echo "This script should be run on the robotino robot"
fi
cd "$(dirname "$0")" || exit
colcon build
source install/setup.bash
export ROS_DOMAIN_ID=1
ros2 launch robotino_ros2 robotino_local.launch.py