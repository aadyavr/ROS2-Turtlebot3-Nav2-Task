import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    gazebo_share = get_package_share_directory('turtlebot3_gazebo')
    nav2_share = get_package_share_directory('nav2_bringup')
    
    map_path = os.path.expanduser('~/ros2_ws/src/turtlebot3_nav2_task1/maps/my_map.yaml')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(gazebo_share, 'launch', 'turtlebot3_world.launch.py')
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_share, 'launch', 'bringup_launch.py')
            ),
            launch_arguments={'map': map_path, 'use_sim_time': 'true'}.items()
        )
    ])
