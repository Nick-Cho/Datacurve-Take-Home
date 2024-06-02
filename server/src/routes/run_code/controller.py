import subprocess
import docker
import json
from sqlalchemy.orm import Session
from ..util.models import CodeSubmission
from ..util.config import get_db
from fastapi import HTTPException, Depends


def execute_code(code: str) -> str:
    client = docker.from_env()
    
    try:
        container = client.containers.run(
            image="datacurve-take-home-backend:latest",
            command=["python3", "/usr/src/app/util/run_code.py"],
            remove=False,
            stdin_open=True,
            volumes={
                "/Users/nickcho/Desktop/Coding/Datacurve-Take-Home/server/src/util/run_code.py": {
                    "bind": "/usr/src/app/util/run_code.py",
                    "mode": "ro"
                }
            },
            environment={"CODE": code},
            working_dir="/usr/src/app/util",
            detach=True,
            # Disable network access so users can't make unauthorized requests on behalf of the server
            network_disabled=True,
            mem_limit="256m",
            cpu_shares=512
        )
        # Capture the output
        container.wait()
        exec_output = container.logs().decode('utf-8')
        exec_result = json.loads(exec_output)
        container.remove()
        if exec_result.get("success"):
            return exec_result["output"]
        else:
            raise HTTPException(status_code=400, detail=exec_result["error"]) 
    except docker.errors.ContainerError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def save_test_code (code: str, output: str, db: Session = Depends(get_db)) -> str:
    code_submission = CodeSubmission(code=code, output=output)
    try:
        db.add(code_submission)
        db.commit()
        db.refresh(code_submission)    
        return "Successfully saved code submission"
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
    

