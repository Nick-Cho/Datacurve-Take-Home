from pydantic import BaseModel

class ExecuteCodeRequest(BaseModel):
    code: str

