from fastapi import FastAPI
import update

app = FastAPI()


@app.get("/update.py/api_to_json")
def print_api():
    return update.api_to_json()

