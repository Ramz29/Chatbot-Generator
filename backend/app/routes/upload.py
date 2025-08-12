from fastapi import APIRouter

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.get("/")
def upload_file():
    return {"message": "Upload Endpoint works."}