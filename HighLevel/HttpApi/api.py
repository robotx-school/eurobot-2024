from fastapi import FastAPI
import uvicorn
import core.usage as usage
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HTTP API for robot high-level",
    version="0.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=['status'])
async def health_check():
    return {
        "name": app.title,
        "version": app.version
    }

@app.get("/stats", tags=['status'])
async def hl_info():
    return {
        "cpu_usage": usage.cpu(),
        "ram_usage": usage.ram(),
        "sd_usage": usage.memory(),
        "cpu_temperature": usage.temperture(),
        "local_ip": "192.168.115.200",
        "auth_data": "pi:pi",
        "git_hash": "97b24441c6ae86d189d4cba92cadcaf976676cfe",
        "ros_report": f"roscore {'up'}; {'noetic'} {'1.15.14'}",
        "spi_status": "Error"
    }

if __name__ == "__main__":
    uvicorn.run("api:app", port=8000, host="0.0.0.0", reload=True)
