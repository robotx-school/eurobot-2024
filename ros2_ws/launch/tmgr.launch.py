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
            package="task_manager",
            namespace="/",
            executable="task_manager",
            name="task_manager",
            # parameters=[params]
        ),
    ])
