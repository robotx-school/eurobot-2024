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
    ])
