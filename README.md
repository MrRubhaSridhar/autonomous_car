FOR SETUP BASH : source ~/Z4Ge/install/setup.bash


TO TEST WHEATHER CAR IS MOVING : ros2 topic pub /diff_drive_controller/cmd_vel geometry_msgs/msg/TwistStamped \
"{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.2}, angular: {z: 0.0}}}" -r 10

CMD FOR LAUNCH :  ros2 launch lidar_demo gazebo.launch.py

FOR TELEOP :  ros2 run teleop_twist_keyboard teleop_twist_keyboard \ --ros-args \ -p stamped:=true \ -r cmd_vel:=                         diff_drive_controller/cmd_vel



# 📌 Project Progress

| Phase | Status | Description | Command |
|:------|:------:|------------|---------|
| **1. ROS 2 Workspace Setup** | ✅ Completed | Created ROS 2 workspace and configured packages | `colcon build --symlink-install` |
| **2. Robot Modeling (URDF/Xacro)** | ✅ Completed | Designed chassis, wheels, LiDAR mount, collision & inertia | `check_urdf robot.urdf` |
| **3. Robot State Publisher** | ✅ Completed | Published robot model and TF frames | `ros2 launch lidar_demo display.launch.py` |
| **4. Gazebo Simulation** | ✅ Completed | Spawned robot successfully in Gazebo Harmonic | `ros2 launch lidar_demo gazebo.launch.py` |
| **5. ROS 2 Control** | ✅ Completed | Configured Joint State Broadcaster & Diff Drive Controller | `ros2 control list_controllers` |
| **6. Robot Motion** | ✅ Completed | Verified keyboard teleoperation | `ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/diff_drive_controller/cmd_vel` |
| **7. LiDAR Integration (Simulation)** | ✅ Completed | Added RP-LiDAR and verified LaserScan data | `ros2 topic echo /scan` |
| **8. TF & ROS Communication** | ✅ Completed | Verified TF tree and ROS topics | `ros2 run tf2_tools view_frames` |
| **9. Real RP-LiDAR Integration** | ⏳ Pending | Connect RP-LiDAR to Raspberry Pi and verify `/scan` | `ros2 launch sllidar_ros2 sllidar_a1_launch.py` |
| **10. Motor Driver Interface** | ⏳ Pending | Interface Raspberry Pi GPIO with motor driver | `ros2 run autonomous_car motor_driver` |
| **11. Wheel Odometry** | ⏳ Pending | Publish accurate `/odom` from wheel encoders | `ros2 topic echo /odom` |
| **12. SLAM Mapping** | ⏳ Pending | Generate and save map using SLAM Toolbox | `ros2 launch slam_toolbox online_async_launch.py` |
| **13. Localization (AMCL)** | ⏳ Pending | Localize robot on the saved map | `ros2 launch nav2_bringup localization_launch.py map:=my_map.yaml` |
| **14. Navigation2** | ⏳ Pending | Configure Nav2 for autonomous navigation | `ros2 launch nav2_bringup navigation_launch.py map:=my_map.yaml` |
| **15. Autonomous Navigation** | ⏳ Pending | Navigate to goal with obstacle avoidance | `rviz2` → **2D Goal Pose** |
