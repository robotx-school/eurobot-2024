"""
Check wiki: Software low level communication
And wiki about protocol: High level <-> Low level communication protocol
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from typing import Tuple, List

class CommandsQueue:
    """
    Custom queue for commands storage
    """
    def __init__(self) -> None:
        """
        commands struct:
            [
                (spi_send_buffer: List[int], add_time: float)
            ]
        """
        self.commands = []

    def add(self):
        pass
 
    def get(self, auto_delete: bool = False) -> Tuple[float, List[int]] | None:
        """
        Return first command in queue
        Args:
            auto_delete is True, command marks as done (deleted from queue)
        """
        if len(self.commands): # if commands in queue
            return self.commands[0]

        return None

    def delete_command(self, index):
        """
        Delete command by index
        """
        self.commands.pop(index)




class LowLevelCommunication(Node):
    def __init__(self):
        super().__init__('low_level_communication')
        self.commands_queue = CommandsQueue()
        self.low_level_data = [-1] * 10
        self.spi_works = False
        self.create_subscription(Int32MultiArray, "/llc/raw", self.add_to_queue, 1)
        self.ll_polling_timer = self.create_timer(0.1, self.ll_polling)
        # self.create_publisher("/ll_data")

    def add_to_queue(self, msg):
        self.get_logger().info("Got spi send request")

    def ll_polling(self):
        pass


def main(args=None):
    rclpy.init(args=args)
    
    llc = LowLevelCommunication()

    rclpy.spin(llc)

    llc.destroy_node()
    rclpy.shutdown()
