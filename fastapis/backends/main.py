from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}
