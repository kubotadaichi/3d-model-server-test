from fastapi import FastAPI, responses

app = FastAPI()

@app.get("/model")
async def download():
	return responses.FileResponse("model/Running.fbx", filename="model")
