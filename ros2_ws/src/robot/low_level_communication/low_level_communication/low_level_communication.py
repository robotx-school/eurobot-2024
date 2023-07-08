"""
Check wiki: Software low level communication
And wiki about protocol: High level <-> Low level communication protocol
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from typing import Tuple, List
from .submodules.spilib import LlcProtocol
import time

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

    def add(self, buffer: List[int]):
        self.commands.append((buffer, time.time()))
 
    def get(self, auto_delete: bool = True) -> Tuple[float, List[int]]:
        """
        Return first command in queue
        Args:
            auto_delete is True, command marks as done (deleted from queue)
        """
        if len(self.commands): # if commands in queue
            if auto_delete:
                return self.commands.pop(0)
            return self.commands[0]

        return ([], 0)

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
        self.communication_works = False
        self.command_interface = LlcProtocol()
        self.create_subscription(Int32MultiArray, "/llc/raw", self.add_to_queue, 1)
        self.ll_polling_timer = self.create_timer(0.05, self.ll_polling)
        self.ll_data_publisher = self.create_publisher(Int32MultiArray, "/llc/data", 1)

    def add_to_queue(self, msg):
        self.get_logger().info("Got spi send request")
        self.commands_queue.add(msg.data)

    def ll_polling(self):
        command, command_add_time = self.commands_queue.get()
        self.command_interface.spi.spi_send(command)
        self.get_logger().info(f"LL polling: {command}")


def main(args=None):
    rclpy.init(args=args)
    
    llc = LowLevelCommunication()

    rclpy.spin(llc)

    llc.destroy_node()
    rclpy.shutdown()
