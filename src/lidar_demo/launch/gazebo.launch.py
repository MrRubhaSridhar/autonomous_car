from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

import os
import xacro


def generate_launch_description():

    pkg = get_package_share_directory("lidar_demo")

    world = os.path.join(
        pkg,
        "worlds",
        "empty.sdf"
    )

    robot_file = os.path.join(
        pkg,
        "description",
        "robot.urdf.xacro"
    )

    robot_description = xacro.process_file(
        robot_file
    ).toxml()

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("ros_gz_sim"),
                "launch",
                "gz_sim.launch.py"
            )
        ),
        launch_arguments={
            "gz_args": world + " -r"
        }.items()
    )

    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {
                "robot_description": robot_description,
                "use_sim_time": True,
            }
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
            "lidar_robot",
        ],
        output="screen"
    )

    bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock",
            "/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan",
        ],
        output="screen"
    )

    controllers_file = os.path.join(
        pkg,
        "config",
        "controllers.yaml"
    )

    joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--param-file",
            controllers_file,
        ],
        output="screen",
    )

    diff_drive_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "diff_drive_controller",
            "--param-file",
            controllers_file,
        ],
        output="screen",
    )

    return LaunchDescription([
        gazebo,
        rsp,
        spawn,
        bridge,

        TimerAction(
            period=3.0,
            actions=[joint_state_broadcaster],
        ),

        TimerAction(
            period=5.0,
            actions=[diff_drive_controller],
        ),
    ])
