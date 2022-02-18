from fastapi import FastAPI
import update

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/gym/{cap}")
def gym(cap: int):
    return cap * 2


@app.get("update.py/get_api")
def print_api():
    return update.get_api()

