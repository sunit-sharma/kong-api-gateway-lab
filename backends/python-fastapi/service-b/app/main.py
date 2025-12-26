from fastapi import FastAPI

app = FastAPI(
    title="Service B",
    version="1.0.0"
)

@app.get("/api/v1/hello")
def hello():
    return {
     "service": "service-b",
     "version": "v2",
     "message": "Hello from API v2"
    }

@app.get("/health")
def health():
    return {"status": "UP"}
