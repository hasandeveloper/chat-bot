from fastapi import APIRouter
from schemas.router_schema import IngestRequest
from services.ingest_service import ingest_file

router = APIRouter()

@router.post("/ingest")
def ingest_controller(request: IngestRequest):
    result = ingest_file(request.file_name, request.s3_url)
    return {
        "status": "success",
        "data": result
    }