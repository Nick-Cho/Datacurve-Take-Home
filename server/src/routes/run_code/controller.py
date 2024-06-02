import subprocess
import docker
import json
from fastapi import HTTPException

def execute_code(code: str) -> str:
    client = docker.from_env()
    
    try:
        container = client.containers.run(
            image="code-execution-image",
            command=["python3", "/usr/src/app/run_code.py"],
            remove=True,
            stdin_open=True,
            volumes={
                "../../util/run_code.py": {
                    "bind": "/usr/src/app/run_code.py",
                    "mode": "ro"
                }
            },
            environment={"CODE": code},
            working_dir="/usr/src/app",
            detach=False,
            network_disabled=True,
            mem_limit="256m",
            cpu_shares=512
        )
        # Capture the output
        exec_output = container.logs().decode('utf-8')
        exec_result = json.loads(exec_output)
        if exec_result.get("success"):
            return exec_result["output"]
        else:
            raise HTTPException(status_code=400, detail=exec_result["error"]) 
    except docker.errors.ContainerError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

