from fastapi import APIRouter
from .controller import execute_code
from .schemas import ExecuteCodeRequest

router = APIRouter()

@router.post("/test-code")
async def test_code(req: ExecuteCodeRequest):
    # logger.debug("Logging code passed to the container: ", code)
    return execute_code(req.code)
    

