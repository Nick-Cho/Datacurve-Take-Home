from fastapi import APIRouter
from .controller import execute_code

router = APIRouter()

@router.post("/test-code")
async def test_code(code: str):
    return execute_code(code)
    

