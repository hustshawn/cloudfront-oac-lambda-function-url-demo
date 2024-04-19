from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()


async def streamer():
    for i in range(20):
        await asyncio.sleep(1.5)
        yield f"<h2>This is streaming from Lambda!</h2>"


@app.get("/")
async def index():
    return StreamingResponse(
        streamer(),
        headers={
            "Content-Type": "text/html",
        },
    )
