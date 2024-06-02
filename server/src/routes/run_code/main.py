from fastapi import APIRouter
from .controller import execute_code, save_test_code
from .schemas import ExecuteCodeRequest

router = APIRouter()

@router.post("/test-code")
async def test_code(req: ExecuteCodeRequest):
    # logger.debug("Logging code passed to the container: ", code)
    return execute_code(req.code)

@router.post("/submit-code")
async def submit_code(req: ExecuteCodeRequest):
    if (execute_code(req.code).json().get("success")):    
        save_test_code(req.code, execute_code(req.code).json().get("output"))
    
    return execute_code(req.code)
    
