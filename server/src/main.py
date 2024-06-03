from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.run_code.main import router as run_code_router

app = FastAPI(
    title="Code Execution API",
    version="0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(run_code_router)