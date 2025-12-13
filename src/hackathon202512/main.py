from fastapi import FastAPI, responses
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]       # テストなので許して
)

@app.get("/model")
async def download():
	return responses.FileResponse("model/Running.fbx", filename="model.fbx")

@app.get("/model/head")
async def download_head():
    return responses.FileResponse("model/head.fbx", filename="model.fbx")