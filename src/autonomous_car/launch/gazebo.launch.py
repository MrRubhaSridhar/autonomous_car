from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

import os
import xacro


def generate_launch_description():

    pkg_share = get_package_share_directory("autonomous_car")

    world = os.path.join(
    pkg_share,
    "worlds",
    "empty.sdf"
    )

    robot_file = os.path.join(
        pkg_share,
        "description",
        "robot.urdf.xacro"
    )

    robot_description = xacro.process_file(robot_file).toxml()

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("ros_gz_sim"),
                "launch",
                "gz_sim.launch.py"
            )
        ),
        launch_arguments={
            "gz_args": world +" -r"
        }.items()
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {"robot_description": robot_description}
        ],
        output="screen"
    )

    spawn = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-topic",
            "robot_description",
            "-name",
            "autonomous_car"
        ],
        output="screen"
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn
    ])
