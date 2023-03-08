# ROS2_Robotino
ROS2 package for robotino.
Fully redesigned package that adapts to robotino [RestAPI](https://wiki.openrobotino.org/index.php?title=Rest_api).
This tutorail introduces preparation for the ROS2 Robotino Package.

## Prerequisite
---
To use this package, you have to install Ubuntu 20.04 first.
Ubuntu 20.04 is strongly recommended, Ubuntu 22.04 should be ok, but it is **NOT** tested yet.
Other linux systems are **NOT** tested.
You can follow this [tutorial](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) to install Ubuntu 20.04.
Or you can follow this [tutorial](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview) to install Ubuntu 20.04 with VirtualBox.


## Dependency
---

### Install Tools
To download the package, you have to install `Git` and `SSH` tools first. Press `ctrl+alt+t` to open the terminal or go to menu and find termial. Copy and paste the following commands.
```
sudo apt update
sudo apt upgrade
sudo apt install git openssh-client
```
---

### Install ROS
Due to Robotino hardware out of date, Robotino3 could only run [ROS Galactic](https://docs.ros.org/en/galactic/index.html).
If you are using Ubuntu 22.04, you should install [ROS Humble](https://docs.ros.org/en/humble/index.html). Please follow the tutorial in this [section](https://docs.ros.org/en/galactic/Installation/Ubuntu-Install-Debians.html).

#### Set Local
---
Make sure you have a locale which supports UTF-8. If you are in a minimal environment (such as a docker container), the locale may be something minimal like POSIX. We test with the following settings. However, it should be fine if you’re using a different UTF-8 supported locale.
```
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

#### Setup Source List
---
You will need to add the ROS 2 apt repository to your system. First, make sure that the Ubuntu Universe [repository](https://help.ubuntu.com/community/Repositories/Ubuntu) is enabled by checking the output of this command.
```
apt-cache policy | grep universe
```
This should output a line like the one below:
```
500 http://us.archive.ubuntu.com/ubuntu focal/universe amd64 Packages
    release v=20.04,o=Ubuntu,a=focal,n=focal,l=Ubuntu,c=universe,b=amd64
```
If you don’t see an output line like the one above, then enable the Universe repository with these instructions.
```
sudo apt install software-properties-common
sudo add-apt-repository universe
```
Now add the ROS 2 apt repository to your system. First authorize our GPG key with apt.
```
sudo apt update && sudo apt install curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```
Then add the repository to your sources list.
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

#### Install ROS2 Package
Update your apt repository caches after setting up the repositories.
```
sudo apt update
```
ROS 2 packages are built on frequently updated Ubuntu systems. It is always recommended that you ensure your system is up to date before installing new packages.
```
sudo apt upgrade
```
Desktop Install (Recommended): ROS, RViz, demos, tutorials.
```
sudo apt install ros-galactic-desktop
```

#### Environment setup
---
If you are using `bash` please input
```
source /opt/ros/galactic/setup.bash
```
If you are using `zsh` please input
```
source /opt/ros/galactic/setup.zsh
```

Please add the command to `.zshrc` or `.bashrc`.

#### Try some examples
---
Try to run this command to make sure the installation is success.
```
ros2
```

If you can see the following output, it means you have installed ROS2 Galactic suceesfully! Contgratulations!
```
usage: ros2 [-h] Call `ros2 <command> -h` for more detailed usage. ...

ros2 is an extensible command-line tool for ROS 2.

optional arguments:
  -h, --help            show this help message and exit

Commands:
  action     Various action related sub-commands
  bag        Various rosbag related sub-commands
  component  Various component related sub-commands
  daemon     Various daemon related sub-commands
  doctor     Check ROS setup and other potential issues
  interface  Show information about ROS interfaces
  launch     Run a launch file
  lifecycle  Various lifecycle related sub-commands
  multicast  Various multicast related sub-commands
  node       Various node related sub-commands
  param      Various param related sub-commands
  pkg        Various package related sub-commands
  run        Run a package specific executable
  security   Various security related sub-commands
  service    Various service related sub-commands
  topic      Various topic related sub-commands
  wtf        Use `wtf` as alias to `doctor`

  Call `ros2 <command> -h` for more detailed usage.
```

