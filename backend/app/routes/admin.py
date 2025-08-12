#Admin bot mgmt (create/delete/update bot)
from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/")
def get_admin_dashboard():
    return {"message": "Admin dashboard working"}
