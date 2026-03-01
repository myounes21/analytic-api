from fastapi.routing import APIRouter

router = APIRouter()

@router.get("/")
def read_events():
    return {
        "id": [1,2,3]
    }