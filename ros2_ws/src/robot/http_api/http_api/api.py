from fastapi import FastAPI
import uvicorn
from .core.usage import cpu, ram, memory, temperture
from .core.device_info import get_local_ip
from fastapi.middleware.cors import CORSMiddleware
import rclpy
from rclpy.node import Node
import threading

class HttpApi(Node):
    def __init__(self):
        super().__init__('http_api')

        self.declare_parameter('port', 8080)
        self.declare_parameter('host', "0.0.0.0")

        self.app = FastAPI(
            title="HTTP API for robot high-level",
            version="0.0.1"
        )

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        @self.app.get("/", tags=['status'])
        async def health_check():
            return {
                "name": self.app.title,
                "version": self.app.version
            }

        @self.app.get("/stats", tags=['status'])
        async def hl_info():
            return {
                "cpu_usage": cpu(),
                "ram_usage": ram(),
                "sd_usage": memory(),
                "cpu_temperature": temperture(),
                "local_ip": "N/A",
                "auth_data": "pi:pi",
                "api_version": self.app.version,
                "ros_report": f"Mock data: ROS2 Humble",
                "spi_status": "Error"
            }
    
    def run_bg(self):
        server = None

        old_new = uvicorn.Server.__new__

        def spoof_server(self, *_, **__):
            '''Interfeer with __new__ to set server'''
            nonlocal server
            server = old_new(self)
            return server

        uvicorn.Server.__new__ = spoof_server
        uvicorn.Server.install_signal_handlers = lambda *_, **__: None

        threading.Thread(target=lambda: uvicorn.run(self.app, port=self.get_parameter('port').value, host=self.get_parameter('host').value)).start()

        def exit_server():
            server.handle_exit(None, None)

        return exit_server

def main(args=None):
    rclpy.init(args=args)
    
    http_api = HttpApi()
    http_api.run_bg()

    rclpy.spin(http_api)

    http_api.destroy_node()
    rclpy.shutdown()
