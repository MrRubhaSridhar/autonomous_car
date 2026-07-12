FOR SETUP BASH : source ~/Z4Ge/install/setup.bash


TO TEST WHEATHER CAR IS MOVING : ros2 topic pub /diff_drive_controller/cmd_vel geometry_msgs/msg/TwistStamped \
"{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.2}, angular: {z: 0.0}}}" -r 10

CMD FOR LAUNCH :  ros2 launch lidar_demo gazebo.launch.py

FOR TELEOP :  ros2 run teleop_twist_keyboard teleop_twist_keyboard \ --ros-args \ -p stamped:=true \ -r cmd_vel:=                         diff_drive_controller/cmd_vel

