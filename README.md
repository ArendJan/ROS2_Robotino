# ROS2_Robotino
ROS2 package for Robotino.
Fully redesigned package that adapts to Robotino [RestAPI](https://wiki.openrobotino.org/index.php?title=Rest_api).

## Prerequisite

To run this package, you have to install these system components first.
- [Robotino4 OS](https://wiki.openrobotino.org/index.php?title=Robotino4_images)
- [ROS Galactic](https://docs.ros.org/en/galactic/Installation.html) on the Robotino.
- ROS Galactic or Humble on your machine

Use other version is at your **OWN** risk, they are **NOT** tested with this system.

ROS2 Humble for Robotino has not been tested, since the Robotino only supports Ubuntu 20.04.

ROS2 Humble for your PC has been tested.

## Install
### Robotino
Connect Robotino with ssh protocol \
`sshpass -p robotino robotino@robotino_ip_address`

Clone this repository by \
`git clone https://github.com/arendjan/ROS2_Robotino.git`

Install dependencies with rosdep \
`rosdep install --from-paths ROS2_Robotino --ignore-src -r -y`

Cd into the repo \
`cd ROS2_Robotino`

build the package by \
`colcon build`

Source the ros package by \
`source install/setup.bash` 
or 
`source install/setup.zsh`

config network connection by \
`export ROS_DOMAIN_ID=1`

launch camera, laser, control, and other nodes on the robotino by \
`ros2 launch robotino_ros2 robotino_local.launch.py`

---

Or run `./start_local.sh` and it will do setup and launch commands.


## Your computer
No need to install anything besides ROS2 (Humble) except when you want to use SLAM or use any of the Robotino messages.

Clone this repository by \
`git clone https://github.com/arendjan/ROS2_Robotino.git`

Install dependencies with rosdep \
`rosdep install --from-paths ROS2_Robotino --ignore-src -r -y`

Cd into the repo \
`cd ROS2_Robotino`

build the package by \
`colcon build`

Source the ros package by \
`source install/setup.bash` 
or 
`source install/setup.zsh`

config network connection by \
`export ROS_DOMAIN_ID=1`

launch the SLAM nodes by \
`ros2 launch robotino_ros2 robotino_slam.launch.py`

---

Or run `./run_slam.sh` to setup and launch SLAM.

# Controlling the Robotino
`/cmd_vel` is there for you to control the Robotino on `ROS_DOMAIN_ID=1`

## Teleop
`ros2 run teleop_twist_keyboard teleop_twist_keyboard`


# Messages

