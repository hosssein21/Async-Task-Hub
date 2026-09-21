from fastapi import FastAPI

app = FastAPI(
    title="AsyncTaskHub",
    description="A concurrent task processing platform",
    version="0.1.0",
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "async-task-hub",
    }