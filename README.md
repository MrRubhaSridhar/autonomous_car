FOR SETUP BASH : source ~/Z4Ge/install/setup.bash


TO TEST WHEATHER CAR IS MOVING : ros2 topic pub /diff_drive_controller/cmd_vel geometry_msgs/msg/TwistStamped \
"{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.2}, angular: {z: 0.0}}}" -r 10
