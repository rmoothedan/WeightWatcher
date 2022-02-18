from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/gym/{cap}")
def gym(cap : int):
    return cap * 2