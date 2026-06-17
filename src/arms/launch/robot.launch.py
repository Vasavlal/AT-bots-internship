from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Node 1: The Lidar Simulator (0 to 10 loop)
        Node(
            package='lidar',
            executable='lidar.py',
            name='lidar_publisher_node'
        ),
        
        # Node 2: The Movement Controller (Logic for > 3m)
        Node(
            package='wheels',
            executable='wheels.py',
            name='lidar_control_node'
        ),
        
        # Node 3: The Arm Controller (Logic for STOP/MOVE)
        Node(
            package='arms',
            executable='arms.py',
            name='arm_control_node'
        )
    ])

