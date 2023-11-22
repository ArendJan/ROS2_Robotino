from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, TextSubstitution
def generate_launch_description():
    robotino_ip = DeclareLaunchArgument("robotino_ip", default_value=TextSubstitution(text="10.42.0.1"))

    return LaunchDescription([
        robotino_ip,
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='power_node',
            name='power', output="screen", parameters=[{
                "robotino_ip":LaunchConfiguration("robotino_ip")
            }]
        ),
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='controller_node',
            name='controller', output="screen", parameters=[{
                "robotino_ip": LaunchConfiguration("robotino_ip")
            }]
        ),
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='service_node',
            name='service', output="screen", parameters=[{
                "robotino_ip": LaunchConfiguration("robotino_ip")
            }]
        ),
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='io_node',
            name='io', output="screen", parameters=[{
                "robotino_ip": LaunchConfiguration("robotino_ip")
            }]
        ),
        Node(
            package='robotino_ros2',
            namespace='robotino',
            executable='omnidrive_node',
            name='omnidrive', output="screen", parameters=[{
                "robotino_ip": LaunchConfiguration("robotino_ip")
            }]
        )
    ])