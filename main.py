from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import user

app = FastAPI()

# app.mount("/static", StaticFiles(directory="articles"), name="articles")

orgins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:3000",
    "https://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=orgins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(user.router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message" : "Hello World"}

