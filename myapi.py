from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
def index():
    item = {"message": "Hello, World!"}
    return JSONResponse(content=item, status_code=200)
