# NTU_COMP30271_RobotSim
NTU COMP30271 Robot Simulation using ROS 2 Humble and Gazebo Fortress
ros2 launch ntu_hmrs_sim maze.launch.py
ros2 launch ntu_hmrs_sim single_robot_sim.launch.py
ros2 launch odom_to_tf_ros2 atlas_odom_to_tf.launch.py
ros2 launch octomap_server2 octomap_server_launch.py
ros2 run rviz2 rviz2
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/atlas/cmd_vel


---Save map
ros2 run map_server map_saver -f my_map  
ros2 run nav2_map_server map_saver_cli -f <directory to save map>/<name of map>
