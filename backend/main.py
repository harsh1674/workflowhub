from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}