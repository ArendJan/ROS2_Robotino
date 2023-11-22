# ROS2_Robotino
ROS2 package for robotino.
Fully redesigned package that adapts to robotino [RestAPI](https://wiki.openrobotino.org/index.php?title=Rest_api).
This tutorail introduces preparation for the ROS2 Robotino Package.

---

## Prerequisites
Before process this step, make sure you are connected to the Robotino, your computer has this package installed and the Robotino has this package and it is running the `robotino_local.launch.py` launch file.

## Start SLAM 

Launch the `robotino_slam` launch file with
```sh
source install/setup.bash
export ROS_DOMAIN_ID=1
ros2 launch robotino_ros2 robotino_slam.launch.py
```
Or just run `./run_slam.sh`.
It will start rviz2:

![](start.png)


Click on the left bottom button **ADD** to add /map (Map) and /scan (laserScan) topics:

![](./add.png)

You will see a menu pops up

![](./add_item.png)

click the **By topic** button and you will see the menu

![](./add_topic.png)

Add both `/map` and `/scan` topics to your rviz2.

The map should look like 

![](final.png)

At this moment you are ready for creating your own map!

More tutorials and info about slam_toolbox you can find at this [repository](https://github.com/SteveMacenski/slam_toolbox)

Rivz2 tutorial you can find at this [repository](https://github.com/ros2/rviz)

---

## Drive Robotino
To drive it around, you can use keyboard to drive. open a new terminal and run the following command
```
export ROS_DOMAIN_ID=1
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Follow the instruction on the screen and drive it around!
Be careful! Don't hit anything!

## Further problems
You can send emails to my [email address](ziang.qiu@gmail.com).