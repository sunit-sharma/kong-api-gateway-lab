from fastapi import FastAPI

app = FastAPI(
    title="Service A",
    version="1.0.0"
)

@app.get("/api/v1/hello")
def hello():
    return {
     "service": "service-a",
     "version": "v1",
     "message": "Hello from API v1"
    }


@app.get("/health")
def health():
    return {"status": "UP"}
