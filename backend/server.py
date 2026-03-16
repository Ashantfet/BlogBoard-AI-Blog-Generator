from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate")
def generate_blog(topic: str):
    try:
        subprocess.run(
            ["python", "backend/run.py", "--topic", topic],
            check=True
        )
        return {"status": "success", "topic": topic}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
#serve frontend
# app.mount("/",StaticFiles(directory="frontend",html=True),name="frontend")