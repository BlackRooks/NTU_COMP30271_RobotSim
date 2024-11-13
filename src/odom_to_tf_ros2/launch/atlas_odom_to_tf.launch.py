from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='odom_to_tf_ros2', 
            executable='odom_to_tf',   
            name='odom_to_tf',
            output='screen',
            parameters=[
                {'odom_topic': '/atlas/odom_ground_truth'},
                {'use_sim_time': True},
            ],
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            arguments=[
                '0', '0', '0',  # Translation: x y z
                '0', '0', '0', '1',  # Rotation: qx qy qz qw
                'atlas/base_link',  # Parent frame
                'atlas/velodyne'  # Child frame
            ],
            parameters=[
                {'use_sim_time': True},
            ],
            output='screen'
        ),
    ])
