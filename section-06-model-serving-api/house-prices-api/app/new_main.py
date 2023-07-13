from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/square")
async def square(num: float):
    result = num**2
    return {"squared": result}
