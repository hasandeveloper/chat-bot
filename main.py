# main.py
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from controllers.ingest_controller import router as ingest_router

app = FastAPI()
app.include_router(ingest_router, prefix="/api")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    # Build a friendly error message
    errors = [{"field": e["loc"][-1], "message": e["msg"]} for e in exc.errors()]
    return JSONResponse(
        status_code=400,
        content={"error": "Invalid request", "details": errors},
    )


@app.get("/")
def home():
    return {"message": "Chatbot Running"}