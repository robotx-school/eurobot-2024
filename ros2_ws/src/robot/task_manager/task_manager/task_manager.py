"""
Check wiki: Software core: Task Manager
"""
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import time

class TaskManager(Node):
    def __init__(self):
        super().__init__('task_manager')

        self.match_start_time = -1

        # Create topics
        self.create_subscription(Int32MultiArray, "/tmgr/signal", self.process_signal, 1)
    
    def process_signal(self, msg):
        data = msg.data
        if len(data) >= 2:
            signal_id = data[0]
            if signal_id == 0: # Start match
                self.match_start_time = time.time()
            elif signal_id == 1: # Stop match
                pass
            elif signal_id == 2: # Health check
                pass
            elif signal_id == 3: # RESET - BYE
                pass
            elif signal_id == 4: # Hardware switch; Real <-> Simulator
                pass



def main(args=None):
    rclpy.init(args=args)
    
    tmgr = TaskManager()

    rclpy.spin(tmgr)

    tmgr.destroy_node()
    rclpy.shutdown()
