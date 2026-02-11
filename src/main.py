from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

def main():
    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()