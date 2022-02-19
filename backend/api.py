from fastapi import FastAPI
import update

app = FastAPI()


# mooth branch
@app.get("/update.py/api_to_json")
def print_api():
    return update.api_to_json()

