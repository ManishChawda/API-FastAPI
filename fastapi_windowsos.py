from fastapi import FastAPI
import platform
import psutil
import time

app = FastAPI()

@app.get("/os-info")
def get_os_info():
    return {
        "os": platform.system(),
        "version": platform.version(),
        "machine": platform.machine(),
        "cpu_percent": psutil.cpu_percent(),
        "virtual_memory" : psutil.virtual_memory(),
        "disk_usage" : psutil.disk_usage("/")

    }

@app.get("/memory")
def memory_info():
    mem = psutil.virtual_memory()

    return {
        "total_gb": round(mem.total/1024/1024/1024,2),
        "available_gb": round(mem.available/1024/1024/1024,2),
        "used_percent" : mem.percent
    }

@app.get("/cpu")
def cpu_info():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "cpu_count": psutil.cpu_count()
    }

@app.get("/uptime")
def uptime():
    boot_time = psutil.boot_time()

    return {
        "uptime_seconds": int(time.time() - boot_time)
    }