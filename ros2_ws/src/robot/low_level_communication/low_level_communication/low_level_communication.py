"""
Check wiki: Software low level communication
And wiki about protocol: High level <-> Low level communication protocol
"""
import rclpy
from rclpy.node import Node

class SpiQueue:
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

    def delete_command(self):
        pass

    def get(self, auto_delete=False):
        pass



class LowLevelCommunication(Node):
    def __init__(self):
        super().__init__('low_level_communication')
        self.commands_queue = SpiQueue()
        self.low_level_data = [-1] * 10
        # self.create_subscription("/raw", )
        # self.create_publisher("/ll_data")

    def add_to_queue(self):
        pass


def main(args=None):
    rclpy.init(args=args)
    
    llc = LowLevelCommunication()

    rclpy.spin(llc)

    llc.destroy_node()
    rclpy.shutdown()
