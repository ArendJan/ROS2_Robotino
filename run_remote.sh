#!/bin/bash
if [ "$HOSTNAME" = robotino ]; then
    echo "This script should NOT be run on the robotino robot"
fi
source install/setup.sh
export ROS_DOMAIN_ID=1
ros2 launch robotino_ros2 robotino_remote.launch.py