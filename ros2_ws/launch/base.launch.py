from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    params = os.path.join(
      "./",
      'params',
      'basic.yaml'
    )

    return LaunchDescription([
        Node(
            package="http_api",
            namespace="/",
            executable="http_api",
            name="http_api",
            parameters=[params]
        ),
        Node(
            package="task_manager",
            namespace="/",
            executable="task_manager",
            name="task_manager",
            parameters=[params]
        ),
        Node(
            package="low_level_communication",
            namespace="/",
            executable="low_level_communication",
            name="low_level_communication",
            parameters=[params]
        )
    ])
