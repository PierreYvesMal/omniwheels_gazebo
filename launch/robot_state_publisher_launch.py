from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open('/home/py/ros2_ws/src/omniwheels_gazebo/urdf/robot.urdf').read()}]
        ),
        # RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', '/home/py/ros2_ws/src/omniwheels_gazebo/rviz/urdf.rviz'],
            output='screen'
        ),
    ])
