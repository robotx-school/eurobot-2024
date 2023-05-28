import psutil

def cpu() -> float:
    return round(psutil.cpu_percent() / 100, 3)

def ram() -> float:
    return round(psutil.virtual_memory().percent / 100, 3)

def memory() -> float:
    return round(psutil.disk_usage("/").percent / 100, 3)

def temperture(machine="dev") -> float:
    try:
        if machine == "dev": # Development laptop scheme
            return psutil.sensors_temperatures()['coretemp'][0].current
        else: # Real RPi
            return psutil.sensors_temperatures()["cpu_thermal"][0].current
    except:
        return 0.0
