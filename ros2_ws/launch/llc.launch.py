from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    # params = os.path.join(
    #   "./",
    #   'params',
    #   'basic.yaml'
    # )

    return LaunchDescription([
        Node(
            package="low_level_communication",
            namespace="/",
            executable="low_level_communication",
            name="low_level_communication",
            # parameters=[params]
        ),
    ])
