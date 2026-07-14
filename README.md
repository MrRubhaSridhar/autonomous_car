FOR SETUP BASH : source ~/Z4Ge/install/setup.bash


TO TEST WHEATHER CAR IS MOVING : ros2 topic pub /diff_drive_controller/cmd_vel geometry_msgs/msg/TwistStamped \
"{header: {frame_id: 'base_link'}, twist: {linear: {x: 0.2}, angular: {z: 0.0}}}" -r 10

CMD FOR LAUNCH :  ros2 launch lidar_demo gazebo.launch.py

FOR TELEOP : ros2 run teleop_twist_keyboard teleop_twist_keyboard \
  --ros-args \
  -p stamped:=true \
  -p frame_id:=base_link \
  --remap cmd_vel:=/diff_drive_controller/cmd_vel



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




# 🚗 Autonomous Car Simulation Progress

## ✅ Current Progress

### Phase 1 – Development Environment
- [x] Ubuntu Linux Setup
- [x] ROS 2 Jazzy Installation
- [x] Gazebo Harmonic (Gazebo Sim 8)
- [x] Colcon Workspace
- [x] Git & GitHub Repository

---

### Phase 2 – Robot Modeling
- [x] Robot URDF
- [x] Xacro Modular Structure
- [x] Base Link
- [x] Chassis
- [x] Four Wheel Configuration
- [x] Wheel Joints
- [x] LiDAR Mount
- [x] TF Tree

---

### Phase 3 – Gazebo Simulation
- [x] Empty World
- [x] Robot Spawn
- [x] Gazebo Plugins
- [x] GPU LiDAR Integration
- [x] Fixed Gazebo Sensors Plugin Issue
- [x] Robot Visualization

---

### Phase 4 – ros2_control
- [x] GazeboSimSystem
- [x] Velocity Interfaces
- [x] Joint State Broadcaster
- [x] Differential Drive Controller
- [x] Wheel Control

---

### Phase 5 – LiDAR Integration
- [x] GPU LiDAR Sensor
- [x] 360° Laser Scan
- [x] `/scan` Topic
- [x] ROS-Gazebo Bridge
- [x] RViz Visualization

---

### Phase 6 – Robot Motion
- [x] Differential Drive Motion
- [x] Wheel Rotation
- [x] Odometry Publishing
- [x] Robot Movement in Gazebo
- [x] Robot Movement in RViz

---

## 📊 Project Status

| Component | Status |
|----------|--------|
| Robot Model | ✅ Complete |
| Gazebo Simulation | ✅ Complete |
| ros2_control | ✅ Complete |
| Differential Drive | ✅ Complete |
| LiDAR | ✅ Complete |
| LaserScan | ✅ Complete |
| RViz | ✅ Complete |
| Robot Motion | ✅ Complete |
| SLAM | ⏳ Next |
| Map Generation | ⏳ Pending |
| Localization | ⏳ Pending |
| Navigation (Nav2) | ⏳ Pending |
| Autonomous Navigation | ⏳ Pending |

---

# 🛠 Tested Commands

## Build Workspace

```bash
cd ~/Z4Ge
colcon build
source install/setup.bash
```

## Launch Simulation

```bash
ros2 launch lidar_demo gazebo.launch.py
```

## Verify LiDAR

```bash
ros2 topic list | grep scan
```

```bash
ros2 topic echo /scan
```

## Verify Controllers

```bash
ros2 control list_controllers
```

## Verify Robot Nodes

```bash
ros2 node list
```

## Verify Robot Motion

```bash
ros2 topic pub /diff_drive_controller/cmd_vel geometry_msgs/msg/TwistStamped \
"{header:{frame_id:'base_link'},twist:{linear:{x:0.3},angular:{z:0.0}}}"
```

---

# 📂 Current Package Structure

```
lidar_demo/
├── config/
│   └── controllers.yaml
├── description/
│   ├── robot.urdf.xacro
│   ├── lidar.xacro
│   ├── ros2_control.xacro
│   └── gazebo.xacro
├── launch/
│   └── gazebo.launch.py
├── worlds/
│   └── empty.sdf
```

---

# 🎯 Next Milestones

- [ ] Install SLAM Toolbox
- [ ] Create `slam.launch.py`
- [ ] Generate Occupancy Map
- [ ] Save Generated Map
- [ ] Configure AMCL
- [ ] Configure Nav2
- [ ] Autonomous Goal Navigation
- [ ] Obstacle Avoidance
- [ ] Camera Integration
- [ ] YOLO Object Detection
- [ ] Complete Autonomous Car Simulation

---

# 📅 Development Roadmap

```
✅ Robot Modeling
        ↓
✅ Gazebo Simulation
        ↓
✅ ros2_control
        ↓
✅ LiDAR
        ↓
✅ Robot Motion
        ↓
🔜 SLAM Toolbox
        ↓
🔜 Map Generation
        ↓
🔜 Map Saving
        ↓
🔜 Localization (AMCL)
        ↓
🔜 Nav2
        ↓
🔜 Autonomous Navigation
        ↓
🔜 Camera + YOLO
        ↓
🏁 Complete Autonomous Car
```
