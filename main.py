from fastapi import FastAPI
from datetime import datetime
import socket

app=FastAPI()

@app.get("/health")
def health():
    return {
        "status": "ok",
        "timestamp": str(datetime.utcnow())
    }

@app.get("/info")
def info():
    return {
        "app": "DevOps Demo App",
        "version": "1.0.0",
        "hostname": socket.gethostname()
    }
